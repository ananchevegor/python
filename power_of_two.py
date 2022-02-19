def power_of_two(n, k):
    if (n == 2 or n==1) and k == 0:
        return 'YES'
    x = n / 2
    if (int(x) / float(x) == 1) and x > 1:
        k += 1
        return power_of_two(x, k)
    if x == 1 and k > 0:
        return 'YES'
    else:
        return 'NO'

n = int(input())
k = 0
print(power_of_two(n, k))