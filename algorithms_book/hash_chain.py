class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class DynamicHashtable:
    def __init__(self, m=10):
        self.table = [[] for i in range(m)]  # создаем список с пустыми списками
        if m < 1:
            raise ValueError('Hashtable storage must be at least 1')
        self.m, self.n = m, 0
        self.load_factor = 0.75
        self.threshold = min(m * self.load_factor, m - 1)  # максимальный порог заполненности, при его пересечении создается новая таблица

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

        if self.n >= self.threshold:  # если порог переступлен, то вызываем resize
            self.resize(2*self.m + 1)

    def resize(self, new_size):
        temp = DynamicHashtable(new_size)  # временная таблица
        for bucket in self.table:  # обязательно нужно заполнить новую таблицу так, а не скопировать (ведь хэш поменялся)
            for key, value in bucket:
                temp.put(key, value)
        self.table, self.m = temp.table, temp.m
        self.threshold = self.load_factor * self.m


a = DynamicHashtable()
a.put(1, 10)
a.put(2, 11)
print(a.get(0))
print(a.get(1))
print(a.get(1))
