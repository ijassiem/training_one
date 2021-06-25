import spead2
import spead2.recv
import logging

logging.basicConfig(level=logging.INFO)

# create threadpool
thread_pool = spead2.ThreadPool()

# create streamConfig
streamConfig = spead2.recv.StreamConfig(memory_allocator=spead2.MemoryPool(16384, 26214400, 12, 8))

# create receiver stream object
stream = spead2.recv.Stream(thread_pool, streamConfig)
del thread_pool

stream.add_udp_reader(8888)  # add udp transport to receiver stream object

ig = spead2.ItemGroup()
num_heaps = 0
for heap in stream:
    print("Got heap", heap.cnt)
    items = ig.update(heap)
    for item in items.values():
        print(f"heap count : {heap.cnt}")
        print(f"item name : {item.name}")
        print(f"item value : {item.value}")
        print(f"item id : {item.id}")
    num_heaps += 1
stream.stop()
print("Received", num_heaps, "heaps")

# heap = stream.get()
# items = ig.update(heap)
# for item in items.values():
#     print(heap.cnt, item.name, item.value)
