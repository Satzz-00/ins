text = input("Enter plaintext: ").replace(" ", "")
depth = int(input("Enter depth: "))
rails = [""] * depth
row = 0
direction = 1
for ch in text:
    rails[row] += ch
    if row == 0:
        direction = 1
    elif row == depth - 1:
        direction = -1
    row += direction
cipher = "".join(rails)
print("Encrypted:", cipher)
