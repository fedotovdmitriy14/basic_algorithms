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
        hc = hash(key) % self.m  #  высчитываем хэш, искомый ключ должен быть в этом индексе или где-то за ним (при коллизии)
        while self.table[hc]:  # если какой-то индекс None, то этого ключа в списке нет
            if self.table[hc].key == key:
                return self.table[hc].value
            hc = (hc + 1) % self.m
        return None

    def put(self, key, value):
        hc = hash(key) % self.m  # в этот индекс нужно записать ключ
        while self.table[hc]:  # пройдемся по таблице начиная с нужного хэша, пока не встретим None
            if self.table[hc].key == key:  # коллизия! здесь перезаписываем значение (возможны другие варианты)
                self.table[hc].value = value
                return
            hc = (hc + 1) % self.m

        if self.n >= self.m - 1:
            raise RuntimeError('Table is full')

        self.table[hc] = Entry(key, value)  # записываем значение при первом None
        self.n += 1

    def get_all_table(self):
        return [{i.key: i.value} if i is not None else None for i in self.table]


a = HashtableOpenAddress()
a.put(1, 10)
a.put(2, 11)
print(a.get(0))
print(a.get(1))
print(a.get(1))
print(a.get_all_table())
