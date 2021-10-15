"""Test the connection."""
import pytest
from pytest_httpx import HTTPXMock

from netdata import Netdata
import httpx


@pytest.mark.asyncio
async def test_timeout(httpx_mock: HTTPXMock):
    """Test if the connection is hitting the timeout."""

    def raise_timeout(request, extensions: dict):
        """Set the timeout for the requests."""
        raise httpx.ReadTimeout(
            f"Unable to read within {extensions['timeout']}", request=request
        )

    httpx_mock.add_callback(raise_timeout)

    with pytest.raises(httpx.ReadTimeout):
        client = Netdata("localhost")
        await client.get_info()
