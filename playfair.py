def matrix(key):
    s = ""
    for c in (key + "ABCDEFGHIKLMNOPQRSTUVWXYZ").upper().replace("J", "I"):
        if c.isalpha() and c not in s:
            s += c
    return [s[i:i+5] for i in range(0, 25, 5)]


def pos(m, c):
    for i in range(5):
        for j in range(5):
            if m[i][j] == c:
                return i, j


def play(text, key, enc):
    m = matrix(key)
    text = text.upper().replace("J", "I")
    if enc:
        text = "".join(c for c in text if c.isalpha())
        s, i = "", 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i+1 < len(text) else "X"
            s += a + ("X" if a == b else b)
            i += 1 if a == b else 2
        text = s

    result, d = "", 1 if enc else -1
    for i in range(0, len(text), 2):
        r, c = pos(m, text[i])
        x, y = pos(m, text[i+1])

        if r == x:
            result += m[r][(c+d)%5] + m[x][(y+d)%5]
        elif c == y:
            result += m[(r+d)%5][c] + m[(x+d)%5][y]
        else:
            result += m[r][y] + m[x][c]
    return result


key = input("Enter Key: ")
text = input("Enter Plaintext: ")
cipher = play(text, key, True)
print("Encrypted Text:", cipher)
print("Decrypted Text:", play(cipher, key, False))
