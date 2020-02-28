class FrequencyList(list):

    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1

        return counts


foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
print("Length is", len(foo))
foo.pop()
print("After pop", repr(foo))
print("Frequency: ", foo.frequency())


class BinaryNode(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


bar = [1, 2, 3]
print(bar[0])
print(bar.__getitem__(0))


class IndexableNode(BinaryNode):

    def _search(self, count, index):
        if not self.left and not self.right:
            return

        while index > 0:
            index -= 1

    def _pre_traverse(self, root):
        if not root:
            return
        self._pre_traverse(root.left)
        self._pre_traverse(root.right)

    def __getitem__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError("Index out of range")
        return found.value


tree = IndexableNode(
    10,
    left=IndexableNode(
        5,
        left=IndexableNode(2),
        right=IndexableNode(
            6, right=IndexableNode(7))),
    right=IndexableNode(
        15, left=IndexableNode(11)
    )
)
