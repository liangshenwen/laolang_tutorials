import aiofiles
import asyncio
import json


async def main():
    async with aiofiles.open('articuno.json', mode='r') as f:
        contents = await f.read()
    pokemon = json.loads(contents)
    print(pokemon['name'])

asyncio.run(main())