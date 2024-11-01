class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# You are given a circular linked list 
# insert an element data just after the given position pos.
def insertAtPosition(head,pos,data):
    # code here
        temp = Node(data)
        if pos == 1:
            temp.next = head.next
            head.next = temp
 
            return head


        else:
            curr = head
            curr2= head.next
            for i in range(pos-1):
                if curr2 == head:
                    return head
                curr2 = curr2.next
                curr = curr.next
                if curr == None:
                    return head
            temp.next = curr.next
            curr.next = temp

            return head


def printCircular(head):
    if head == None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

    print()


head = Node(20)
head.next = Node(30)
head.next.next = head
printCircular(head)

printCircular(insertAtPosition(head, 3,10))

#printCircular(head)
