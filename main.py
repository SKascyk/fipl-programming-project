from cipher import encrypt, decrypt

def main():
    while True:
        print('\n--- Menu ---')
        print('1. Text Encryption')
        print('2. Text Decryption')
        print('3. Exit')
        choice = input('> ').strip()

        if choice == '1':
            text = input('Enter text: ')
            key = input('Enter key: ')
            if not key:
                print('Error: key must not be empty')
                continue
            try:
                result = encrypt(text, key)
                print(f'Encrypted text (hex): {result}')
            except Exception as error:
                print(f'Encryption error: {error}')

        elif choice == '2':
            hex_cipher = input('Enter encrypted text (hex): ')
            key = input('Enter key: ')
            if not key:
                print('Error: key must not be empty')
                continue
            try:
                result = decrypt(hex_cipher, key)
                print(f'Decrypted text: {result}')
            except Exception as error:
                print(f'Decryption error: {error}')
                print('Most likely:\nWrong key\nWrong text')

        elif choice == '3':
            print('Exiting...')
            break
        
        else:
            print('Invalid input. Please try again.')


main()
