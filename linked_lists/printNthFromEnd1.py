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
    len = 0 
    curr = head
    while curr:
        curr=curr.next
        len+=1
    if len<n :
        return
    curr = head
    for i in range (1,len-n+1):
        curr = curr.next
    print(curr.data)
        
    
            
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
printNthFromEnd(head,1)
