from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

message = b"Secure document transmission data."
signature = private_key.sign(message, hashes.SHA256())

print("Signature generated. Length:", len(signature))

try:
    public_key.verify(signature, message, hashes.SHA256())
    print("Verification SUCCESS: Signature is valid.")
except Exception as e:
    print("Verification FAILED:", e)