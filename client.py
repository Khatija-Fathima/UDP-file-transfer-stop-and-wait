import socket
import time

SERVER_IP = "10.0.0.1"
PORT = 5000

TIMEOUT = 1.0
LOSS_PERCENT = 10

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(TIMEOUT)

total_packets_sent = 0
retransmissions = 0

start_time = time.time()

for seq in range(1, 11):

    message = f"{seq}|Message {seq} from h2"

    while True:

        try:
            total_packets_sent += 1

            print(f"Sending Packet {seq}")

            client.sendto(message.encode(), (SERVER_IP, PORT))

            ack, _ = client.recvfrom(1024)

            ack_msg = ack.decode()

            if ack_msg == f"ACK|{seq}":
                print(f"Received {ack_msg}")
                break

        except socket.timeout:

            retransmissions += 1

            print(f"Timeout Packet {seq}")
            print("Retransmitting...")

end_time = time.time()

transfer_time = round(end_time - start_time, 4)

print("\n===== CLIENT STATISTICS =====")
print("TOTAL_MESSAGES=10")
print(f"LOSS_PERCENT={LOSS_PERCENT}")
print(f"TIMEOUT={TIMEOUT}")
print(f"TOTAL_PACKETS_SENT={total_packets_sent}")
print(f"TOTAL_RETRANSMISSIONS={retransmissions}")
print(f"TRANSFER_TIME_SECONDS={transfer_time}")
print("STATUS=SUCCESS")

client.close()
