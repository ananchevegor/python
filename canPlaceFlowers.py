def canPlaceFlowers(array, n):
    k = 0
    b = None
    for i in range(1, len(array)-1):
        if array[i] == 0:
            if array[i-1] == 0 and array[i+1] == 0:
                k += 1
            else:
                k += 0
    if array[len(array)-2] == 1:
        k += 0
    if array[0] == 0 and array[1] == 0:
        k += 1
    elif array[len(array)-1] == 0 and array[len(array)-2] == 0:
        k += 1
    if k >= n:
        b = True
    else:
        b = False
    return b

array, n = input().split()
n = int(n)
array = list(map(int, list(array)))
print(canPlaceFlowers(array, n))