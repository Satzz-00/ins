import socket, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

s = socket.create_connection(('localhost', 12345))
c = ctx.wrap_socket(s, server_hostname='localhost')

c.send(b"Hello Server! This is a secure message.")
print("Server:", c.recv(1024).decode())

c.close()