# Encoder and Menu created by Harrison Lucas
# decode() by David Hochman

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


def decode(password):
    password = list(password)
    for i in range(0, len(password)):
        if password[i] == '0':  # changes numbers in passcode
            password[i] = 7
        elif password[i] == '1':
            password[i] = 8
        elif password[i] == '2':
            password[i] = 9
        elif password[i] == '3':
            password[i] = 0
        elif password[i] == '4':
            password[i] = 1
        elif password[i] == '5':
            password[i] = 2
        elif password[i] == '6':
            password[i] = 3
        elif password[i] == '7':
            password[i] = 4
        elif password[i] == '8':
            password[i] = 5
        elif password[i] == '9':
            password[i] = 6
        else:
            pass

    password = map(str, password)
    password = "".join(password)  # joins numbers in passcode

    return password


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
