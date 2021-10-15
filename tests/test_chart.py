"""Test the chart data retrieval."""
import pytest
from pytest_httpx import HTTPXMock

from netdata import Netdata, exceptions

RESPONSE_VALID = {
    "labels": [
        "time",
        "guest_nice",
        "guest",
        "steal",
        "softirq",
        "irq",
        "user",
        "system",
        "nice",
        "iowait",
    ],
    "data": [
        [1634256154, 0, 0, 0, 0.2506266, 3.759398, 32.45614, 6.015038, 0, 0.1253133]
    ],
}


@pytest.mark.asyncio
async def test_chart_valid(httpx_mock: HTTPXMock):
    """Test a valid response."""
    httpx_mock.add_response(json=RESPONSE_VALID)

    client = Netdata("localhost")
    await client.get_chart("system.cpu")

    assert client.values.get("system") == 6.015038
