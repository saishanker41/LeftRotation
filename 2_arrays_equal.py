def arrEqual(arr1, arr2):
    if(len(arr1) != len(arr2)):
        return False

    arr1.sort()
    arr2.sort()    

    for i in range(len(arr1)-1):
        if arr1[i] != arr2[i]:
           return False
    return True

arr1 = [2,4,6,1,0,7]
arr2 = [7,2,1,0,4,6]
if (arrEqual(arr1, arr2)):
    print("Yes")
else:
    print("No")    
