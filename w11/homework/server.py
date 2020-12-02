import asyncio
import uvicorn
from fastapi import FastAPI

api = FastAPI()


@api.get('/')
async def main():
    await asyncio.sleep(3)
    return 'ok'


if __name__ == '__main__':
    uvicorn.run(api)
