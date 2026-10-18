a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))
c = int(input('Enter Third Number: '))

min = a if a < b and a < c else b if b < c else c
#min = a if (a < b and a < c) else (b if (b < c) else c)

print('Minimum Value: ', min)

print('--------------------------------------------')

#min = a if a < b < c else b if b < c else c #  Incorrect answer for input : 5, 35, 30 (a < b < c : not work)
#print('Minimum Value: ', min)


