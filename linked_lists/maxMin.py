class Node:
    def __init__(self, k):
        self.data = k
        self.next = None
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

def maximum(head):
    res=head.data
    curr = head
    while curr is not None:
        res = curr.data if curr.data > res else res
        curr = curr.next
    return res

print(maximum(head))

def minimum(head):
    res=head.data
    curr = head
    while curr is not None:
        res = curr.data if curr.data < res else res
        curr = curr.next
    return res

print(minimum(head))