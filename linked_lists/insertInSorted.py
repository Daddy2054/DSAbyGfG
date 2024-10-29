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

#insert the given data at appropriate position in the linked list.
def insertInSorted(head,data):
    #code here
    new_node = Node(data)
    if head == None or head.data >= data:
        new_node.next = head
        return new_node
    
    curr = head
    while curr.next != None and curr.next.data < data:
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head
    
    
printList(head) 

printList (insertInSorted(head,25))
printList(head)    
printList(insertInSorted(head,  26))
printList(head)    
printList(insertInSorted(head, 225))
printList(head)    