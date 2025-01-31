# Blowfish Encryption/Decryption 

This Python script allows you to **encrypt** and **decrypt** messages using the **Blowfish** encryption algorithm. The script provides an option for the user to choose whether they want to **encrypt** or **decrypt** a message.

## Features:
- Encrypt a message using Blowfish with a user-provided key.
- Decrypt an encrypted message using the same key.
- Base64 encoding is used to represent the encrypted message for easy display.

**Example**:

**Encrypt-**
Do you want to encrypt or decrypt the message? 
(Enter 'encrypt' or 'decrypt'): encrypt

Enter the message to encrypt: Hello, Blowfish!

Enter the key (4-56 bytes): mysecretkey1234

Encrypted Message (Base64): k5U6IMrqD2O6OBaTkH8BLw==

**Decrypt**- 
Do you want to encrypt or decrypt the message? 
(Enter 'encrypt' or 'decrypt'): decrypt

Enter the encrypted message (Base64): k5U6IMrqD2O6OBaTkH8BLw==

Enter the key (4-56 bytes): mysecretkey1234

Decrypted Message: Hello, Blowfish!

