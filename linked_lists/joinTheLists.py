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

head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)
head1.next.next.next = Node(40)
head1.next.next.next.next = Node(50)

head2 = Node(100)
head2.next = Node(200)
head2.next.next = Node(300)
head2.next.next.next = Node(400)
head2.next.next.next.next = Node(500)
#join the head of second list to the tail of first 
# so that we can traverse both the lists using head of 1st list.
def joinTheLists(head1, head2):
    #code here
    curr = head1
    while curr.next != None:
        curr = curr.next
    curr.next = head2
    return head1
    


    
    
printList(head1) 

printList (joinTheLists(head1, head2))
printList(head1)    
   