s = {10,20,30,40}
fs = frozenset(s)
print(fs)

# fs.add(50) # AttributeError: 'frozenset' object has no attribute 'add'

# fs.remove(30) # AttributeError: 'frozenset' object has no attribute 'remove'