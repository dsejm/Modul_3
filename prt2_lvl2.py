from random import randint

n = 5
m = [[randint(0, 100) for i in range(n)]for j in range(n)]
a, b, c, d, e = m
max_list = a + b + c + d + e
max_num = max(max_list)
print(m)
print(max_list)
print(max_num)

