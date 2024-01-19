class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# открытая адресация
class HashtableOpenAddress:
    def __init__(self, m=10):
        self.table = [None] * m
        self.m, self.n = m, 0

    def get(self, key):
        hc = hash(key) % self.m
        while self.table[hc]:
            if self.table[hc].key == key:
                return self.table[hc].value
            hc = (hc + 1) % self.m
        return None

    def put(self, key, value):
        hc = hash(key) % self.m
        while self.table[hc]:
            if self.table[hc].key == key:
                self.table[hc].value = value
                return
            hc = (hc + 1) % self.m

        if self.n >= self.m - 1:
            raise RuntimeError('Table is full')

        self.table[hc] = Entry(key, value)
        self.n += 1


a = HashtableOpenAddress()
a.put(1, 10)
print(a.get(0))
print(a.get(1))
