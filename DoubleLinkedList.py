
class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, elem):
        new_node = DoubleNode(elem)
        if self.head is None:
            self.prev = None
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.next = None
            new_node.prev = current

    def repend(self, elem):
        new_node = DoubleNode(elem)
        if self.head is None:
            self.prev = None
            self.head = new_node
        else:
            self.prev = new_node
            new_node.prev = None
            new_node.next = self.head
            self.head = new_node

    def insert_to_sorted(self, elem):
        new_node = DoubleNode(elem)
        if self.head is None:
            self.prev = None
            self.head = new_node
        elif self.head.data >= elem:
            new_node.next = self.head
            self.prev = new_node
            new_node.prev = None
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < elem:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            new_node.prev = current

    def reverse(self):
        current = self.head
        prev_elem = None
        while current is not None:
                prev_elem = current.prev
                current.prev = current.next
                current.next = prev_elem
                current = current.prev
        if prev_elem is not None:
            self.head = prev_elem.prev

    def print_list(self):
            elemList = []
            current = self.head
            while current is not None:
                elemList.append(current.data)
                current = current.next
            print(elemList)

doublyLinkedList = DoubleLinkedList()
doublyLinkedList.append(2)
doublyLinkedList.append(3)
doublyLinkedList.append(4)
#doublyLinkedList.repend(-1)
#doublyLinkedList.insert_to_sorted(-1)
doublyLinkedList.print_list()
doublyLinkedList.reverse()
doublyLinkedList.print_list()

