x=10+20j
print(type(x))

print('-------------------------')

x=10+20J
print(type(x))
print(x.real)
print(x.imag)

print('-------------------------')

x=10.5 + 20.5J
print(type(x))
print(x.real)
print(x.imag)

# x=10+20i # SyntaxError: invalid syntax

print('-------------------------')
x= 0B1111 + 20j
print(x.real)
print(x.imag)

print('-------------------------')
# x= 15 + 0B1111j # SyntaxError: invalid syntax
print('-------------------------')
x=10+20j
y=20+30j
print(x+y)
print(x-y)
print(x*y)
print(x/y)
