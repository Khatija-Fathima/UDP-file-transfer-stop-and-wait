# UDP File Transfer using Stop-and-Wait ARQ

A Python-based implementation of the Stop-and-Wait Automatic Repeat Request (ARQ) protocol for reliable UDP file transfer. The project demonstrates packet retransmission, timeout handling, packet loss simulation, and performance analysis using Mininet.

## Features

- Reliable file transfer over UDP
- Stop-and-Wait ARQ implementation
- Packet loss simulation
- Timeout and retransmission handling
- Performance evaluation using Mininet
- CSV-based result analysis

## Technologies Used

- Python
- UDP Socket Programming
- Stop-and-Wait ARQ
- Mininet
- Linux
- Computer Networks

## Project Structure

```
client.py
server.py
result_table.csv
report.pdf
screenshots/
```

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/Khatija-Fathima/UDP-file-transfer-stop-and-wait.git
```

2. Run the server.

```bash
python server.py
```

3. Run the client.

```bash
python client.py
```

## Results

Performance metrics are available in:

- result_table.csv
- report.pdf

## Screenshots

Screenshots of the Mininet topology and execution are included in the `screenshots` folder.

## Learning Outcomes

- Reliable data transfer protocols
- UDP socket programming
- Computer networking concepts
- Network emulation using Mininet
- Performance analysis
