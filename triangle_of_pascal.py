rows = []
def triangle_of_pascal(n):
    row = [1]
    for i in range(n):
        #print(row)
        rows.append(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]

    print(rows, end=' ')
    return ''

n= int(input())
print(triangle_of_pascal(n))