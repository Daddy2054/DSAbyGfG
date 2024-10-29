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
#to insert a new node in 
#	the middle of the linked list with
#	the given value. 
def insertInMiddle(head,x):
        if head is None:
            return Node(x)
        else:
            # Create a new node
            new_node = Node(x)
            slow = head
            fast = head.next
            
            # Find the middle node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                    
            # Insert the new node after the middle node
            new_node.next = slow.next
            slow.next = new_node
            
            # Return the head of the linked list
            return head



printList(head)
 
printList(insertInMiddle(head,60)) 
printList(insertInMiddle(head,35)) 
head = None

printList(insertInMiddle(head,60)) 
head = Node(10)
printList(insertInMiddle(head,60))
printList(insertInMiddle(head,20))
head = Node(1)
head.next = Node(2)
head.next.next = Node(4)
printList(insertInMiddle(head,3))
#728 279 868 363 966 212 111 329 859
head = Node(728)
head.next = Node(279)
head.next.next = Node(868)
head.next.next.next = Node(363)
head.next.next.next.next = Node(966)
head.next.next.next.next.next = Node(212)
head.next.next.next.next.next.next = Node(111)
head.next.next.next.next.next.next.next = Node(329)
head.next.next.next.next.next.next.next.next = Node(859)
printList(insertInMiddle(head,88))

head = Node(610)
head.next = Node(585)
head.next.next = Node(541)
head.next.next.next = Node(76)
head.next.next.next.next = Node(523)
head.next.next.next.next.next = Node(862)
head.next.next.next.next.next.next = Node(284)
# 610 585 541 76 523 862 284
#720 input
#610 585 541 720 76 523 862 284 wrong
#610 585 541 76 720 523 862 284  correct
printList(insertInMiddle(head,720))
