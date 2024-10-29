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


    
def printNthFromEnd(head,n):
    if head == None :
        return
    first = head
    for i in range (n):
        if first == None:
            return
        first=first.next
    second=head
    while first!= None:
        second=second.next
        first=first.next
    print(second.data)
        
        
    
            
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
printNthFromEnd(head,1)
