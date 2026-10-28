import socket, ssl

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain('cert.pem', 'key.pem')

c, _ = s.accept()
c = ctx.wrap_socket(c, server_side=True)

msg = c.recv(1024).decode()
print("Client:", msg)

c.send(b"Hello Client! Secure message received.")
c.close()
s.close()