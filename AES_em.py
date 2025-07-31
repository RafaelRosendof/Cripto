import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import argparse


ITERATION_COUNT = 19052004
AES_KEY_SIZE_BYTES = 32  # 256 bits
SALT_SIZE_BYTES = 16
IV_SIZE_BYTES = 12

def encrypt(plaintext: str, password: str) -> str:
    """Encrypts data in a way that is compatible with the Go/Java versions."""
    salt = os.urandom(SALT_SIZE_BYTES)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=AES_KEY_SIZE_BYTES,
        salt=salt,
        iterations=ITERATION_COUNT,
        backend=default_backend()
    )
    key = kdf.derive(password.encode('utf-8'))
    
    iv = os.urandom(IV_SIZE_BYTES)
    
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(iv, plaintext.encode('utf-8'), None)
    
    payload = salt + iv + ciphertext
    
    return base64.b64encode(payload).decode('utf-8')

def decrypt(base64_payload: str, password: str) -> str:

    decoded_payload = base64.b64decode(base64_payload.encode('utf-8'))
    
    salt = decoded_payload[:SALT_SIZE_BYTES]
    iv = decoded_payload[SALT_SIZE_BYTES : SALT_SIZE_BYTES + IV_SIZE_BYTES]
    ciphertext_with_tag = decoded_payload[SALT_SIZE_BYTES + IV_SIZE_BYTES:]
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=AES_KEY_SIZE_BYTES,
        salt=salt,
        iterations=ITERATION_COUNT,
        backend=default_backend()
    )
    key = kdf.derive(password.encode('utf-8'))
    
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(iv, ciphertext_with_tag, None)
    
    return plaintext.decode('utf-8')

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt data.")
    parser.add_argument('-E', '--encrypt', action='store_true', help="Encrypt the input data.")
    parser.add_argument('-D', '--decrypt', action='store_true', help="Decrypt the input data.")
    parser.add_argument('-Data', type=str, help="The data to process (plaintext for encryption, base64 for decryption).")
    parser.add_argument('-Key', type=str, help="The password for the operation.")

    args = parser.parse_args()

    try:
        if args.encrypt:
            print("Encrypting data...")
            encrypted_data = encrypt(args.Data, args.Key)
            print("\n--- Encrypted Payload (save this) ---")
            print(encrypted_data)

        elif args.decrypt:
            print("Decrypting data...")
            decrypted_data = decrypt(args.Data, args.Key)
            print("\n--- Decrypted Data ---")
            print(decrypted_data)
            
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()