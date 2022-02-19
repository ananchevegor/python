def reverse_number(n):
    return str(n % 10) + " " + reverse_number(n // 10) if n else ""

n = int(input())
print(reverse_number(n))