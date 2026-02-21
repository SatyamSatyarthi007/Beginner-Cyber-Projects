# Port Scanner Utility

This repository contains a compact Python program that surveys a host for open TCP ports. The script is intentionally straightforward so that its behavior is easy to understand, audit, and adapt to specific assessment needs.

## Key Capabilities

- Accepts a target either as a command-line argument (`python3 port_scanner.py <target>`) or through an interactive prompt when no argument is supplied.
- Resolves hostnames to IPv4 addresses before initiating the scan, providing reproducible output.
- Iterates across the complete TCP port range (1–65534) and reports each open port as it is discovered.
- Handles keyboard interrupts, DNS resolution failures, and socket errors gracefully, offering clear feedback before exiting.

## Operating the Scanner

```bash
python3 port_scanner.py               # prompts for a host or IP address
python3 port_scanner.py 192.168.1.10  # scans the specified address directly
```

After launch, the script announces the target and start time, then streams the results in real time. Press `Ctrl+C` to halt the scan whenever required.

## Practical Guidance

- The default one-second timeout (`socket.setdefaulttimeout(1)`) balances speed and reliability. Adjust the value if your environment demands faster probes or greater patience.
- Because the scan is sequential, large address spaces or high-latency links may require substantial time. Introducing concurrency or restricting the port range can shorten the run.
- Use this tool only on systems for which you have explicit authorization. Unauthorized scanning may violate policy or law.

## Paths for Enhancement

- Permit custom port ranges via flags such as `--ports 20-1024`.
- Introduce multithreading or asyncio to accelerate scanning on stable networks.
- Export findings to text or JSON for archival and reporting.
- Map well-known ports to service names to aid interpretation.

You are encouraged to extend the script in whatever manner best supports your operational workflows. Contributions and refinements are welcome.

