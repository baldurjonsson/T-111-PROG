import string


def main():
    file_name = input('Enter file name: ')
    file_obj = open_file(file_name)
    if file_obj:
        word_list = get_word_list(file_obj)
        print()
        print(word_list)
        print()
        word_list = remove_punctuation(word_list)
        print(word_list)
        print()
        word_class_dict = get_word_class_dict(word_list)
        print_word_dict(word_class_dict)
        print()
        longest_dict = get_longest_in_class_dict(word_class_dict)
        print_word_dict(longest_dict)


def get_word_list(file_obj):
    word_list = []
    for line in file_obj.readlines():
        word_list += line.split()
    return word_list


def remove_punctuation(word_list):
    new_word_list = []
    for word in word_list:
        if not word in string.punctuation:
            new_word_list.append(word)
    return new_word_list


def get_word_class_dict(word_list):
    word_class_dict = {}
    for i in range(0, len(word_list), 2):
        word_class = word_list[i + 1][0]
        word = word_list[i]
        if word_class not in word_class_dict:
            word_class_dict[word_class] = set()
        word_class_dict[word_class].add(word)
    return word_class_dict


def get_longest_in_class_dict(word_dict):
    new_dict = {}
    for k in word_dict:
        length = 0
        new_dict[k] = set()
        for word in sorted(word_dict[k]):
            if len(word) > length:
                length = len(word)
                new_dict[k] = set([word])
    return new_dict


def print_word_dict(word_dict):
    for k in sorted(word_dict.keys()):
        print(f'{k}:')
        for word in sorted(word_dict[k]):
            print(word.rjust(20))


def open_file(file_name):
    try:
        return open(file_name, 'r')
    except FileNotFoundError:
        print(f'File {file_name} not found!')


if __name__ == '__main__':
    main()
