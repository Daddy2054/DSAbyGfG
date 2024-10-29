class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def areIdentical(head1,head2):
    # Code here
        while head1 and head2:
            if head1.data != head2.data:
                return False
            head1 = head1.next
            head2 = head2.next
        return True 

head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)
head1.next.next.next = Node(40)

head2 = Node(10)
head2.next = Node(20)
head2.next.next = Node(30)
head2.next.next.next = Node(40)

print(areIdentical(head1,head2))

head2.next.next.next = Node(50)

print(areIdentical(head1,head2))