
def rotate_left(arr, d):
      n = len(arr)
      d = d % n  # Handle cases where d > n
      arr[:] = arr[d:] + arr[:d]
      return arr
  

l = [10, 20, 30, 40]
rotate_left(l,2)
print(l)
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotate_left(l,3)
print(l)
