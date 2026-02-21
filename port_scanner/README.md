# 🔎 Port Scanner Utility

> A compact and transparent Python script that surveys a host for open TCP ports.  
> Designed to be simple, auditable, and easy to adapt for educational or authorized security assessments.

---

## 📌 Overview

The **Port Scanner Utility** scans a target system to identify open TCP ports across the full range (1–65534).

Its intentionally straightforward design makes it ideal for:

- 🎓 Learning how TCP port scanning works  
- 🔐 Practicing authorized security assessments  
- 🧪 Testing lab environments  
- 🛠️ Understanding socket programming basics  

---

## ✨ Key Capabilities

- 🖥️ Accepts a target:
  - As a command-line argument  
  - Or via interactive prompt  
- 🌍 Resolves hostnames to IPv4 addresses before scanning  
- 🔁 Iterates across the full TCP port range (1–65534)  
- 📡 Reports open ports in real time  
- 🛑 Gracefully handles:
  - `Ctrl+C` interruptions  
  - DNS resolution failures  
  - Socket errors  

---

## 🚀 Operating the Scanner

### ▶ Interactive Mode

```bash
python3 port_scanner.py
