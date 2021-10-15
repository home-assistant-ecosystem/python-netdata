"""Test the chart data retrieval."""
import pytest
from pytest_httpx import HTTPXMock

from netdata import Netdata

RESPONSE_VALID = {
    "version": "v1.31.0",
    "uid": "792bb46a-fb11-11e7-b935-e6a17492adc8",
    "mirrored_hosts": ["london3"],
    "mirrored_hosts_status": [
        {
            "guid": "792bb46a-fb11-11e7-b935-e6a17492adc8",
            "claim_id": "792bb46a-fb11-11e7-b935-e6a17492adc8",
        }
    ],
}


@pytest.mark.asyncio
async def test_info_valid(httpx_mock: HTTPXMock):
    """Test a valid response."""
    httpx_mock.add_response(json=RESPONSE_VALID)

    client = Netdata("localhost")
    await client.get_info()

    assert client.info.get("version") == "v1.31.0"
