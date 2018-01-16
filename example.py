"""
Copyright (c) 2016-2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import asyncio
import aiohttp
import json

from netdata import Netdata


@asyncio.coroutine
def main():
    with aiohttp.ClientSession() as session:
        data = Netdata('localhost', 'system.cpu', loop, session)
        yield from data.async_get_data()

        print(json.dumps(data.values, indent=4, sort_keys=True))

        # Print the current value of the system's CPU
        print("CPU System:", round(data.values['system'], 2))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

