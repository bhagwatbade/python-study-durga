print('--------------------------------------------')

print('durga'  * 3)

print('--------------------------------------------')

print(2 * 'durga')

print('--------------------------------------------')

# print('durga' * 2.5) # TypeError: can't multiply sequence by non-int of type 'float'

print('--------------------------------------------')

# print('durga' * 'soft') # TypeError: can't multiply sequence by non-int of type 'str'

print('--------------------------------------------')

# print('durga' * '3') # TypeError: can't multiply sequence by non-int of type 'str'

print('durga' * int('3'))

print('--------------------------------------------')

print('durga' * True) # durga : internally True equal to 1
print('durga' * False) # (empty string):  internally False equal to 0

print('--------------------------------------------')
