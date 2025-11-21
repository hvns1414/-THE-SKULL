import socket
import threading
import sys
import time
import os
from optparse import OptionParser
from colorama import Fore, Style, init
print(Fore.RED+"""


⠀⠀⠀⠀⠀⠀⠀⢀⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⠀⠀⠀⠀⢀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣧⡀⠀⠀⣼⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⢀⣴⡶⠀⠀⠀⠀⠀
⠀⢸⣿⣧⠀⣰⡏⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣈⣧⠈⠻⣿⣦⣀⣀⠀⠀⠀⣸⣿⣿⣿⣆⠀⠀⠀⣴⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠘⡏⢿⣧⣿⠀⢀⣿⠁⠀⢀⣾⡇⠀⠀⠀⣀⠤⠖⠂⠉⠉⠀⠀⠀⠀⠀⠸⡏⣀⣀⣭⣷⣄⠉⠉⠒⢻⣿⣿⣿⣿⡆⢀⣾⣿⣿⡏⠀⠀⠀⠀⠀⠀
⠀⣤⣇⠘⣿⠇⠀⢸⡇⠀⢠⣾⣿⣀⡤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⢻⣽⣿⣿⣿⣧⡀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⢸⣿⣿⡀⢻⡇⢠⡿⠀⣰⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣷⡀⢸⣿⣿⣿⣿⠏⠙⢿⣿⣿⣇⠀⠀⠀⠀⢀⣶
⢸⣿⣿⣧⣈⣧⡿⠁⢠⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣧⠈⣿⣿⣿⡏⠀⠀⣼⢹⣿⣿⠀⠀⠀⢀⣾⣿
⣿⡟⢿⣿⣿⣿⠁⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠳⡀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⡆⢹⣿⣿⠁⠀⢀⢛⣼⣿⣿⠳⣄⢀⣾⣿⣿
⢻⡇⠀⢻⣿⣇⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠘⢦⣀⡀⠀⠀⠈⠻⣿⣿⣿⣇⠀⣿⡟⠀⠀⡞⣿⣿⣿⣿⠀⠘⣿⡗⣿⣿
⠈⣧⠀⠈⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠈⠙⡓⠶⣤⣄⡈⠻⣿⣿⣧⣸⡇⡆⠀⢳⣿⣿⣿⡇⠀⣸⣏⠁⣿⣿
⠀⠹⡆⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠉⠳⢦⡈⠛⠷⣿⣿⣿⣿⣅⠁⠀⣿⣿⣿⡟⠀⢰⣿⠃⠀⣼⣿
⠀⠀⢻⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⣄⣌⣲⣄⠸⣿⡿⣿⣿⣷⣴⣿⣿⠟⠀⠀⣿⡿⠀⠀⣸⡟
⠀⠀⠘⣿⡏⠀⠀⠀⢀⠀⠀⠀⠀⠀⠐⣿⣿⢿⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣷⣿⣧⠈⠻⢿⣿⣿⠋⠀⠀⢸⣿⠇⠀⣼⡿⣇
⠀⣀⡴⢋⣴⣿⣿⣿⣿⣿⡷⠿⣿⣿⣿⢣⣾⣿⣿⣿⣿⣷⣭⣙⠶⡄⠀⠀⢰⡇⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣧⠀⠘⠛⣿⣆⠀⠀⣿⡇⠀⢀⣿⠇⢸
⠀⢻⠀⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠈⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⡄⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣇⠀⠀⠈⢻⡆⢸⠃⠀⠀⣾⠏⠀⢸
⠀⠈⡇⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⡀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣾⡄⠀⠀⢿⡟⠀⣠⣼⣿⠇⠀⢼
⠀⠸⣅⢷⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⡇⠀⠀⢧⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⢠⣿⣿⣿⡿⣿⣿⠀⠀⡟
⠀⣀⡿⠈⢿⣿⣿⡇⢻⣿⡗⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣸⠁⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⠿⠋⣴⣿⣿⠀⢀⡟
⠀⡿⠁⠀⠼⠛⢹⣯⣸⣿⣷⡄⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⡿⠛⠁⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠞⠉⢿⡿⠿⠟⣻⡟⠁⢠⡾⠛⢩⣿⣰⡿⠀
⠸⡇⠀⠀⠀⠀⢸⠇⠿⠋⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⠁⠀⠀⣠⡴⢻⣿⣿⣶⣶⣶⣾⡿⠀⡖⢸⡇⠀⢠⡟⣠⡾⣋⣴⣴⠟⣽⣿⠃⠀
⠀⢷⠀⢀⡾⣤⣼⣶⡖⠶⣿⠃⠀⠀⠀⠀⠀⢲⣷⣶⡶⠶⠆⣀⣀⣠⣴⠟⡟⠀⠀⠻⣿⣿⣿⣿⣿⠁⢨⠃⣸⣿⣦⣿⣟⣩⣾⡿⠋⣡⣾⣿⠃⠀⠀
⠀⠀⠉⠉⠀⢰⠏⠈⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣏⣴⣾⣿⡟⠁⠀⠀⣸⡇⠀⠀⠀⢿⠻⠿⢫⠏⠀⠀⠀⣿⣿⣿⣿⣿⠿⠁⣶⣴⣿⣿⠇⠀⠀⠀
⠀⠀⠀⠀⢀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⣿⠏⣿⡇⠀⢀⣾⣿⠧⠀⠀⠀⢸⡄⣰⠟⠀⠀⠀⢠⣿⣿⣿⣯⣁⣠⣾⣿⣿⠟⠋⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠘⠋⢰⣿⣿⣶⡾⣿⣿⠇⠀⣠⠞⢉⠜⠁⡴⠀⢀⣴⡟⠉⠀⠉⠛⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣹⣶⡦⣴⢲⣴⢦⡤⣤⣤⣄⣤⣤⣤⣤⣤⣴⡿⠋⠙⢿⣯⣿⣿⠀⡰⠃⠀⠋⠀⡼⠁⠀⡞⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡏⣿⢰⡇⢰⠇⢸⡇⣸⣨⣇⣸⣏⣸⢇⣾⣿⣀⣠⠤⠤⠵⣫⠏⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣟⢿⢿⣿⣷⣿⣹⣇⣿⣸⣧⠥⠿⠴⠜⠋⠁⠀⠀⡴⠞⠁⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⢀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠛⠉⠉⠙⠉⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣴⣶⠾⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⣠⣾⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⢀⣀⡀⣀⡀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⠶⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢷⣂⣀⣀⣀⣍⣳⣶⣾⣿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠛⠻⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣷⣿⡆⣶⣶⣿⣿⣶⣿⣶⡀⣶⣶⣿⣷⣶⣶⣾⣶⣶⡆⠀⢰⣶⣶⣾⡧⣿⣶⣆⠀⢠⣶⣶⡆⣾⣶⣶⣿⣶⣿⣶⡀⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⣷⣦⣭⡅⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⠀⢸⣿⡏⠀⢸⣿⠀⠀⢸⣿⣷⣿⡇⣿⣿⣿⣆⣿⣿⣿⡇⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣟⣻⣿⡇⣿⣿⣉⣉⣸⣿⡟⣿⣿⣿⠀⢸⣿⣇⠀⢸⣿⣄⣀⣸⣿⣍⣉⡁⣿⣿⣿⣿⣿⢿⣿⡇⣿⣿⣉⣉⣸⣿⡟⣿⣿⣿⢠⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠟⠃⠻⠟⠛⠛⠛⠿⠇⠈⠛⠛⠀⠘⠿⠟⠀⠘⠛⠛⠿⠟⠛⠛⠛⠋⠿⠟⠘⠿⠋⠘⠛⠃⠻⠟⠛⠛⠛⠿⠇
""")
print(Fore.RESET)
#!/usr/bin/env python3
"""
forwarder_mods.py
Multi-mode TCP/UDP port forwarder with wizard and mod selection.

Usage examples:
  python forwarder_mods.py
  python forwarder_mods.py -k
  python forwarder_mods.py -w
  python forwarder_mods.py -m 2 -g
  python forwarder_mods.py -f 0.0.0.0 -d 9000 -i 10.0.0.5 -r 8080
"""

import socket
import threading
import time
import sys
import os
from optparse import OptionParser
from typing import List, Tuple
try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True)
except Exception:
    class _C:
        RED = GREEN = YELLOW = CYAN = BLUE = MAGENTA = RESET = ""
    Fore = _C()
    Style = _C()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
if not os.path.isdir(SRC_DIR):
    os.makedirs(SRC_DIR, exist_ok=True)
LOG_FILE = os.path.join(SRC_DIR, "ss.log")

def log(msg: str):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def tcp_relay(src_sock: socket.socket, dst_sock: socket.socket):
    try:
        while True:
            data = src_sock.recv(4096)
            if not data:
                break
            dst_sock.sendall(data)
    except Exception:
        pass
    finally:
        try:
            dst_sock.shutdown(socket.SHUT_WR)
        except Exception:
            pass

def start_single_tcp_forward(lhost: str, lport: int, rhost: str, rport: int):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        srv.bind((lhost, lport))
    except Exception as e:
        print(f"{Fore.RED}ERROR binding {lhost}:{lport}: {e}{Style.RESET_ALL}")
        log(f"ERROR binding {lhost}:{lport}: {e}")
        return
    srv.listen(200)
    print(f"{Fore.CYAN}[TCP] Listening {lhost}:{lport} -> {rhost}:{rport}{Style.RESET_ALL}")
    log(f"TCP Listening {lhost}:{lport} -> {rhost}:{rport}")

    def handle_client(client_sock, addr):
        print(f"{Fore.GREEN}[TCP] Conn from {addr}{Style.RESET_ALL}")
        log(f"TCP Conn {addr} -> {rhost}:{rport}")
        try:
            remote = socket.create_connection((rhost, rport), timeout=10)
        except Exception as e:
            print(f"{Fore.RED}[TCP] Remote connect failed: {e}{Style.RESET_ALL}")
            log(f"TCP remote connect failed: {e}")
            client_sock.close()
            return

        t1 = threading.Thread(target=tcp_relay, args=(client_sock, remote), daemon=True)
        t2 = threading.Thread(target=tcp_relay, args=(remote, client_sock), daemon=True)
        t1.start(); t2.start()
        t1.join(); t2.join()
        try: client_sock.close()
        except: pass
        try: remote.close()
        except: pass
        print(f"{Fore.YELLOW}[TCP] Closed {addr}{Style.RESET_ALL}")
        log(f"TCP closed {addr}")

    try:
        while True:
            client, addr = srv.accept()
            threading.Thread(target=handle_client, args=(client, addr), daemon=True).start()
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        try: srv.close()
        except: pass

def start_single_udp_forward(lhost: str, lport: int, rhost: str, rport: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind((lhost, lport))
    except Exception as e:
        print(f"{Fore.RED}ERROR binding UDP {lhost}:{lport}: {e}{Style.RESET_ALL}")
        log(f"UDP bind error {lhost}:{lport}: {e}")
        return

    print(f"{Fore.CYAN}[UDP] Listening {lhost}:{lport} -> {rhost}:{rport}{Style.RESET_ALL}")
    log(f"UDP Listening {lhost}:{lport} -> {rhost}:{rport}")

    try:
        while True:
            data, addr = sock.recvfrom(65535)
            try:
                sock.sendto(data, (rhost, rport))
                log(f"UDP pkt from {addr} forwarded to {(rhost,rport)} size={len(data)}")
            except Exception as e:
                log(f"UDP forward error: {e}")
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        try: sock.close()
        except: pass

class Config:
    def __init__(self):
        self.mode = "tcp"
        self.mod = 0
        self.lhost = "127.0.0.1"
        self.lport = 7777
        self.rhost = "192.168.0.32"
        self.rport = 446
        self.twin: List[Tuple[str,int,str,int]] = []
        self.lports: List[int] = []
        self.rports: List[int] = []

cfg = Config()

def run_classic():
    if cfg.mode == "tcp":
        start_single_tcp_forward(cfg.lhost, cfg.lport, cfg.rhost, cfg.rport)
    else:
        start_single_udp_forward(cfg.lhost, cfg.lport, cfg.rhost, cfg.rport)

def run_twin():
    threads = []
    for (lh, lp, rh, rp) in cfg.twin:
        if cfg.mode == "tcp":
            t = threading.Thread(target=start_single_tcp_forward, args=(lh, lp, rh, rp), daemon=True)
        else:
            t = threading.Thread(target=start_single_udp_forward, args=(lh, lp, rh, rp), daemon=True)
        t.start()
        threads.append(t)
        log(f"Started twin forward {lh}:{lp} -> {rh}:{rp}")
        print(f"{Fore.MAGENTA}[TWIN]{Style.RESET_ALL} {lh}:{lp} -> {rh}:{rp}")
    for t in threads:
        t.join()

def run_ports_forwarding():
    threads = []
    for lp in cfg.lports:
        if cfg.mode == "tcp":
            t = threading.Thread(target=start_single_tcp_forward, args=(cfg.lhost, lp, cfg.rhost, cfg.rport), daemon=True)
        else:
            t = threading.Thread(target=start_single_udp_forward, args=(cfg.lhost, lp, cfg.rhost, cfg.rport), daemon=True)
        t.start()
        threads.append(t)
        log(f"Started ports forward {cfg.lhost}:{lp} -> {cfg.rhost}:{cfg.rport}")
        print(f"{Fore.MAGENTA}[PORTS]{Style.RESET_ALL} {cfg.lhost}:{lp} -> {cfg.rhost}:{cfg.rport}")
    for t in threads:
        t.join()

def run_reverse_ports_forwarding():
    threads = []
    base_local = cfg.lport
    for idx, rp in enumerate(cfg.rports):
        lp = base_local + idx
        if cfg.mode == "tcp":
            t = threading.Thread(target=start_single_tcp_forward, args=(cfg.lhost, lp, cfg.rhost, rp), daemon=True)
        else:
            t = threading.Thread(target=start_single_udp_forward, args=(cfg.lhost, lp, cfg.rhost, rp), daemon=True)
        t.start()
        threads.append(t)
        log(f"Started reverseports {cfg.lhost}:{lp} -> {cfg.rhost}:{rp}")
        print(f"{Fore.MAGENTA}[RPORTS]{Style.RESET_ALL} {cfg.lhost}:{lp} -> {cfg.rhost}:{rp}")
    for t in threads:
        t.join()

def run_selected_mod():
    if cfg.mod == 0:
        run_classic()
    elif cfg.mod == 1:
        run_twin()
    elif cfg.mod == 2:
        run_ports_forwarding()
    elif cfg.mod == 3:
        run_reverse_ports_forwarding()
    else:
        print("Invalid mod")

def print_wizard_help():
    print(f"""
Wizard commands:
  set:lhost <ip>
  set:lport <port>
  set:rhost <ip>
  set:rport <port>
  set:R <lhost> <rhost> <lport> <rport>
  set:lport <p1> <p2> ...
  set:rport <p1> <p2> ...
  show
  start
  help
  exit
""")

def run_wizard():
    print(f"{Fore.GREEN}--- Forwarder Wizard ---{Style.RESET_ALL}")
    while True:
        print("[0] TCP\n[1] UDP\n[99] Exit")
        c = input("Select protocol: ").strip()
        if c == "" or c == "0":
            cfg.mode = "tcp"; break
        elif c == "1":
            cfg.mode = "udp"; break
        elif c == "99":
            sys.exit(0)
    while True:
        print("[0]classic\n[1]twinsmod\n[2]portsforwading\n[3]reverseportsforwading\n[99]Exit")
        m = input("MOD: ").strip()
        if m in ("0","1","2","3"):
            cfg.mod = int(m); break
        elif m == "99":
            sys.exit(0)
    print_wizard_help()

    while True:
        cmd = input("set: ").strip()
        if cmd == "show":
            print("Mode:", cfg.mode, "Mod:", cfg.mod)
            print("Single:", cfg.lhost, cfg.lport, "->", cfg.rhost, cfg.rport)
            print("Twin:", cfg.twin)
            print("Lports:", cfg.lports)
            print("Rports:", cfg.rports)
            continue
        if cmd == "start":
            run_selected_mod()
            break
        if cmd == "exit":
            sys.exit(0)

        if cmd.startswith("set:"):
            try:
                rest = cmd[4:].strip()
                if rest.startswith("R "):
                    p = rest.split()
                    _, lh, rh, lp, rp = p
                    cfg.twin.append((lh, int(lp), rh, int(rp)))
                    print("Added twin")
                    continue
                p = rest.split()
                k = p[0]; vals = p[1:]
                if k == "lhost":
                    cfg.lhost = vals[0]
                elif k == "rhost":
                    cfg.rhost = vals[0]
                elif k == "lport":
                    nums = [int(x) for x in vals]
                    if cfg.mod == 2:
                        cfg.lports = nums
                    else:
                        cfg.lport = nums[0]
                elif k == "rport":
                    nums = [int(x) for x in vals]
                    if cfg.mod == 3:
                        cfg.rports = nums
                    else:
                        cfg.rport = nums[0]
            except:
                print("Parse error")
                continue

def parse_cli_and_run():
    parser = OptionParser()

    # EXTRA ADDED ARGS
    parser.add_option("-f", "--lhost", dest="lhost", help="Set local host")
    parser.add_option("-d", "--lport", dest="lport", type="int", help="Set local port")
    parser.add_option("-i", "--rhost", dest="rhost", help="Set remote host")
    parser.add_option("-r", "--rport", dest="rport", type="int", help="Set remote port")

    parser.add_option("-k", "--udp", action="store_true", dest="udp", help="Use UDP")
    parser.add_option("-g", "--tcp", action="store_true", dest="tcp", help="Use TCP")
    parser.add_option("-w", "--wizard", action="store_true", dest="wizard", help="Start wizard")
    parser.add_option("-m", "--mod", dest="mod", type="int", help="Select mod")

    (opts, args) = parser.parse_args()

    if opts.lhost: cfg.lhost = opts.lhost
    if opts.lport: cfg.lport = opts.lport
    if opts.rhost: cfg.rhost = opts.rhost
    if opts.rport: cfg.rport = opts.rport

    if opts.udp:
        cfg.mode = "udp"
    elif opts.tcp:
        cfg.mode = "tcp"

    if opts.mod is not None:
        cfg.mod = opts.mod

    if opts.wizard:
        run_wizard()
        return

    run_selected_mod()

if __name__ == "__main__":
    parse_cli_and_run()
