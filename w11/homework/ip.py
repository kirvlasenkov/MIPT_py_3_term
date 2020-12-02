from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp
import json

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def fetch_ip(service, session):
    async with session.get(service.url) as ip_response:
        ip = await ip_response.text()
        ip_parsed = json.loads(ip)["query"]

        return f"Your IP: {ip_parsed}"


async def asynchronous():
    aws = [
        fetch_ip(service=service, session=aiohttp.ClientSession())
        for service in SERVICES
    ]

    done, pending = await asyncio.wait(aws, return_when=FIRST_COMPLETED)

    for aw in done:
        print(aw.result())


if __name__ == "__main__":
    ioloop = asyncio.get_event_loop()

    start_time = time.time()
    ioloop.run_until_complete(asynchronous())
    print("Took time: ", time.time() - start_time)
