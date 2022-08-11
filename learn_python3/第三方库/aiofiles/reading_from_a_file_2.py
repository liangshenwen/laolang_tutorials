import aiofiles
import asyncio
import json


async def main():
    async with aiofiles.open('articuno.json', mode='r') as f:
        async for line in f:
            print(line, end='')

asyncio.run(main())