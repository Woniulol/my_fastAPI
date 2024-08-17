import socket


HOST: str = "127.0.0.1"
HOST_NAME: str = "Local Host"
PORTS: int = 8080

sock = socket.socket()
sock.bind((HOST, PORTS))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)

    print("From client: \n", data)
    # Response should Follow HTTP Response requirement
    response = f"HTTP/1.1 200 OK\r\nserver:{HOST_NAME}\r\n\r\nHello World"

    # Responds should be byte
    conn.send(response.encode())
    conn.close()
