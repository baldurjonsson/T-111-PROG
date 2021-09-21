even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0
while (n := int(input('Input an integer (0 to quit): '))) != 0:
    if n < 0:
        print('Ignoring this negative number!')
    elif n % 2 == 0:
        even_sum += n
        even_count += 1
    else:
        odd_sum += n
        odd_count += 1
print('Sum of even:', even_sum)
print('Sum of odd:', odd_sum)
print('Even count:', even_count)
print('Odd count:', odd_count)