d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
values = list(d.values())
keys = list(d.keys())
d = dict(zip(values, keys))
print(d)
