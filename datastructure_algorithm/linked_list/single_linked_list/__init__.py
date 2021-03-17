# Python code for the implementation of the methods of single linked list

class Node:

    # Constructor for Node
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:

    # Constructor for Linked list
    def __init__(self):
        self.head = None

    # insert a new Node with a data in the beginning of the linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = l_list.head
        l_list.head = new_node

    # insert a new Node with a data after a particular Node of the Linked list
    def insert_after(self, previous_node, new_data):
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    # insert a new Node with a data at the end of the Linked list
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    # delete a node from the Linked list
    def delete(self, key):
        temp = self.head

        # delete the first node of the Linked list
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # searching for the node with data as key
        while temp is not None:
            if temp.data == key:
                break
            previous = temp
            temp = temp.next

        # if key is not present in the Linked list
        if temp is None:
            return "Key not found in the list."

        # unlink the node from the Linked list
        previous.next = temp.next
        temp = None

    # Traverse from the head till the last node of the linked list
    # and print the data of each node while traversing.
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end= " ")       # new_learning :D
            current = current.next


if __name__ == '__main__':
    l_list = LinkList()

    # creating 3 nodes
    head_node = Node(7)
    second_node = Node(2)
    third_node = Node(4)

    # updating the pointers of the node
    head_node.next = second_node
    second_node.next = third_node

    # updating the head of the linked list
    l_list.head = head_node         # 7->2->4->Null

    # insertion in the beginning of the linked list
    l_list.push(0)          # 0->7->2->4->Null

    # insertion after any particular node of the linked list
    l_list.insert_after(l_list.head, 5)       # 0->5->7->2->4->Null

    # insertion at the end of the linked list
    l_list.append(11)  # 0->5->7->2->4->11->Null

    # delete a node from the linked list
    l_list.delete(7)    # 0->5->2->4->11->Null

    # printing the value of the nodes in the linked list
    l_list.print_list()