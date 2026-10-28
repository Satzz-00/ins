from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import os

# Generate a random key of 32 bytes
key = os.urandom(32)  # Key length: 32 to 448 bits
cipher = Blowfish.new(key, Blowfish.MODE_CBC)

# Data to encrypt
data = b"This is a secret message."

# Pad the data to ensure it's a multiple of 8 bytes
padded_data = pad(data, Blowfish.block_size)

# Encrypt the data
iv = cipher.iv  # Initialization vector
encrypted_data = cipher.encrypt(padded_data)
print("Encrypted:", encrypted_data)
cipher_decrypt = Blowfish.new(key, Blowfish.MODE_CBC, iv)

# Decrypt the data
decrypted_data = unpad(cipher_decrypt.decrypt(encrypted_data), Blowfish.block_size)
print("Decrypted:", decrypted_data)