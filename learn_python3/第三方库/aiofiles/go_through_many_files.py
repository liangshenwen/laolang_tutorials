import aiofiles
import asyncio
import json
from pathlib import Path

# 当前目录
directory = '.'


async def main():
    pathlist = Path(directory).glob('*.json')

    # Iterate through all json files in the directory.
    for path in pathlist:
        # Read the contents of the json file.
        async with aiofiles.open(f'{directory}/{path.name}', mode='r') as f:
            contents = await f.read()

        # Load it into a dictionary and create a list of moves.
        pokemon = json.loads(contents)
        name = pokemon['name']
        moves = [move['move']['name'] for move in pokemon['moves']]

        # Open a new file to write the list of moves into.
        async with aiofiles.open(f'{directory}/{name}_moves.txt', mode='w') as f:
            await f.write('\n'.join(moves))


asyncio.run(main())
