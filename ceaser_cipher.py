#function for encryption
def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char

    return encrypted_text

#function for decryption
def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char

    return decrypted_text

#Main program
def main():
    print("Welcome to the Caesar Cipher Program!")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Choose an option 1 or 2: ")

    message = input("Enter your message: ")
    shift_value = int(input("Enter shift value: "))

    if choice == '1':
        encrypted_message = encrypt(message, shift_value)
        print("Encrypted message:", encrypted_message)
    elif choice == '2':
        decrypted_message = decrypt(message, shift_value)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice! Please select either 1 or 2.")

if __name__ == "__main__":
    main()
