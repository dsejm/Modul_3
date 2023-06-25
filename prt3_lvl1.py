a = int(input("Введите сторону A: "))
b = int(input("Введите сторону B: "))
c = int(input("Введите сторону C: "))
def area (a, b, c):
    p = (a + b + c)/2
    square = (p*(p-a)*(p-b)*(p-c)) ** 0.5 #теперь должно быть корректно
    print(square)
area (a, b, c)
