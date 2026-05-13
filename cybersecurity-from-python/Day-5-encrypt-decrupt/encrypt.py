import base64

def encrypt_text(text):
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


def decrypt_text(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode("utf-8"))
    return decoded_bytes.decode("utf-8")


while True:

    print("\n===== ENCRYPTION TOOL =====")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        text = input("Enter text to encrypt: ")

        encrypted = encrypt_text(text)

        print("\nEncrypted Text:")
        print(encrypted)

        with open("encrypted.txt", "w") as file:
            file.write(encrypted)

        print("\nEncrypted text saved in encrypted.txt")

    elif choice == "2":

        encrypted_text = input("Enter text to decrypt: ")

        try:
            decrypted = decrypt_text(encrypted_text)

            print("\nDecrypted Text:")
            print(decrypted)

        except:
            print("\nInvalid encrypted text!")

    elif choice == "3":

        print("\nExiting Program...")
        break

    else:
        print("\nInvalid Choice!")