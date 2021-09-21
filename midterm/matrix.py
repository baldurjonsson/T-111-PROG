size = int(input('Input matrix size: '))

# Tvívídd lúppa, förum eftir x ásnum y oft.
for y in range(0, size):
    for x in range(0, size):
        # fyrsta keyrsla: x = y = 0, prentar 1
        # fyrsta keyrsla í annari röð: x = 0, y = 1, prentar 1 + size
        print(x + y * size + 1, end=' ')
    print()

