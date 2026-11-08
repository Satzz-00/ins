from math import gcd

text = input("Enter Plaintext: ").upper().replace(" ", "")
text = (text + "X" * 9)[:9]

K = []
print("Enter 9 Key Matrix Elements:")
for i in range(3):
    K.append([int(input()) for j in range(3)])

P = [[ord(text[i*3+j]) - 65 for j in range(3)] for i in range(3)]

det = (K[0][0]*(K[1][1]*K[2][2] - K[1][2]*K[2][1])
     - K[0][1]*(K[1][0]*K[2][2] - K[1][2]*K[2][0])
     + K[0][2]*(K[1][0]*K[2][1] - K[1][1]*K[2][0])) % 26

if gcd(det, 26) != 1:
    print("Wrong Key!")
else:
    C = [[sum(K[i][k]*P[k][j] for k in range(3)) % 26
          for j in range(3)] for i in range(3)]

    print("Cipher Matrix:")
    for row in C:
        print(row)

    cipher = ''.join(chr(x+65) for row in C for x in row)
    print("Ciphertext:", cipher)
