import asyncio
import json
from pathlib import Path

import aiofiles

directory = '.'

async def write_pokemon_moves(filename):
    await asyncio.sleep(2)
    # Read the contents of the json file.
    async with aiofiles.open(f'{directory}/{filename}', mode='r') as f:
        contents = await f.read()

    # Load it into a dictionary and create a list of moves.
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]

    # Open a new file to write the list of moves into.
    async with aiofiles.open(f'{directory}/{name}_moves.txt', mode='w') as f:
        await f.write('\n'.join(moves))
    return { 'name': name, 'moves': moves }


async def main():
    pathlist = Path(directory).glob('*.json')

    # A list to be populated with async tasks.
    tasks = []

    # Iterate through all json files in the directory.
    for path in pathlist:
        print(path)
        # 在write_pokemon_moves会停留2秒钟，整个过程需要len(pathlist) * 2
        # await write_pokemon_moves(path.name)

        # 因为使用了并发操作，这个过程大概是2秒多一点
        tasks.append(asyncio.ensure_future(write_pokemon_moves(path.name)))

    # Will contain a list of dictionaries containing Pokemons' names and moves
    moves_list = await asyncio.gather(*tasks)
    print(moves_list)


asyncio.run(main())