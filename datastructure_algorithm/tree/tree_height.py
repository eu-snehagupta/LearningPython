class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)


if __name__ == '__main__':

    node = Node(1)
    node.left = Node(2)
    node.left.left = Node(3)
    node.left.right = Node(4)
    node.right = Node(5)

    binary_tree = Tree()
    binary_tree.root = node

    print(binary_tree.height(node))
