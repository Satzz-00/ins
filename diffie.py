def power(a, b, p):
    return pow(a, b, p)

P, G = 23, 5
a, b = 4, 3

print("P:", P)
print("G:", G)
print("Alice's private key:", a)
print("Bob's private key:", b)

x = power(G, a, P)
y = power(G, b, P)

ka = power(y, a, P)
kb = power(x, b, P)

print("Secret key for Alice:", ka)
print("Secret key for Bob:", kb)
