import hashlib

text=input("Enter text: ")

hash=hashlib.sha256(text.encode('utf-8')).hexdigest()

print("SGA-256 Hash: ", hash)