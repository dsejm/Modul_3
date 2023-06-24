from random import randint
def sort_list(x):
    global list_sorted
    list_sorted = sorted(x, reverse=True)
    print(list_sorted)
    return list_sorted
def max_num():
    new_max_num = str(list_sorted[0]) + str(list_sorted[1]) + str(list_sorted[2]) + str(list_sorted[3]) + str(list_sorted[4])
    print(new_max_num)

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
print(m)
a, b, c, d, e = m
sort_list(a)
max_num()


