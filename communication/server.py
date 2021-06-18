"""Server-side code.

This python script uses the Comms class in the comms.py module
to create a server with asyncio for facilitating communication
between two pokemon.
"""

import asyncio
import comms

c = comms.Comms("charmander", "char", "Fire")
c.learn_move("Leap")
c.print_details()
try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(c.server_main())
    loop.run_forever()
except KeyboardInterrupt:
    loop.close()
