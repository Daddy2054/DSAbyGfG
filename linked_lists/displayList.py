class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

def displayList(head):
    #code here
    res=[]
    curr = head
    while curr != None:
        res.append(curr.data)
        curr = curr.next
    return res
print(displayList(head))   
head = None
print(displayList(head))
head = Node(10)
print(displayList(head))
print(displayList(head))