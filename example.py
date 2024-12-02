"""Sample code to interact with a Netdata instance."""
import asyncio
import json

from netdata import Netdata


async def main():
    """Get the data from a Netdata instance."""
    client = Netdata("localhost")

     # Get all metrics
    await client.get_info()
    print(client.info)

    # Get details of a available chart
    await client.get_chart("system.cpu")
    print(json.dumps(client.values, indent=4, sort_keys=True))

    # Print the current value of the system's CPU
    print("CPU System:", round(client.values["system"], 2))

    # Get the alarms which are present
    await client.get_alarms()
    print(client.alarms)

    # Get all metrics
    await client.get_allmetrics()
    print(client.metrics)

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())