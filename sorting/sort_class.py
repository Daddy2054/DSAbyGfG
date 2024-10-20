#  The below example sorts the list in increasing order based on the first value of pair.
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def myFun(p):
    return p.x


l = [Point(1, 15), Point(10, 5), Point(3, 8)]
l.sort(key=myFun)

for i in l:
    print(i.x, i.y)
