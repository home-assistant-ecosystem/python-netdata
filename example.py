"""
Copyright (c) 2016-2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import asyncio
import aiohttp
import json

from netdata import Netdata


async def main():
    """Get the data from a Netdata instance."""
    with aiohttp.ClientSession() as session:
        data = Netdata('localhost', loop, session, data='data')
        await data.get_data('system.cpu')

        print(json.dumps(data.values, indent=4, sort_keys=True))

        # Print the current value of the system's CPU
        print("CPU System:", round(data.values['system'], 2))

    with aiohttp.ClientSession() as session:
        data = Netdata('localhost', loop, session, data='alarms')
        await data.get_alarms()

        print(data.alarms)

    with aiohttp.ClientSession() as session:
        data = Netdata('localhost', loop, session)
        await data.get_allmetrics()

        print(data.metrics)

        # Print the current value for the system's CPU
        print("CPU System:", round(data.metrics['system.cpu']
                                   ['dimensions']['system']['value'], 2))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

