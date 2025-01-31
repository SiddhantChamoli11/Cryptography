# RSA Encryption and Decryption

This Python script demonstrates the use of the **RSA** encryption algorithm to **encrypt** and **decrypt** messages. The script generates RSA public and private keys, and uses the **PKCS1_OAEP** cipher for secure encryption and decryption.

## Features:
- **Generate RSA Keys**: The script generates a **2048-bit RSA public and private key pair**.
- **Encrypt a Message**: The message is encrypted using the **RSA public key**.
- **Decrypt a Message**: The encrypted message is decrypted using the corresponding **RSA private key**.
- The encrypted message is displayed as a **hexadecimal string** for easy representation.

## Example:
### Encrypt:
```
Enter the message to encrypt: Hello, RSA Encryption!
Encrypted Message: b'30819f...d512d'
Decrypted Message: Hello, RSA Encryption!
```

### Notes:
- The encrypted message is represented in **hexadecimal format** for easy viewing.
- RSA encryption works with the **public key**, while decryption works with the **private key**.
- The script uses **2048-bit RSA keys**, which provide a strong level of security for most applications.
