class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#the function displayList() which takes head reference as argument and 
# returns the circular linked list as a list.


def displayList(head):
    if head == None:
        return
    list = []
    list.append(head.data)
    curr = head.next
    while curr != head:
        list.append(curr.data)
        curr = curr.next
    return list


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
head.next.next = Node(15)
head.next.next.next = Node(30)
head.next.next.next.next = head

printCircular(head)

print(displayList(head))

printCircular(head)
