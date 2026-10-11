l = [10, 20, 30, 40]
b = bytearray(l)

for x in b:
    print(x)

print('--------------------------------------------')

b[0] = 77

for x in b:
    print(x)