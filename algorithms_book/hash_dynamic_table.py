class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# открытая адресация
class HashtableChain:
    def __init__(self, m=10):
        self.table = [[] for i in range(m)]  # создаем список с пустыми списками
        self.m, self.n = m, 0

    def get(self, key):
        hc = hash(key) % self.m  #  высчитываем хэш, искомый ключ должен быть в списке с этим хэшом
        for entry in self.table[hc]:  # находим - возвращаем его value, нет - None
            if entry.key == key:
                return entry.value
        return None

    def put(self, key, value):
        hc = hash(key) % self.m  # в этот индекс нужно записать ключ
        for entry in self.table[hc]:
            if entry.key == key:
                entry.value = value
                return
        if self.n >= self.m - 1:
            raise RuntimeError('Table is full')

        self.table[hc].append(Entry(key, value))  # записываем значение при первом None
        self.n += 1

    # def get_all_table(self):
    #     return [{i.key: i.value} if i is not None else None for i in self.table]


a = HashtableChain()
a.put(1, 10)
a.put(2, 11)
print(a.get(0))
print(a.get(1))
print(a.get(1))
# print(a.get_all_table())
