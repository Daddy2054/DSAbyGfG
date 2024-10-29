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

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

def insertAtEnd(head,x):
    #code here
        temp = Node(x)
        if head == None:
            return temp
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = temp
        return head

printList(head)
 
printList(insertAtEnd(head,60)) 
head = None

printList(insertAtEnd(head,60)) 
head = Node(10)
printList(insertAtEnd(head,60))
