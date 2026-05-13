import socket

print("=== Simple Port Scanner ===")

# Target website or IP
target = input("Enter target website or IP: ")

# Common ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 443]

print(f"\nScanning target: {target}\n")

for port in ports:
    try:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout
        s.settimeout(1)

        # Try connecting
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

        s.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        break

    except socket.error:
        print("Could not connect to server.")
        break