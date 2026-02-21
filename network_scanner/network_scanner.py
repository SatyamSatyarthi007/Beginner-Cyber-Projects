#!/usr/bin/env python3
"""
Basic Network Scanner
Identifies active devices on a network and gathers basic information.
"""

from scapy.all import ARP, Ether, srp, conf
import socket
import sys

def get_local_network():
    """Auto-detect local network range."""
    try:
        # Get default interface
        iface = conf.route.route("0.0.0.0")[0]
        # Get IP and netmask
        for net, msk, gw, i, addr, metric in conf.route.routes:
            if i == iface and net != 0:
                # Convert to CIDR notation
                cidr = bin(msk).count('1')
                network = f"{socket.inet_ntoa(net)}/{cidr}"
                if not network.startswith('0.'):
                    return network
    except:
        pass
    return "192.168.1.0/24"  # Default fallback

def scan_network(target_ip):
    """Scan network for active hosts using ARP."""
    print(f"Scanning network: {target_ip}\n")
    
    # Create ARP packet
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    
    # Send packet and receive response
    result = srp(packet, timeout=3, verbose=0)[0]
    
    devices = []
    for sent, received in result:
        # Try to get hostname
        try:
            hostname = socket.gethostbyaddr(received.psrc)[0]
        except:
            hostname = "Unknown"
        
        devices.append({
            'ip': received.psrc,
            'mac': received.hwsrc,
            'hostname': hostname
        })
    
    return devices

def display_results(devices):
    """Display scan results in a formatted table."""
    if not devices:
        print("No devices found on the network.")
        return
    
    print(f"Found {len(devices)} device(s):\n")
    print(f"{'IP Address':<18} {'MAC Address':<20} {'Hostname'}")
    print("-" * 70)
    
    for device in devices:
        print(f"{device['ip']:<18} {device['mac']:<20} {device['hostname']}")

def main():
    """Main function to run network scanner."""
    try:
        # Get target network from command line or auto-detect
        if len(sys.argv) > 1:
            target = sys.argv[1]
        else:
            target = get_local_network()
            print(f"Auto-detected network: {target}")
        
        # Scan network
        devices = scan_network(target)
        
        # Display results
        display_results(devices)
        
    except PermissionError:
        print("Error: This script requires root/administrator privileges.")
        print("Run with: sudo python3 network_scanner.py")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nScan interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
