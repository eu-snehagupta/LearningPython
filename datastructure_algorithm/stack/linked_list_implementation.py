class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Empty stack.")
            return
        temp = self.head
        if self.head.next is not None:
            self.head = self.head.next
        else:
            self.head = None
        temp.next = None
        return temp.data

    def top(self):
        if self.is_empty():
            print("Empty stack.")
            return
        return self.head.data

    def print(self):
        if self.is_empty():
            print("Empty stack.")
            return
        current = self.head
        while current is not None:
            print(current.data, end= " ")
            current = current.next

    def delete(self):
        if self.is_empty():
            print("Empty stack.")
            return
        current = self.head
        while current is not None:
            temp = current.next
            del current.data
            current = temp
        self.head = None


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.pop()
    stack.push(7)
    stack.push(2)
    stack.print()
    print("\n", stack.is_empty())
    print(stack.pop())
    stack.push(4)
    stack.print()
    print("\n", stack.top())
    stack.print()
    stack.delete()
    stack.print()


