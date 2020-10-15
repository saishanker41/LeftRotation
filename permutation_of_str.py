def permutation_str(List):
    return ''.join(List)

def permut(s,l,r):
    if l == r:
        print(permutation_str(s))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            #print(a[l])
            permut(s,l+1,r)
            a[l], a[i] = a[i], a[l]

string = "COMPUTER"
n = len(string)
a = list(string)
permut(a,0,n-1)
