def alphabetically_first(string1, string2):
    if string1 < string2:
        return string1
    else:
        return string2


def is_substring(substring, string):
    return substring in string


def extract_first_number_from_string(string):
    words = string.split()
    for word in words:
        if word.isdigit():
            return int(word)
    return -1


def sum_of_range(start, end, step):
    sum = 0
    for n in range(start, end + 1, step):
        sum += n
    return sum


def sum_of_factors(n):
    sum = 0
    for f in range(1, n // 2 + 1):
        if n % f == 0:
            sum += f
    return sum


def decide(n):
    sum = sum_of_factors(n)
    if n > sum:
        return f'{n} is deficient.'
    elif n == sum:
        return f'{n} is a perfect number.'
    else:
        return f'{n} is abundant.'


print(decide(12))