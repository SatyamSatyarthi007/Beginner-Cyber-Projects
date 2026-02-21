#!/usr/bin/env python3
"""
Simple Packet Sniffer
Captures and analyzes network packets to demonstrate data flow across networks.
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP
import sys

def packet_callback(packet):
    """Process and display captured packet information."""
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        # Determine protocol type
        if TCP in packet:
            proto_name = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            print(f"[{proto_name}] {ip_src}:{sport} -> {ip_dst}:{dport}")
        elif UDP in packet:
            proto_name = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            print(f"[{proto_name}] {ip_src}:{sport} -> {ip_dst}:{dport}")
        elif ICMP in packet:
            proto_name = "ICMP"
            print(f"[{proto_name}] {ip_src} -> {ip_dst}")
        else:
            print(f"[Protocol {protocol}] {ip_src} -> {ip_dst}")

def main():
    """Start packet sniffing."""
    print("Starting packet sniffer...")
    print("Press Ctrl+C to stop\n")
    
    try:
        # Sniff packets on all interfaces
        sniff(prn=packet_callback, store=False)
    except PermissionError:
        print("Error: This script requires root/administrator privileges.")
        print("Run with: sudo python3 packet_sniffer.py")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nStopping packet sniffer...")
        sys.exit(0)

if __name__ == "__main__":
    main()
