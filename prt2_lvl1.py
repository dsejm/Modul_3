l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
l_dubl = [x for i, x in enumerate(l) if i != l.index(x)]
print(l_dubl)

