import aiofile
import asyncio
import aiohttp
import re
import time


async def process_response(url, client):
    async with client.get(url) as response:
        response_text = await response.text()

        for line in response_text:
            if re.search(r"<a >", line):
                async with aiofile.AIOFile("found.txt", "a") as file:
                    await file.write(line + " <------was founded")


async def read_urls(file):
    async with aiofile.AIOFile(file, "r") as file:
        async with aiohttp.ClientSession() as client:
            tasks = []
            async for url in aiofile.LineReader(file):
                tasks.append(asyncio.create_task(process_response(url, client)))

            await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    time_start = time.time()
    loop.run_until_complete(read_urls("urls.txt"))
    print("Took time:", time.time() - time_start)

