class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_Node = Node(data)

        if self.head is None:
            self.head = new_Node
            return self.head

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_Node
        return self.head

    def display(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def remove_duplicate(self):
        if self.head is None:
            return
        current = self.head
        while current.next is not None:
            current_value = current.data
            next_value = current.next.data
            if current_value == next_value:
                temp = current.next
                current.next = current.next.next
                temp = None
                del temp
            else:
                current = current.next
        return self.head


if __name__ == '__main__':
    data = [1, 2, 2, 2, 3, 3, 4]

    l_list = LinkedList()

    for i in range(len(data)):
        l_list.insert(data[i])
    l_list.display()

    l_list.remove_duplicate()
    print("Remove duplicates")
    l_list.display()

