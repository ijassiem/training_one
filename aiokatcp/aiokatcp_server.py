"""This module contains a class called MyServer for creating an aiokatcp server."""

import aiokatcp
import asyncio
import datetime


class MyServer(aiokatcp.DeviceServer):
    """Example of derived class for aiokatcp server.

       This class is required for implementing an aiokatcp server. The class inherits
       from the aiokatcp.DeviceServer base class required for running an aiokatcp server.
       Methods are added to the class for replying to current date and time requests, and
       echoing commands sent by client.
    """

    VERSION = "myserver-api-1.0"
    BUILD_STATE = "myserver-1.0.1.dev0"

    async def request_time(self, ctx):
        """Reply with current date and time.

        Returns
        ------
        Tuple(str)
            Tuple contains a string indicating the current date amd time.
        """
        return "Current date and time", str(datetime.datetime.now())

    async def request_echo(self, ctx, *args: str):
        """Return the arguments to the caller.

        Returns
        ------
        Tuple(str)
            Tuple contains the string arguments.
        """
        return tuple(args)


async def main():
    """Start aiokatcp server and reply to requests from client."""
    server = MyServer("localhost", 4444)
    await server.start()
    await server.join()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    asyncio.get_event_loop().close()
