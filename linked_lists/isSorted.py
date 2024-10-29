class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()
# Given a linked list of size n, you have to find whether the given linked list is sorted or not.
#The sorting can either be non-increasing or non-decreasing.
def isSorted(head):
    curr = head
    while curr.next != None:
        if curr.data > curr.next.data:
            while curr.next != None:
                if curr.data < curr.next.data:
                    return 0
                curr = curr.next
            return 1
        elif curr.data < curr.next.data:
            while curr.next != None:
                if curr.data > curr.next.data:
                    return 0
                curr = curr.next
            return 1
        curr = curr.next
    return 1


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)
print(isSorted(head))
head = Node(10)
head.next = Node(20)
head.next.next = Node(50)
head.next.next.next = Node(40)
printList(head)
print(isSorted(head))

head = Node(19)
head.next = Node(7)
printList(head)
print(isSorted(head))