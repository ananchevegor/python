def triangle_sequence(n):
    k = 1
    for i in range(1, n + 1):
        print(k, end=' ')
        if i == k * (k + 1) // 2:
            k += 1
    return ''


n = int(input())
print(triangle_sequence(n))
