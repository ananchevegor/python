def findMaxConsecutiveOnes(array):
    k = 0;
    m = [];
    for i in range(0, len(array)):
        if array[i] == array[i - 1] and array[i] != 0:
            k += 1
            m.append(k)
        elif array[i] == 1 and array[i-1] == 0:
            k += 1
            m.append(k)
        else:
            k = 0
        if len(m) == 0:
            m.append(0)
    return max(m)

array = list(map(int, list(input())))
print(findMaxConsecutiveOnes(array))