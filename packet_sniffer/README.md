# Simple Packet Sniffer

A basic packet sniffer that captures and analyzes network packets to demonstrate how data flows across a network.

## Features
- Captures network packets in real-time
- Displays packet information (protocol, source, destination)
- Analyzes TCP, UDP, and ICMP packets

## Requirements
- Python 3.x
- Root/Administrator privileges (required for raw socket access)

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
sudo python3 packet_sniffer.py
```

Note: On Linux, you need root privileges. On Windows, run as Administrator.
