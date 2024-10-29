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
    
def deleteAtPosition(head,pos):
    
    if (pos == 1):
        return head.next

    prev = None
    curr = head
    curr_pos = 1

    while (curr_pos < pos):
        prev = curr
        curr = curr.next
        curr_pos += 1

    prev.next = curr.next

    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
printList(head)
deleteAtPosition(head, 3)
printList(head)
deleteAtPosition(head, 2)
printList(head)
deleteAtPosition(head, 1)