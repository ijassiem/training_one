"""This module contains a Comms class for providing client-server communication between two pokemon."""

import asyncio
import random
import pokemon.pokemon as pkmn


class Comms(pkmn.ElectricPokemon):
    """
    This Comms class inherits from the ElectricPokemon class.

    Adds client-server communication between pokemon, implemented with asyncio and co-routines.

    Attributes
    ----------
    name : str
        Name of pokemon.
    nickname : str
        Nickname of pokemon.
    moves : list
        A list of 4 pokemon moves.
    pokemon_type : str
        Type of pokemon.
    ip_address : str
        The IP address as the client or server (default 127.0.0.1).
    port_no : int
        The port number to communicate on (default 8765).
    """

    def __init__(self, name, nickname, pokemon_type, ip_address="127.0.0.1", port_no=8765):
        """Initialise Comms class object.

        Initialise with the arguments name, nickname and type, and with
        optional keyward arguments ip_address and port_no.

        Parameters
        ----------
        name : str
            Name of pokemon.
        nickname : str
            Nickname of pokemon.
        pokemon_type : str
            Type of pokemon.
        ip_address : str
            The IP address as the client or server (default 127.0.0.1).
        port_no : int
            The port number to communicate on (default 8765).
        """
        self.ip_address = ip_address
        self.port_no = port_no
        super(Comms, self).__init__(name, nickname, pokemon_type)

    async def msg_tx(self, message, writer):
        """Write message to socket.

        Parameters
        ----------
        message : str
            The message to write to socket.
        writer :  StreamWriter object
            Object instance of StreamWriter class for writing to socket.
        """
        print(f"Sending: {message!r}")
        writer.write(message.encode())
        await writer.drain()

    async def random_num_tasks(self, writer):
        r"""Create random number of tasks for writing messages to socket.

        Each message ends with a \n. Multiple messages are sent as a group
        of messages, and gets terminated with 'EOM' to indicate the end of transmission.

        Parameters
        ----------
        writer :  StreamWriter object
            Object instance of StreamWriter class for writing to socket.
        """
        message = self.name + ".\n"
        tasks = []
        random_no = random.randint(1, 5)
        print(f"Random number generated = {random_no}")
        for i in range(random_no):
            tasks.append(self.msg_tx(message, writer))
        await asyncio.gather(*tasks)
        await self.msg_tx("EOM\n", writer)

    async def read_data(self, reader):
        """Read asynchronously from socket.

        The reading of data is carried out in a while loop. All received messages are stored in list.
        Breaks out of while loop if a message is received containing 'EOM' or 'last message'

        Parameters
        ----------
        reader :  StreamReader object
            Object instance of StreamReader class for reading from socket.

        Returns
        -------
        len(msg_list) : tuple int
            Integer value indicating number of messages received and appended to list.
        end : tuple bool
            True or False indicating if connection should be ended.
        """
        msg_list = []
        end = False
        while True:
            data = await reader.readline()
            print(f"Received: {data.decode()!r}")
            msg_list.append(data)
            if data.decode() == "EOM\n":
                print("EOM received and breaking out.")
                print(f"Number of messages received = {len(msg_list) - 1}")
                break
            elif "last message" in data.decode():
                end = True
                print("End = True")
                break
        return len(msg_list), end

    async def handle_echo(self, reader, writer):
        """Handle messages received on server-side.

        This co-routine/callback is invoked by the server when a new client connection is established.
        If a single message is received from the client, then server replies with a final message and
        terminates connection. If end flag is True then connection is also terminated without replying.

        Parameters
        ----------
        reader :  StreamReader object
            Object instance of StreamReader class for reading from socket.
        writer : StreamWriter object
            Object instance of StreamWriter class for writing to socket.
        """
        first_msg = True

        while True:
            if not first_msg:
                await self.random_num_tasks(writer)
            num_msgs, end = await self.read_data(reader)
            first_msg = False
            if num_msgs == 2:
                print("Sending last message.")
                await self.msg_tx(f"{self.name} last message\n", writer)
                await self.msg_tx("EOM\n", writer)
                break
            elif end:
                break
        print("Closing connection after 1 second.")
        await asyncio.sleep(1)
        writer.close()
        await writer.wait_closed()  # used with writer.close
        print("Connection closed.")

    async def server_main(self):
        """Co-routine starts up the socket server."""
        server = await asyncio.start_server(self.handle_echo, self.ip_address, self.port_no)

        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")

    async def client_main(self):
        """Co-routine runs the socket client.

        The sending and receiving of messages from the client-side runs in a while loop.
        If a single message is received from the server, then the client replies with a final message and
        terminates connection. If end flag is True then the connection is also terminated without replying to the server.
        """
        reader, writer = await asyncio.open_connection(self.ip_address, self.port_no)
        while True:
            await self.random_num_tasks(writer)
            num_msgs, end = await self.read_data(reader)
            if num_msgs == 2:
                print(f"Number of msgs received = {num_msgs - 1}")
                print("Sending last message.")
                await self.msg_tx(f"{self.name} last message\n", writer)
                await self.msg_tx("EOM\n", writer)
                break
            elif end:
                break
        print("Closing connection after 1 second.")
        await asyncio.sleep(1)
        writer.close()
        await writer.wait_closed()  # used with writer.close
        print("Connection closed.")
