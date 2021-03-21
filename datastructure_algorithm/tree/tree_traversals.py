class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_pre_order(root):
    if root:
        print(root.val)
        print_pre_order(root.left)
        print_pre_order(root.right)


def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.val)
        print_in_order(root.right)


def print_post_order(root):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.val)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder traversal: ")
    print_pre_order(root)

    print("Inorder traversal: ")
    print_in_order(root)

    print("Postorder traversal: ")
    print_post_order(root)