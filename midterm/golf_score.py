par = int(input('Par for hole: '))
score = int(input('Score on hole: '))

diff = score - par

if diff >= 3:
    print('Bad score')
elif diff == 2:
    print('Double bogey')
elif diff == 1:
    print('Bogey')
elif diff == 0:
    print('Par')
elif diff == -1:
    print('Birdie')
elif diff == -2:
    print('Eagle')
else:
    print('Unbelievable!')