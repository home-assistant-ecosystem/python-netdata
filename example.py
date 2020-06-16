"""Sample code to interact with a Netdata instance."""
import asyncio
import aiohttp
import json

from netdata import Netdata


async def main():
    """Get the data from a Netdata instance."""
    async with aiohttp.ClientSession() as session:
        data = Netdata("localhost", loop, session)
        # Get data for the CPU
        await data.get_data("system.cpu")
        print(json.dumps(data.values, indent=4, sort_keys=True))

        # Print the current value of the system's CPU
        print("CPU System:", round(data.values["system"], 2))

        # Get the alarms which are present
        await data.get_alarms()
        print(data.alarms)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
