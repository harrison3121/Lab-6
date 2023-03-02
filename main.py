# Encoder and Menu created by Harrison Lucas


def encode(password):
    num1 = ''
    for i in password:
        if int(i) <= 6:
            num1 += str(int(i) + 3)

        elif int(i) == 7:
            num1 += '0'
        elif int(i) == 8:
            num1 += '1'
        elif int(i) == 9:
            num1 += '2'
    return num1


def menu():
    end_menu = 0
    epassword = None
    password = None

    while end_menu == 0:

        # Menu loop
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit ')
        print()
        print()
        operation = int(input('Please enter an option: '))

        if operation == 1:
            password = input('Please enter your password to encode: ')
            epassword = encode(password)
            print('Your password has been encoded and stored!')
            print()
            print()

        if operation == 2:
            password = decode(epassword)
            print(f'Your encoded password is {epassword}, and the original password is {password}.')
            print()
            print()

        if operation == 3:
            end_menu = 1


if __name__ == '__main__':
    menu()
