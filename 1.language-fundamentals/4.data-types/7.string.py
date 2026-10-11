s='a'
print(s)
print(type(s))

print('-------------------------------------')

s='durga'
print(s)
print(type(s))

print('-------------------------------------')

s="durga"
print(s)
print(type(s))

print('-------------------------------------')

s="""durga"""
print(s)
print(type(s))

print('-------------------------------------')

# s='durga
# software
# solution' # SyntaxError: EOL while scanning string literal

# s=""durga
# software
# solution"" # SyntaxError: invalid syntax

s="""durga
software
solution"""
print(s)
print(type(s))

print('-------------------------------------')

s='''durga
software
solution'''
print(s)
print(type(s))

print('-------------------------------------')

s = "class by 'durga' is very good"
print(s)

print('-------------------------------------')

s = 'class by "durga" is very good'
print(s)

print('-------------------------------------')

s = """class by "durga" is 'very' good"""
print(s)

print('-------------------------------------')

s = '''class by "durga" is 'very' good'''
print(s)

print('---------------------------------------------------------------------------------------------------------------')

s='durga'
print(s[0])
print(s[3])
# print(s[100]) # IndexError: string index out of range
print(s[-1])
print(s[-5])
# print(s[-6]) # IndexError: string index out of range

print('---------------------------------------------------------------------------------------------------------------')

# slicing of string
s='abcdefghijklmnopqrstuvwxyz'
print(s[3:9])
print(s[:9])
print(s[3:])
print(s[:])
print(s[3:40]) # work
print(s[-100:40]) # work
print("20:5", s[20:5])
print("100:200", s[100:200])
print("-100:-200", s[-100:-200])

print('---------------------------------------------------------------------------------------------------------------')

s='durga' # make string like = Durga / durgA / DurgA

output = s[0].upper() + s[1:]
print(output)

output = s[:len(s)-1] + s[-1].upper()
print(output)

output=s[0].upper() + s[1:len(s)-1] + s[-1].upper()
print(output)

print('---------------------------------------------------------------------------------------------------------------')

s='durga' + 'soft'
print(s)

# s='durga' + 10 #TypeError: can only concatenate str (not "int") to str

print('---------------------------------------------------------------------------------------------------------------')

s='durga' * 3
print(s)

s= 3 * 'durga'
print(s)

# s= 'durga' * 'soft' # TypeError: can't multiply sequence by non-int of type 'str'
print('---------------------------------------------------------------------------------------------------------------')

print('#' * 10)
print('durgasoft')
print('#' * 10)