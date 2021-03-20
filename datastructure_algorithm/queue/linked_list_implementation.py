class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, capacity):
        self.head = None
        self.front = self.rear = 0
        self.capacity = capacity

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.queue_size() == self.capacity

    def queue_size(self):
        if self.is_empty():
            print("Empty queue.")
            return
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def get_capacity(self):
        return self.capacity

    def queue_front(self):
        if self.is_empty():
            print("Empty queue.")
            return
        return self.head.data

    def enqueue(self, new_data):
        if self.rear == self.capacity:
            print("Full queue exception.")
            return
        new_node = Node(new_data)
        if self.is_empty():
            self.head = new_node
            self.rear += 1
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            print("Empty queue exception.")
            return
        temp = self.head
        if self.head.next is not None:
            self.head = self.head.next
        else:
            self.head = None
        temp.next = None
        self.rear -= 1
        return temp.data

    def print_queue(self):
        if self.is_empty():
            print("Empty stack.")
            return
        current = self.head
        while current is not None:
            print(current.data, end= "<-")
            current = current.next
        print("")

    def delete_queue(self):
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
    queue = Queue(4)
    queue.print_queue()
    queue.enqueue(70)
    queue.enqueue(50)
    queue.enqueue(40)
    queue.enqueue(90)
    print(queue.queue_size())
    print(queue.is_full())
    print(queue.is_empty())
    queue.enqueue(20)
    queue.print_queue()
    print(queue.rear)
    queue.dequeue()
    queue.print_queue()
    print(queue.rear)
    print(queue.queue_front())
    queue.delete_queue()






