class Queue:
    def __init__(self, length):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = length

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def queue_size(self):
        return len(self.queue)

    def get_capacity(self):
        return self.capacity

    def queue_front(self):
        if self.is_empty():
            print("Empty queue.")
            return
        return self.queue[self.front]

    def enqueue(self, new_data):
        if self.is_full():
            print("Full queue exception")
            return
        self.queue.append(new_data)
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            print("Empty queue exception")
            return
        self.queue.pop(0)
        self.rear -= 1

    def print_queue(self):
        if self.is_empty():
            print("Empty queue.")
            return
        for i in self.queue:
            print(i, end="<-")
        print("")

    def delete_queue(self):
        del self.queue
        print("Queue deleted.")


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

