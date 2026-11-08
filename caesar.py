def caesar(text, shift): 
    result = ""
    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch.upper()) - 65 + shift) % 26 + 65) 
        else:
            result += ch
    return result
text = input("Enter text: ")
shift = int(input("Enter shift: ")) 
encrypted = caesar(text, shift) 
print("Encrypted:", encrypted) 
decrypted = caesar(encrypted, -shift) 
print("Decrypted:", decrypted)
