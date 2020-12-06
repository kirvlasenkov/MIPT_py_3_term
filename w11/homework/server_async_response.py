import asyncio
import aiohttp
import time

WORKERS_NUM = 200


async def get_response(session, link):
    async with session.get(link) as response:
        text = await response.text()
        print(text)


if __name__ == "__main__":
    tasks = [
        get_response(aiohttp.ClientSession(), "http://127.0.0.1:8000")
        for _ in range(WORKERS_NUM)
    ]

    loop = asyncio.get_event_loop()

    start = time.time()
    loop.run_until_complete(asyncio.gather(*tasks))
    print("Took time: ", time.time() - start)
