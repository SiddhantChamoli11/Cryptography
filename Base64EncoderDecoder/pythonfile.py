import base64

def encode_base64(text):
    """Encodes a given text to Base64."""
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_base64(encoded_text):
    """Decodes a Base64 encoded text."""
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

if __name__ == "__main__":
    choice = input("Do you want to encode or decode? (e/d): ").strip().lower()

    if choice == 'e':
        text = input("Enter text to encode: ")
        encoded_text = encode_base64(text)
        print(f"Encoded: {encoded_text}")
    elif choice == 'd':
        encoded_text = input("Enter text to decode: ")
        try:
            decoded_text = decode_base64(encoded_text)
            print(f"Decoded: {decoded_text}")
        except Exception as e:
            print("Invalid Base64 encoded text.")
    else:
        print("Invalid choice. Please enter 'e' to encode or 'd' to decode.")
