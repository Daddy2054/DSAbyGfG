class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

    #Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        if head == None:
            return -1
        first = head
        for i in range (k):
            if first == None:
                return -1
            first=first.next
        second=head
        while first!= None:
            second=second.next
            first=first.next
        return second.data
    
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
print(Solution().getKthFromLast(head,1))
print(Solution().getKthFromLast(head,2))
print(Solution().getKthFromLast(head,3))
print(Solution().getKthFromLast(head,4))