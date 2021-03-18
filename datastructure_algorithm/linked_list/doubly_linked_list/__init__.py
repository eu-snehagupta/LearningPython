class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self, ):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)

        self.head.prev = new_node
        new_node.next = self.head

        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current
        return

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Previous Node cannot be null")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next
        if prev_node.next is not None:
            prev_node.next.prev = new_node

        prev_node.next = new_node
        new_node.prev = prev_node

    def delete_node(self, node_to_delete):

        if self.head is None or node_to_delete is None:
            return

        if self.head == node_to_delete:
            node_to_delete.next.prev = None
            self.head = node_to_delete.next
            del node_to_delete
            return

        if node_to_delete.next is None:
            node_to_delete.prev = None
            del node_to_delete
            return

        node_to_delete.next.prev = node_to_delete.prev
        node_to_delete.prev.next = node_to_delete.next
        del node_to_delete
        return

    def print_list(self):
        if self.head is None:
            print("Empty list!")
            return

        current =self.head
        print("Traversing in forward direction: ")
        while current:
            print(current.data, end = " ")
            temp = current
            current = current.next

        current = temp
        print("\nTraversing in backward direction: ")
        while current:
            print(current.data, end=" ")
            current = current.prev


if __name__ == '__main__':
    l_list = DoublyLinkedList()

    l_list.append(4)
    l_list.push(7)
    l_list.push(1)
    l_list.append(9)

    l_list.insert_after(l_list.head.next.next, 8)
    l_list.delete_node(l_list.head.next)

    l_list.print_list()









