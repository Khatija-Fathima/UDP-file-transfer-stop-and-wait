import socket

HOST = "10.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("Server started...")
print(f"Listening on {HOST}:{PORT}")

received = set()
duplicates = 0

while True:
    data, addr = server.recvfrom(1024)

    msg = data.decode()
    seq, text = msg.split("|", 1)

    if seq in received:
        duplicates += 1
        print(f"Duplicate Packet {seq}")
    else:
        received.add(seq)
        print(f"Received Packet {seq}: {text}")

    ack = f"ACK|{seq}"
    server.sendto(ack.encode(), addr)

    if len(received) == 10:
        print("\n===== SERVER STATISTICS =====")
        print(f"TOTAL_UNIQUE_MESSAGES_RECEIVED={len(received)}")
        print(f"TOTAL_DUPLICATES_DETECTED={duplicates}")
        print("STATUS=SUCCESS")
        break

server.close()
