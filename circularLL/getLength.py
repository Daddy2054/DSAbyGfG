class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getLength(head):
    if head == None:
        return
        count = 1
    curr = head.next
    while curr != head:
        count += 1
        curr = curr.next
    return count


head = Node(10)
head.next = Node(5)
head.next.next = Node(20)
head.next.next.next = Node(15)
head.next.next.next.next = head
print(getLength(head))