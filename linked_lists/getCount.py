class LinkedList:
    def __init__(self,head):
        self.head=head
        self.tail=None

class Solution:

    def getCount(self, head):
            count = 0
            curr = head
            while curr:
                count += 1
                curr = curr.tail
            return count
    
head = LinkedList(1)
head.tail =  LinkedList(2)
head.tail.tail = LinkedList(3)
head.tail.tail.tail = LinkedList(4)
head.tail.tail.tail.tail = LinkedList(5)
print(Solution().getCount(head))