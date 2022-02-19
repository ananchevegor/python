def pivotIndex(array):
    x = 0
    for i in range(1, len(array)-1):
        sum = 0
        sum1 = 0
        for j in range(0, i):
            sum =sum+array[j]
        for k in range(i+1, len(array)):
            sum1 =sum1+array[k]
        if(sum == sum1):
            x = i
            break
    else:
        x = -1
    sum2=0
    for a in range(1,len(array)):
        sum2+=array[a]
    if (sum2==0):
        x = 0
    return x
array = list(map(int, input().split(',')))
print(pivotIndex(array))