# реализация очереди с помощью двоичной кучи

class Entry:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PQ:
    def less(self, i, j):
        """Проверяет, что storage[i] имеет меньший приоритет, чем storage[j]."""
        return self.storage[i].priority < self.storage[j].priority

    def swap(self, i, j):
        """меняет местами узлы i и j."""
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    def __init__(self, size):
        """Узлы хранятся в ячейках от storage[1] до storage[size], а узел 0 не используется."""
        self.size = size
        self.storage = [None] * (size + 1)
        self.n = 0

    def enqueue(self, value, priority):
        """Чтобы добавить элемент в кучу, надо разместить его в первой свободной клетке массива, а затем
        позволить ему всплыть."""
        if self.n == self.size:
            raise RuntimeError('Priority queue is full!')
        self.n += 1
        self.storage[self.n] = Entry(value, priority)
        self.swim(self.n)

    def swim(self, child):
        """Перестраивает массив storage, возвращая куче пирамидальность."""
        while child > 1 and self.less(child//2, child):  # родительский узел для child находится в child//2
            self.swap(child, child//2)
            child = child//2

    def dequeue(self):
        if self.n == 0:
            raise RuntimeError('Priority queue is empty!')
        max_entry: Entry = self.storage[1]  # запоминаем ячейку на вершине кучи
        self.storage[1] = self.storage[self.n]  # переставляем на вершину самый последний элемент, а его место освобождаем
        self.storage[self.n] = None
        self.n -= 1
        self.sink(1)
        return max_entry.value

    def sink(self, parent):
        while 2*parent <= self.n:  # проверка продолжается, пока у узла есть хотя бы один левый потомок
            child = 2*parent
            if child < self.n and self.less(child, child+1):  # если правый потомок существует и приоритет левого потомка меньше, нам нужен правый потомк
                child += 1
            if not self.less(parent, child):  # если приоритет родителя не меньше максимального приоритета потомков, пирамидальность восстановлена
                break
            self.swap(child, parent)  # если нет, то меняем местами родителя и потомка
            parent = child
