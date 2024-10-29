class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

#check if the given linked list is palindrome or not.
def isPalindrome(head):
    #code here
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        left = head
        right = prev
        while right != None:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True



def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(30)
head.next.next.next.next = Node(20)
head.next.next.next.next.next = Node(110)
printList(head)

print(isPalindrome(head))

printList(head)
