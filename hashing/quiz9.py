def findSymPairs(arr, row):
    hM = dict()
    for i in range(row):
        first = arr[i][0]
        sec = arr[i][1]
        if (sec in hM.keys() and hM[sec] == first):
            print("(", sec,",", first, ")")
        else:
            hM[first] = sec
        
if __name__ == '__main__':
    arr = [[0 for i in range(2)]
      for i in range(5)]
    arr[0][0], arr[0][1] = 11, 20
    arr[1][0], arr[1][1] = 30, 40
    arr[2][0], arr[2][1] = 5, 10
    arr[3][0], arr[3][1] = 40, 30
    arr[4][0], arr[4][1] = 10, 5
    findSymPairs(arr, 5)
