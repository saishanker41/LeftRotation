def sum_of(arr):
    
    sum = 0
    for i in arr:
        sum = sum +i
        
    return sum


def missing_num(arr,n):
    sum_of_Elements = n *(n+1)//2
    return sum_of_Elements - sum_of(arr)

arr = [1,2,3,4,5,6,8]
n = len(arr) + 1
print(missing_num(arr,n))    

        
