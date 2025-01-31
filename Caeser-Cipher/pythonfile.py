# Caesar Cipher encryption and decryption

# Function to encrypt the message
def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if character is a letter
            shift_amount = 65 if char.isupper() else 97  # ASCII for A=65 and a=97
            encrypted_message += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_message += char
    return encrypted_message

# Function to decrypt the message
def decrypt_message(message, shift):
    return encrypt_message(message, -shift)  # Decrypt by shifting backwards

# Take input from the user
message = input("Enter the message to encrypt/decrypt: ")
shift = int(input("Enter the shift value (integer): "))

# Encrypt the message
encrypted = encrypt_message(message, shift)
print("Encrypted Message:", encrypted)

# Decrypt the message
decrypted = decrypt_message(encrypted, shift)
print("Decrypted Message:", decrypted)
