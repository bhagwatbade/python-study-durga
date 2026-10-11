def f1():
    print('Hello')

x = f1()
print(x)

print('--------------------------------------------')

a = None
print(type(a))
print(id(a))

print('--------------------------------------------')

a = None
b = None
c = None
d = f1()

print(a, b, c, d)
print(id(a), id(b), id(c), id(d))