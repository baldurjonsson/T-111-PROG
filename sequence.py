# Farið yfir tölur frá 0 uppí n
# Útbúið lista af tölum og bætið einn við í hverri umferð.
# Talan sem bætist við er summa talnana sem á undan hafa komið.

n = int(input("Enter the length of the sequence: ")) # Do not change this line

numbers = []

for i in range(n):
    sum = 0
    for pn in numbers[-3:]:
        sum += pn
    if sum < 2:
        sum += 1
    numbers.append(sum)
    print(sum)
