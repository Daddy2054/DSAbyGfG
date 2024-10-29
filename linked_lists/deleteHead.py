
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteHead(head):
    #code here
    if head == None:
        return None
    else:

        curr=head.next
        head.next =None
        return curr
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print(head.data)
print(head.next.data)
print(head.next.next.data)
print(head.next.next.next.data)
print(deleteHead(head).data)
print(deleteHead(head).data)
print(deleteHead(head).data)
print(deleteHead(head).data)