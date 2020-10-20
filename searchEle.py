def search_ele(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [15,23,1,6,95]
key = 1

result = search_ele(arr, key)
if result != -1:
    print("Number is present at index", str(result))
else:
    print("Number is not present in array")    
