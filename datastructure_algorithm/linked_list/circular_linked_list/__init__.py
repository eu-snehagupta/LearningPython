class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def length(self):

        if self.head is None:
            return 0
        if self.head.next == self.head:
            return 1

        count = 1
        current = self.head
        while True:
            count += 1
            current =current.next
            if current.next == self.head:
                break
        return count

    def print_list(self):

        if self.head is None:
            print("Empty list!")
            return

        current = self.head
        while True:
            print(current.data, end= " ")
            current = current.next
            if current == self.head:
                break

    def push(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head


if __name__ == '__main__':
    l_list = CircularLinkedList()

    l_list.push(4)
    l_list.append(11)

    l_list.push(9)
    l_list.append(7)

    print(l_list.length())         # 4
    l_list.print_list()     # 9->4->11->7
