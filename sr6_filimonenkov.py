try:
    b= []
    n = int(input("Введите размерность: "))
    if n<0:
        print("Ошибка")
    for Y in range(n):
        c = int(input())
        b.append(c)
    for Y in range(n - 1):
        for P in range(Y, n):
            if b[Y] > b[P]:
                b[P], b[Y] = b[Y], b[P]
    delta = int(input("Введите delta: " ))
    if delta<0:
        print("Ошибка")
    k = 0
    for x in b:
        if x == b[0] + delta:
            k+= 1
    print(k)
except ValueError:
    print("Ошибка")
     
