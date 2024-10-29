class Node:
    def __init__(self, k):
        self.data = k
        self.next = None
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

def sumOfElements(head):
    #code here
    res=0
    curr = head
    while curr != None:
        res+=curr.data
        curr = curr.next
    return res
print(sumOfElements(head))   
head = None
print(sumOfElements(head))
head = Node(10)
print(sumOfElements(head))
print(sumOfElements(head))