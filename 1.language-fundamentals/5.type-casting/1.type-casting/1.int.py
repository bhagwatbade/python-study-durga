print('-------------------------------------------- float ------------------------------------------------------------------')
print(int(123.987))

print('-------------------------------------------- complex ------------------------------------------------------------------')
# print(int(10.5j)) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

print('-------------------------------------------- bool ------------------------------------------------------------------')
print(int(True))
print(int(False))

print('-------------------------------------------- str ------------------------------------------------------------------')
print(int("10"))
# print(int("10.5") # ValueError: invalid literal for int() with base 10: '10.5'
#print(int("ten")) # ValueError: invalid literal for int() with base 10: 'ten'
# int("OB1111") # ValueError: invalid literal for int() with base 10: 'OB1111'

