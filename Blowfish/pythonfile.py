from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import base64

# Function for Blowfish encryption
def encrypt_message(message, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)  # Using ECB mode
    padded_message = pad(message.encode(), Blowfish.block_size)  # Pad the message
    encrypted_message = cipher.encrypt(padded_message)  # Encrypt the message
    return base64.b64encode(encrypted_message).decode()  # Return base64 encoded for easy viewing

# Function for Blowfish decryption
def decrypt_message(encrypted_message, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)  # Using ECB mode
    encrypted_bytes = base64.b64decode(encrypted_message)  # Decode from base64
    decrypted_message = cipher.decrypt(encrypted_bytes)  # Decrypt the message
    return unpad(decrypted_message, Blowfish.block_size).decode()  # Remove padding and return the original message

# User input for operation type (encryption or decryption)
operation = input("Do you want to encrypt or decrypt the message? (Enter 'encrypt' or 'decrypt'): ").strip().lower()

if operation == 'encrypt':
    message = input("Enter the message to encrypt: ")
    key = input("Enter the key (4-56 bytes): ").encode()  # Convert the key to bytes
    encrypted_message = encrypt_message(message, key)
    print("Encrypted Message (Base64):", encrypted_message)

elif operation == 'decrypt':
    encrypted_message = input("Enter the encrypted message (Base64): ")
    key = input("Enter the key (4-56 bytes): ").encode()  # Convert the key to bytes
    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted Message:", decrypted_message)

else:
    print("Invalid operation! Please enter 'encrypt' or 'decrypt'.")
