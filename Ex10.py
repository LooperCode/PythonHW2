n = int(input("Введите число: "))
tmp = 1
for i in range(n):
    if tmp > n:
        break
    else:
        print(tmp, end=' ')
        tmp = tmp * 2
print('\n')
        