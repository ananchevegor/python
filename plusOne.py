def plusOne(n):
    n[len(n)-1] = n[len(n)-1] + 1
    if n[len(n)-1] == 10:
        n.remove(n[len(n)-1])
        n.append(1)
        n.append(0)
    return n
n = list(map(int, list(input())))
print(plusOne(n))