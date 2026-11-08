text = input("Enter Plain Text: ").replace(" ", "")
key = input("Enter Key: ")
cols = len(key)
cipher = ""
for k in key:
    for i in range(int(k)-1, len(text), cols):
        cipher += text[i]
print("Encrypted Text:", cipher)
