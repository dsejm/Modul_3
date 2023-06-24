x = int(input())
p = int(input())
y = int(input())
year = 0

while x < y:
    x = (x + (x * (p/100))) // 1
    year += 1

print(year)

