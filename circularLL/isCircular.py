class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Given the head, the head of a singly linked list, Returns true 
# if the linked list is circular & false if it is not circular.
def isCircular(head):
        if head == None:
            return True
        curr = head.next
        while curr != None and curr != head:
            curr = curr.next
        return curr == head




        

def printCircular(head):
    if head == None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

    print()


head = Node(10)
head.next = Node(20)
head.next.next = head
printCircular(head)

print(isCircular(head))

printCircular(head)
