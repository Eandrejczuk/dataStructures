# the class creating a node of linked list
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def to_string(self):
        return 'node: ' + str(self.data)
# the class creating linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # a method to append at the end of the list
    def append(self, elem):
        new_elem = Node(elem)
        if self.head is None:
            self.head = new_elem
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_elem

    # a method to add an element at the position position
    def insert_at_position(self, position, data):
        if position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            n = self.head
            while count < position -1 and n is not None:
                n = n.next
                count += 1
            if n is None:
                print("Index out of bound")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
    # remove an element at the position position
    def delete_at_position(self,position):
        if position == 0:
            self.head = self.head.next
        else:
            count = 0
            n = self.head
            while count < position - 1 and n is not None:
                n = n.next
                count += 1
            if n is None:
                print("Index out of bound")
            else:
                n.next = n.next.next
    # reverse linked list
    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    #return length of the linked list
    def length(self):
        current = self.head
        total = 0
        while current is not None:
            total += 1
            current = current.next
        return total
    # print linked list
    def print_list(self):
        list_of_elem = []
        current = self.head
        while current is not None:
            list_of_elem.append(current.data)
            current = current.next
        print(list_of_elem)

# compare two linked lists. Return True if identical and false otherwise.
def compare_lists(llist1, llist2):
    head1 = llist1.head
    head2 = llist2.head
    if llist1.length() != llist2.length():
        return False
    while head1 is not None:
        if head1.data == head2.data:
            head1 = head1.next
            head2 = head2.next
        else:
            return False
    return True

# get length given head of linked list
def get_length(head):
    total = 0
    current = head
    while current is not None:
        total +=1
        current = current.next
    return total

#return linked list element on the positionFromTail position from the tail
def getNode(head, positionFromTail):
    current = head
    length = get_length(head)
    if length <= positionFromTail:
        print("index out of bound")
        return 0
    count = 0
    while count < length - positionFromTail -1 and current is not None:
        current = current.next
        count += 1
    return current.data

# the function checks if the linked list contains cycles
def has_cycle(head):
    if head == None:
        print("Index out of bound")
        return 0
    fast_pointer = head
    slow_pointer = head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True
    return False

#the method merges two linked lists
def mergeLists(head1, head2):
    n1 = head1
    n2 = head2
    new_llist = LinkedList()
    while n1 and n2:
        if n1.data >= n2.data:
            new_llist.append(n2.data)
            n2 = n2.next
        else:
            new_llist.append(n1.data)
            n1 = n1.next
    while n1:
        new_llist.append(n1.data)
        n1 = n1.next
    while n2:
        new_llist.append(n2.data)
        n2 = n2.next
    return new_llist

def delete_duplicates(head):
    current = head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

def print_list_from_head(head):
    list = []
    current = head
    while current:
        list.append(current.data)
        current = current.next
    return list


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
#linked_list.add_at_position(1,5)
linked_list.insert_at_position(3,5)
#linked_list.delete_at_position(3)

linked_list2 = LinkedList()
linked_list2.append(2)
linked_list2.append(3)
linked_list2.append(3)
linked_list2.append(3)
linked_list2.append(3)
linked_list2.append(3)
#linked_list2.append(1)
#linked_list2.append(1)

#print(linked_list.length())
#linked_list.reverse()

linked_list.print_list()

llist_merged = mergeLists(linked_list.head,linked_list2.head)
llist_merged.print_list()

head_removed= delete_duplicates(llist_merged.head)
print(print_list_from_head(head_removed))
#linked_list2.print_list()

#print(getNode(linked_list.head, 4))
#print(has_cycle(linked_list.head))

#print(compare_lists(linked_list,linked_list2))



