def akkerman(m, n):
    if m == 0:
        return (n + 1)
    if m > 0 and n == 0:
        return akkerman(m - 1, 1)
    if m > 0 and n > 0:
        return akkerman(m - 1, akkerman(m, n - 1))


m, n = map(int, input().split())
print(akkerman(m, n))
