python
import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                return port
    except Exception:
        return None

def scan_ports(target, start_port=1, end_port=1024, threads=100):
    print(f"Scanning ports on {target} from {start_port} to {end_port}...")
    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(scan_port, target, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)
    
    if open_ports:
        print("Open ports:")
        for port in sorted(open_ports):
            print(f" - Port {port}")
    else:
        print("No open ports found.")

if name == "main":
  target_ip = input("Enter the IP address to scan: ")
    start = int(input("Start port (default 1): ") or 1)
    end = int(input("End port (default 1024): ") or 1024)
    scan_ports(target_ip, start, end)
