"""Client to retrieve data from a Netdata instance."""
import logging
from typing import Dict

import httpx
from yarl import URL

from . import exceptions

_LOGGER = logging.getLogger(__name__)
DATA_ENDPOINT = "data?chart={resource}&before=0&after=-1&options=seconds"
ALARMS_ENDPOINT = "alarms?all&format=json"
ALL_METRIC_ENDPOINT = (
    "allmetrics?format=json&help=no&types=no&" "timestamps=yes&names=yes&data=average"
)
ALARM_COUNT = "alarm_count?context={resource}&status=RAISED"

API_VERSION = 1


class Netdata(object):
    """A class for handling connections with a Netdata instance."""

    def __init__(self, host, port=19999, tls=None, path=None):
        """Initialize the connection to the Netdata instance."""
        self.host = host
        self.port = port
        self.values = self.alarms = self.metrics = None

        self.scheme = "http" if tls is None or not False else "https"

        if path is None:
            self.base_url = URL.build(
                scheme=self.scheme, host=host, port=port, path=f"/api/v{API_VERSION}/"
            )
        else:
            self.base_url = URL.build(
                scheme=self.scheme, host=host, port=port, path=path
            )

    async def get_data(self, url) -> Dict:
        """Execute a request to a data endpoint."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(str(url))
        except httpx.ConnectError:
            raise exceptions.NetdataConnectionError(
                f"Connection to {self.scheme}://{self.host}:{self.port} failed"
            )

        if response.status_code == httpx.codes.OK:
            _LOGGER.debug(response.json())
            try:
                return response.json()
            except TypeError:
                _LOGGER.error("Can not load data from Netdata")
                raise exceptions.NetdataError("Unable to get the data from Netdata")

    async def get_chart(self, resource):
        """Get the details about a chart."""
        url = URL(self.base_url) / DATA_ENDPOINT.format(resource=resource)
        data = await self.get_data(url)

        try:
            self.values = {k: v for k, v in zip(data["labels"], data["data"][0])}
        except TypeError:
            raise exceptions.NetdataError("Format of data doesn't match")

    async def get_alarms(self):
        """Get alarms for a Netdata instance."""
        url = URL(self.base_url) / ALARMS_ENDPOINT
        self.alarms = await self.get_data(url)

    async def get_allmetrics(self):
        """Get all available metrics from a Netdata instance."""
        url = URL(self.base_url) / ALL_METRIC_ENDPOINT
        self.metrics = await self.get_data(url)

    async def get_info(self):
        """Get information about the Netdata instance."""
        url = URL(self.base_url) / "info"
        self.info = await self.get_data(url)
