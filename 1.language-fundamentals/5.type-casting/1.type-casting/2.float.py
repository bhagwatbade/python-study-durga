
print('-------------------------------------------- int ------------------------------------------------------------------')
print(float(10))
print(float(0B1111))

print('-------------------------------------------- complex ------------------------------------------------------------------')
# print(float(10.5j)) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

print('-------------------------------------------- bool -------------------------------------------------------------------')
print(float(True))
print(float(False))

print('-------------------------------------------- str -----------------------------------------------------------------')
print(float("10"))
print(float("10.5"))
# print(float("ten")) # ValueError: invalid literal for int() with base 10: 'ten'
# print(float("OB1111")) # ValueError: invalid literal for int() with base 10: 'OB1111'
# print(float("durga")) # ValueError: could not convert string to float: 'durga'


