message = input("Enter a message :-")
shift = 3

encrypted = ""

for char in message:

    if char.isalpha():

        new_char = chr(ord(char) + shift)

        encrypted += new_char
    else:

        encrypted += char

print("Encryptd message is:",encrypted)