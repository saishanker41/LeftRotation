def printmaxele(arr, k, n):
    max = 0
    for i in range(n-k+1):
        max = arr[i]
        for j in range(1,k):
            if arr[i + j] > max:
                max = arr[i + j]
        print(str(max) + " ", end = " ")

arr = [1,9,4,6,2,1,1,6,2,10]
k = 3
n = len(arr)
printmaxele(arr, k, n)