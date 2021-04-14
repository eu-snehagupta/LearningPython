class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right =  None


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, val):
        return self.queue.append(val)

    def dequeue(self):
        return self.queue.pop(0)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if root is None:
            self.root = Node(val)
            return self.root

        if root.val >= val:
            current = self.insert(root.left, val)
            root.left = current
        else:
            current = self.insert(root.right, val)
            root.right = current
        return root

    def print_pre_order(self, root):
        if root:
            print(root.val)
            self.print_pre_order(root.left)
            self.print_pre_order(root.right)

    def print_in_order(self, root):
        if root:
            self.print_in_order(root.left)
            print(root.val)
            self.print_in_order(root.right)

    def print_post_order(self, root):
        if root:
            self.print_post_order(root.left)
            self.print_post_order(root.right)
            print(root.val)

    def print_level_order(self, root):
        if root is None:
            return
        directory_queue = Queue()
        directory_queue.enqueue(root)
        while not(directory_queue.is_empty()):
            current = directory_queue.dequeue()
            print(current.val, end=" ")
            if current.left:
                directory_queue.enqueue(current.left)
            if current.right:
                directory_queue.enqueue(current.right)


if __name__ == '__main__':

    data = [3, 5, 4, 7, 2, 1]

    binary_tree = BinaryTree()
    root = None

    for i in range(len(data)):
        root = binary_tree.insert(root, data[i])

    # print("Preorder traversal: ")
    # binary_tree.print_pre_order(root)
    #
    # print("Inorder traversal: ")
    # binary_tree.print_in_order(root)
    #
    # print("Postorder traversal: ")
    # binary_tree.print_post_order(root)

    print("Levelorder traversal: ")
    binary_tree.print_level_order(root)