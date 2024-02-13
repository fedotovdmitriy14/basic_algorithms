class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None  # если дерево пустое - None

    def insert(self, value):  # добавляет val в дерево
        self.root = self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value):
        if node is None:  # основание рекурсии: если поддерево пусто, возвращаем новый узел
            return BinaryNode(value)

        if value <= node.value:  # добавляем в левое поддерево
            node.left = self._insert(node.left, value)
        else:  # в правое
            node.right = self._insert(node.right, value)
        return node

    def __contains__(self, target):
        """Проверяет, есть ли значение в дереве"""
        node = self.root
        while node:  # ищем вглубь дерева
            if target == node.value:
                return True
            if target < node.value:  # идем по левой ветви
                node = node.left
            else:  # по правой
                node = node.right
        return False

    def _remove_min(self, node: BinaryNode):
        """Удаляет наименьший элемент дерева с корнем node."""
        if node.left is None:  # если у узла нет левого потомка, значит, он содержит наименьшее значение в дереве; поднимаем на его место правое поддерево
            return node.right
        node.left = self._remove_min(node.left)
        return node

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value):
        if node is None:
            return None

        if value < node.value:  # удалять надо из левого поддерева
            node.left = self._remove(node.left, value)
        elif value > node.value:  # удалять надо из правого поддерева
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            original, node = node, node.right  # ищем узел без левого потомка
            while node.left:
                node = node.left

            node.right = self._remove_min(original.right)
            node.left = original.left

        return node

    def __iter__(self):
        yield from self._inorder(self.root)

    def _inorder(self, node: BinaryNode):
        """Обход бинарного дерева в порядке по возрастанию."""
        if node is None:
            return

        print(f'{node.value=}')

        for value in self._inorder(node.left):
            yield value

        yield node.value

        for value in self._inorder(node.right):
            yield value


# Test data for insertion
insertion_data = [5, 3, 7, 2, 4, 6, 8]

# Test data for removal
removal_data = [3, 6, 8]

# Test data for traversal
traversal_data = [5, 3, 7, 2, 4, 6, 8]


tree = BinaryTree()
for value in insertion_data:
    tree.insert(value)


for value in tree:
    print(value)
