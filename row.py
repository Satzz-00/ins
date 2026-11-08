text = input("Enter plaintext: ").replace(" ", "").upper()
key = input("Enter key: ")
key = [int(x) for x in key]
cipher = ""
n = len(key)
for k in sorted(key):
    col = key.index(k)
    for i in range(col, len(text), n):
        cipher += text[i]
print("Encrypted:", cipher)
