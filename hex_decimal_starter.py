def remainder_to_hex(remainder):
    if remainder < 10:
        return str(remainder)
    else:
        # a is 97 in ascii and a in hex is 10 so we do 87 + 10 for a and so on
        chr_code = 87 + remainder
        return chr(chr_code)


def decimal_to_hex_str(dec_int):
    hex_str = ''
    result = dec_int
    while result > 0:
        remainder = result % 16
        result = result // 16
        # prepend the remainder in hex to the string
        hex_str = remainder_to_hex(remainder) + hex_str
    return hex_str


def hex_str_to_decimal(hex_str):
    dec_int = 0
    seat = len(hex_str) - 1
    for c in hex_str:
        # for the last seat we want seat * 16 to become 1
        if seat == 0:
            seat = 1 / 16
        if c.isnumeric():
            dec_int += int(c) * int(seat * 16)
        seat -= 1
    return dec_int


def display_menu():
    print('d. Decimal to hex')
    print('h. Hex to decimal')
    print('x. Exit')
    print()


def get_option():
    return input('Enter option: ')


def main():
    running = True
    while running:
        display_menu()
        option = get_option()
        if option == 'd':
            dec_int = int(input('Decimal number: '))
            hex_str = decimal_to_hex_str(dec_int)
            print('The hex is', hex_str, '\n')
        elif option == 'h':
            hex_str = input('Hex number: ')
            dec_int = hex_str_to_decimal(hex_str)
            print('The decimal is', dec_int, '\n')
            pass
        elif option == 'x':
            running = False
        else:
            print('Invalid option!\n')


# Main program starts here
if __name__ == "__main__":
    main()
