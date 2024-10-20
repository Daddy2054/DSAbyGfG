check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
check2 = check1
check3 = check1[:]

check2[0] = 'Code'
check3[1] = 'Mcq'
print(check1)
print(check2)
print(check3)

count = 0
for c in (check1 , check2 , check3):
    if c[0] == 'Code':
        count += 1
    if c[1] == 'Mcq':
        count += 10
print(count)

#quiz6
list1= range(100,110)
print(list1.index(105))

#quiz7
list1=[1998,2022]
list2=[2014,2016]
print((list1+list2)*2)