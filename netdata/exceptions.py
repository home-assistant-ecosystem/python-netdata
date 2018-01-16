"""
Copyright (c) 2016-2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""


class NetdataError(Exception):
    """General NetdataError exception occurred."""

    pass


class NetdataConnectionError(NetdataError):
    """When a connection error is encountered."""

    pass
