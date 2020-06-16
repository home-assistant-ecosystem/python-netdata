"""Client to retrieve data from a Netdata instance."""
import asyncio
import logging
import socket

import aiohttp
import async_timeout
from yarl import URL

from . import exceptions

_LOGGER = logging.getLogger(__name__)
_DATA_ENDPOINT = "data?chart={resource}&before=0&after=-1&options=seconds"
_ALARMS_ENDPOINT = "alarms?all&format=json"
_ALL_METRIC_ENDPOINT = (
    "allmetrics?format=json&help=no&types=no&" "timestamps=yes&names=yes&data=average"
)

API_VERSION = 1


class Netdata(object):
    """A class for handling connections with a Netdata instance."""

    def __init__(self, host, loop, session, port=19999, path=None):
        """Initialize the connection to the Netdata instance."""
        self._loop = loop
        self._session = session
        self.host = host
        self.port = port
        self.values = self.alarms = self.metrics = None
        if path is None:
            self.base_url = URL.build(scheme="http", host=host, port=port, path=f"/api/v{API_VERSION}/")
        else:
            self.base_url = URL.build(scheme="http", host=host, port=port, path=path)


    async def get_data(self, resource):
        """Get detail for a resource from the data endpoint."""
        self.endpoint = _DATA_ENDPOINT
        url = "{}{}".format(self.base_url, self.endpoint.format(resource=resource))

        try:
            with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url)

            _LOGGER.info("Response from Netdata: %s", response.status)
            data = await response.json()
            _LOGGER.debug(data)
            self.values = {k: v for k, v in zip(data["labels"], data["data"][0])}

        except (asyncio.TimeoutError, aiohttp.ClientError, socket.gaierror):
            _LOGGER.error("Can not load data from Netdata")
            raise exceptions.NetdataConnectionError()

    async def get_alarms(self):
        """Get alarms for a Netdata instance."""
        self.endpoint = _ALARMS_ENDPOINT
        url = "{}{}".format(self.base_url, self.endpoint)

        try:
            with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url)

            _LOGGER.debug("Response from Netdata: %s", response.status)
            data = await response.json()
            _LOGGER.debug(data)
            self.alarms = data

        except (asyncio.TimeoutError, aiohttp.ClientError, socket.gaierror):
            _LOGGER.error("Can not load data from Netdata")
            raise exceptions.NetdataConnectionError()

    async def get_allmetrics(self):
        """Get all available metrics from a Netdata instance."""
        self.endpoint = _ALL_METRIC_ENDPOINT
        url = "{}{}".format(self.base_url, self.endpoint)

        try:
            with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url)

            _LOGGER.debug("Response from Netdata: %s", response.status)
            data = await response.json()
            _LOGGER.debug(data)
            self.metrics = data

        except (asyncio.TimeoutError, aiohttp.ClientError, socket.gaierror):
            _LOGGER.error("Can not load data from Netdata")
            raise exceptions.NetdataConnectionError()
