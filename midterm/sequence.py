length = int(input('Length of sequence: '))
step = int(input('Step size: '))

start = step
finish = step * length + 1

for s in range(start, finish, step):
    print(s)