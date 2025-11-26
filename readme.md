<p align="center">
  <img src="1000004178-removebg-preview.png " width="200" height="165" alt="The Skull Logo">
</p>

<h1 align="center">🦅 The-Skull Port Forwarding Engine</h1>

<p align="center">
  A high-performance TCP/UDP port forwarding engine featuring Twin Mode, Multi-Port routing, Reverse Multi-Port, and an Interactive Wizard.
  <br>
  <b>Cross‑Platform • Python Powered • Fully Modular • Developer Friendly</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20Termux%20%7C%20RaspberryPi-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Protocol-TCP%20%7C%20UDP-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Wizard-YES-purple?style=for-the-badge">
  <img src="https://img.shields.io/github/license/yourname/The-Skull?style=for-the-badge">
</p>

---

# 🔥 Overview

**The-Skull** is a next‑generation port forwarding engine written in Python.  
It supports:

- ✔ **TCP Forwarding**
- ✔ **UDP Forwarding**
- ✔ **Twin Mode (two-way dual‑pipe forwarder)**
- ✔ **Multi-Port Forwarding**
- ✔ **Reverse Multi-Port Routing**
- ✔ **Interactive Wizard Menu**
- ✔ **Full CLI Flags Support**
- ✔ **Cross‑Platform Execution**

Perfect for networking tools, C2 redirectors, debugging, development, and penetration testing labs.

---

# 📦 Features

### 🟦 **Protocol Support**
- `--tcp` or `-g`
- `--udp` or `-k`  
(Default: **TCP**)

### 🟪 **Forwarder Modes**
| Mode | Name | Description |
|------|------|-------------|
| **0** | Classic | Standard TCP/UDP port forwarder |
| **1** | Twin Mode | Two-way mirrored port forwarding |
| **2** | Multi-Port | Multiple LPORT → one RPORT |
| **3** | Reverse Multi-Port | Multiple RPORT → one LPORT |

---

# 🧙 Wizard Mode (`--wizard` / `-w`)

Wizard offers a terminal UI to configure everything interactively.

## **Wizard Example**
--- Forwarder Wizard ---
[0] TCP
[1] UDP
[99] Exit
Select protocol: 0

[0] Classic
[1] Twin Mode
[2] Multi-Port
[3] Reverse Multi-Port
[99] Exit
MOD: 1

Wizard Commands:
set:lhost <ip>
set:lport <p1> <p2> ...
set:rhost <ip>
set:rport <p1> <p2> ...
set:R <lhost> <rhost> <lport> <rport>
show
start
exit



---

# 📥 Installation

### 👉 **Clone the repository**
```bash
git clone https://github.com/yourname/The-Skull.git
cd The-Skull
👉 Install Python dependencies

pip install -r requirements.txt
This project uses only standard Python libraries, but requirements.txt is included for future module expansion.

▶️ Usage Examples
🔹 Classic TCP Forward

python skull.py --tcp -f 127.0.0.1 -d 7777 -i 192.168.0.32 -r 446
🔹 Classic UDP Forward


python skull.py --udp -f 0.0.0.0 -d 9000 -i 192.168.1.10 -r 9000
🔹 Twin Mode Forwarding

a
python skull.py --tcp --mod 1 -f 127.0.0.1 -d 5555 -i 10.0.0.20 -r 6666
🔹 Multi-LPORT → Single RPORT


python skull.py --tcp --mod 2 -f 0.0.0.0 -d 4444 5555 6666 -i 192.168.0.10 -r 7777
🔹 Reverse Multi-RPORT → Single LPORT


python skull.py --tcp --mod 3 -f 127.0.0.1 -d 8000 -i 192.168.0.50 -r 9001 9002 9003
🔹 Wizard Mode

python skull.py --wizard
📂 Project Structure

The-Skull/
│-The-skull.py
├── src/
│   ├
│   └── ss.log
│
├── cookie/
│   ├
│   └── logo.png
├── requirements.txt
└── README.md

🛠 Developer Notes
✔ Modular Architecture
The forwarder engine is fully modular and can easily be expanded:

Add encryption layers

Add proxies

Add traffic inspection

Add SOCKS5/HTTP tunneling

Add UI (Tkinter / Web)

✔ Cross-Platform Safe
The script is compatible with:

Windows cmd / PowerShell

Linux bash / zsh

Termux

macOS

Raspberry Pi

✔ Stable Threading Engine
Handles:

Multiple clients

High throughput

Low latency

🪪 License
This project is licensed under the MIT License.
You are free to modify, distribute, use, and integrate it into your own tools.



MIT License

Copyright (c) 2025 <Your Name>

Permission is hereby granted, free of charge, to any person obtaining a copy
...
👤 Developer
Author: Your Name
GitHub: https://github.com/hvns1414
Email: immi@boxfi.uk
If you find The-Skull useful, consider giving it a GitHub Star ⭐.

text

Made with ❤️ and Python by YourName
yaml



