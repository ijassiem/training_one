"""Client-side code.

This python script uses the Comms class in the comms.py module
to create a client with asyncio for facilitating communication
between two pokemon.
"""

import asyncio
import comms

c = comms.Comms("pikachu", "pika", "Fire")
c.learn_move("glide")
c.print_details()

loop = asyncio.get_event_loop()
loop.run_until_complete(c.client_main())
