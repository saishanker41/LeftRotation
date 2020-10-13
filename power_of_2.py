def powerof2(n):

    if n== 1 :
        return True

    elif n == 0 or n % 2 != 0:
        return False 

    return powerof2(n/2)

print(powerof2(5))

