class BinaryNode(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree(object):

    def __init__(self, root=None):
        self._root = root

    def add(self, item):
        node = BinaryNode(item)
        if not self._root:
            self._root = node
            return

        queue = [self._root]
        while queue:
            cur = queue.pop(0)
            if not cur.left:
                cur.left = node
                return
            elif not cur.right:
                cur.right = node
                return
            else:
                queue.append(cur.left)
                queue.append(cur.right)

    def pre_traverse(self, root):
        if not root:
            return
            # raise ValueError("root Error")

        print("value: ", root.value)
        self.pre_traverse(root.left)
        self.pre_traverse(root.right)

    def mid_traverse(self, root):
        if not root:
            return
        self.mid_traverse(root.left)
        print("value:", root.value)
        self.mid_traverse(root.right)

    def post_traverse(self, root):
        if not root:
            return
        self.post_traverse(root.left)
        self.post_traverse(root.right)
        print(root.value)


if __name__ == '__main__':
    '''
                10 
              /    \
              20   100
            /   \      \
            78  2      33 
    '''
    node = BinaryNode(10,
                      left=BinaryNode(20, left=BinaryNode(78), right=BinaryNode(2)),
                      right=BinaryNode(100, left=None, right=BinaryNode(33)),
                      )
    tree = Tree(node)
    tree.pre_traverse(node)
    print("-" * 20)
    tree.mid_traverse(node)
    print("-" * 20)
    tree.post_traverse(node)
