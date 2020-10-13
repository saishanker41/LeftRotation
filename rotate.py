def left_rotate(arr,e,n):
    for i in range(e):
        temp = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
            
        arr[n-1] = temp
             
    for k in range(n):
        print(arr[k])

arr = [2,4,1,1,5,6]
print(left_rotate(arr, 3, 6))



