def binarysearch(arr, n):
    low = 0
    mid = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2

        if arr[mid] > n:
            high = mid - 1
        elif arr[mid] < n:
            low = mid + 1
        else:
            return mid 
    return -1

arr = [9,18,19,24,43]
n = 19
result = binarysearch(arr,n)

if result != -1:
    print("Number is present at index", str(result))
else:
    print("Number is not present")    