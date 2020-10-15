def left_rotate(arr,e,n):
    for i in range(e):
        temp = arr[0]
        print(temp, "--")
        for j in range(n-1):
            arr[j] = arr[j+1]
            print(arr[j], "()")
            
        arr[n-1] = temp
        print(arr[n-1])
             
    for k in range(n):
        print(arr[k], end = " ")

arr = [2,4,3,1,5,6]
print(left_rotate(arr, 3, 6))



