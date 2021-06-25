import spead2
import spead2.send
import logging
import numpy as np

logging.basicConfig(level=logging.INFO)

# create threadpool
thread_pool = spead2.ThreadPool()

# create streamConfig
streamConfig = spead2.send.StreamConfig(rate=1e7)

# create sender stream object. Defines transport as UDP stream
stream = spead2.send.UdpStream(thread_pool, [("127.0.0.1", 8888)], streamConfig)
del thread_pool

shape_foo = (4, 5)
shape_bar = (10, 2)
ig = spead2.send.ItemGroup(flavour=spead2.Flavour(4, 64, 48, 0))  # create item group

ig.add_item(0x1234, 'foo', 'a foo item', shape=shape_foo, dtype=np.int32)  # add item to item group
ig["foo"].value = np.zeros(shape_foo, np.int32)  # assign value to item

ig.add_item(0x2345, 'bar', 'a bar item', shape=shape_bar, dtype=np.int32)  # add item to item group
ig["bar"].value = np.ones(shape_bar, np.int32)  # assign value to item

#ig.add_item(0x3456, 'num', 'a num item', shape=[], format=[('u',48)] # Immediate item
#ig["num"].value = 2000000 # not working

stream.send_heap(ig.get_heap())  # send heap with stream
stream.send_heap(ig.get_end())
print("End reached.")
