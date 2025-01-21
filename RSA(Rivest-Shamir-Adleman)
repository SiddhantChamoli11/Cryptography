from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import binascii

# Function to generate RSA keys (public and private)
def generate_rsa_keys():
    key = RSA.generate(2048)  # 2048-bit key size is commonly used
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

# Function to encrypt a message
def encrypt_message(message, public_key):
    recipient_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(recipient_key)
    encrypted_message = cipher.encrypt(message.encode())
    return binascii.hexlify(encrypted_message)

# Function to decrypt a message
def decrypt_message(encrypted_message, private_key):
    private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(binascii.unhexlify(encrypted_message)).decode()
    return decrypted_message

# Generate RSA Keys
public_key, private_key = generate_rsa_keys()

# User input for the message
message = input("Enter the message to encrypt: ")

# Encrypt the message
encrypted_message = encrypt_message(message, public_key)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
