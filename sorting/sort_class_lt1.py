#Below code sort the list based on first value of pair and if first values are same in some pairs then it will sort them based on second value of pair.



class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):

        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x


l = [Point(1, 15), Point(10, 5), Point(1, 8)]
l.sort()

for i in l:
    print(i.x, i.y)
