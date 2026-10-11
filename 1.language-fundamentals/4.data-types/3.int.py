# 1) decimal
a=10
print(a)

print('---------------------------------')

# 2) binary
a=0B1111
print(a)

print('-----------------')

a=0B1011
print(a)

#a=0B123 # IndentationError: unexpected indent

print('---------------------------------')

# 3) Octal
a=0O123
print(a)

print('-----------------')

a=0o174
print(a)

#a=0O786 # SyntaxError: invalid syntax

print('---------------------------------')

# 4) Hexa decimal
a=0XFACE
print(a)

print('-----------------')

a=0xbeef
print(a)

#a=0XBeer # SyntaxError: SyntaxError: invalid syntax

print('---------------------------------')

# 1) bin()

print(bin(15))
print(bin(0b101))
print(bin(0o11))
print(bin(0x10))


print('---------------------------------')

# 2) oct()

print(oct(15))
print(oct(0b101))
print(oct(0o11))
print(oct(0x10))

print('---------------------------------')

# 2) hex()

print(hex(15))
print(hex(0b101))
print(hex(0o11))
print(hex(0x10))

print('---------------------------------')

