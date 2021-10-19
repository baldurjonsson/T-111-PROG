def main():
    filename1 = input("Enter the path to the first file: ")
    filename2 = input("Enter the path to the second file: ")
    word_set1 = file_to_word_set(filename1)
    word_set2 = file_to_word_set(filename2)

    common = word_set1.intersection(word_set2)
    unique = word_set1.symmetric_difference(word_set2)
    first_file_only = word_set1.difference(word_set2)

    print(f'The two files have {len(common)} words in common.')
    print_word_set(common)

    print(f'There are {len(unique)} words that are only in either file but not both.')
    print_word_set(unique)

    print(f'There are {len(first_file_only)} words that only appear in the first file.')
    print_word_set(first_file_only)


def print_word_set(word_set):
    print('These words are as follows:', end=' ')
    word_list = sorted(word_set)
    if len(word_list) > 0:
        # Prentum allt nema síðasta orðið með kommu á milli og prentum svo síðasta orðið.
        print(', '.join(word_list[0:-1]), end='')
        print(f', and {word_list[-1]}.')


def file_to_word_set(filename):
    word_set = set()
    try:
        with open(filename, 'r') as file:
            for line in file.readlines():
                for word in line.split():
                    word_set.add(word)
    except FileNotFoundError:
        pass
    return word_set


if __name__ == "__main__":
    main()