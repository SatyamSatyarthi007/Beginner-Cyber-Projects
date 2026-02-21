# Basic Network Scanner

Identifies active devices on a network and gathers basic network information.

## Features
- Scans network range for active hosts
- Displays IP addresses and MAC addresses
- Shows hostname information when available
- Fast concurrent scanning

## Requirements
- Python 3.x
- Root/Administrator privileges (for ARP scanning)

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
# Scan local network (auto-detect)
sudo python3 network_scanner.py

# Scan specific network range
sudo python3 network_scanner.py 192.168.1.0/24
```

Note: Root privileges are required for ARP scanning on Linux/Mac.
