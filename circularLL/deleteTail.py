class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Given a circular linked list of size n, 
# you have to delete the tail (last element) in the linked list.
def deleteTail(head):
    if head == None:
        return
    curr = head
    while curr.next.next != head:
        curr = curr.next
    curr.next = head
    return head



        

def printCircular(head):
    if head == None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

    print()


head = Node(10)
head.next = Node(20)
head.next.next = head
printCircular(head)

head = deleteTail(head)

printCircular(head)
