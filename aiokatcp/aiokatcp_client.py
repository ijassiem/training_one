"""This code creates an aiokatcp client using the aiokatcp module."""

import asyncio
import aiokatcp

IP_ADDRESS = 'localhost'
PORT = 4444

async def run_client():
    """Co-routine starts an aiokatcp client with requests to server."""
    client = await aiokatcp.Client.connect(IP_ADDRESS, PORT)
    async with client:
        reply, informs = await client.request('time')
        for r in reply:
            print(r.decode('ascii'))
        print('----------------------')
        reply, informs = await client.request('help')
        for inform in informs:
            print(b' '.join(inform.arguments).decode('ascii'))
        print('----------------------')
        value, _ = await client.request('echo', 'Hello','Goodbye')
        for v in value:
            print(v.decode('ascii'))

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(run_client())
