def majority_ele(arr):
    max_count = 0
    index = -1
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count > max_count:
            max_count = count
            index = i
    if len(arr) // 2:
        print(arr[index])
    else:
        return 

arr = [2, 2, 5, 2, 3, 6]

print(majority_ele(arr))