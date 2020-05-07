class LRUCache:
    def __init__(self, capacity, cache):
        self.capacity = capacity
        self.cache = cache

    def get(self, key):
        if key not in self.cache:  # GOTO put
            return False
        self.cache.remove(key)  # remove the key &
        self.cache.append(key)  # add at last
        return True

    def put(self, key):
        if len(self.cache) == self.capacity:
            self.cache.remove(self.cache[0])
        self.cache.append(key)

    def caller(self, key):
        if not self.get(key):  # if false
            self.put(key)

    def display(self):
        for i in self.cache:
            print(i)
        # print(self.cache)


size = 3
cache_memory = []
lru = LRUCache(size, cache_memory)
lru.caller(1)
lru.caller(2)
lru.caller(3)
lru.caller(1)
lru.caller(2)
lru.caller(5)
lru.display()