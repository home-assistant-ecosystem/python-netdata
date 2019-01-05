"""Execptions for the Python Netdata client."""


class NetdataError(Exception):
    """General NetdataError exception occurred."""

    pass


class NetdataConnectionError(NetdataError):
    """When a connection error is encountered."""

    pass
