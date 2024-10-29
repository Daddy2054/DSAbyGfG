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

#insert an element data just after the given position pos.
def insertAtPosition(head,pos,data):
    #code here
        # if pos == 1:
        #     new_node = Node(data)
        #     new_node.next = head
        #     return new_node
        
        #return head
        #else:
            curr = head
            for i in range(pos-1):
                curr = curr.next
                if curr == None:
                    return head
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node

            return head
    
    
printList(head) 

printList (insertAtPosition(head,2,25))
printList(head)    
printList(insertAtPosition(head, 1, 26))
printList(head)    
printList(insertAtPosition(head, 8, 25))
printList(head)    