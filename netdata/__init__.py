"""
Copyright (c) 2016-2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import asyncio
import logging
import socket

import aiohttp
import async_timeout

from . import exceptions

_LOGGER = logging.getLogger(__name__)
_RESOURCE = 'http://{host}:{port}/api/v{api}/data?chart={resource}&{realtime}'
_REALTIME = 'before=0&after=-1&options=seconds'

API_VERSION = 1


class Netdata(object):
    """A class for handling connections with a Netdata instance."""

    def __init__(self, host, resource, loop, session, port=19999):
        """Initialize the connection to the Netdata instance."""
        self._loop = loop
        self._session = session
        self.host = host
        self.port = port
        self.resource = resource
        self.values = None

    async def async_get_data(self):
        url = _RESOURCE.format(
            host=self.host, port=self.port, api=API_VERSION,
            resource=self.resource, realtime=_REALTIME)

        try:
            with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url)

            _LOGGER.debug(
                "Response from Netdata: %s", response.status)
            data = await response.json()
            _LOGGER.debug(data)
            self.values = {k: v for k, v in zip(
                data['labels'], data['data'][0])}

        except (asyncio.TimeoutError, aiohttp.ClientError, socket.gaierror):
            _LOGGER.error("Can not load data from Netdata")
            raise exceptions.NetdataConnectionError()
