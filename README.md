# Python_DevOps_Networking-Libraries

## Socket Library

The socket library provides low-level networking capabilities. It allows you to create sockets for communication between processes. Here's a basic example of a Python server-client communication using the `socket` library. The server will listen for incoming connections, and the client will connect to the server and send a message.

**Implementation:**

1. Save the server script in a file, e.g., `server.py`.
2. Save the client script in another file, e.g., `client.py`.
3. Open two terminal windows.
4. In the first terminal, run `python server.py` to start the server.
5. In the second terminal, run `python client.py` to start the client.

    You should see output indicating that the client sends a message, the server receives it, and then echoes it back to the client.

- Both the `server.py` and `client.py` are present in the repo 


##  Requests Library

The `requests` library in Python is a widely-used library for making HTTP requests. It simplifies the process of sending HTTP requests and handling responses. Below is an example that demonstrates how to use the `requests` library to make a simple HTTP GET request:

**Implementation:**

1. We import the `requests` module.
2. We use `requests.get()` to send a GET request to the specified URL (`https://jsonplaceholder.typicode.com/posts/1`).
3. We check if the response status code is `200`, which indicates a successful request.
4. If the request was successful, we print the response content, assuming it's in JSON format. If not, we print an error message along with the status code.

Keep in mind that you'll need an active internet connection to run this code since it makes a request to an external URL.

To run this code, you need to have the `requests` library installed. You can install it using `pip`:

```bash
pip install requests
```

The `requests` library is incredibly versatile and can be used for a wide range of HTTP operations, including making POST, PUT, DELETE requests, handling authentication, sessions, and much more.

- `DO_requests.py` is present in the repo


## Netmiko Library

Netmiko is a multi-vendor library that simplifies SSH connections to network devices and provides an easy-to-use interface for sending commands and receiving responses. It supports a wide range of network devices, including routers and switches from various vendors.

**Implementation:**

1. Import the `ConnectHandler` class from `netmiko`.
2. Define the device information, including the device type (e.g., `cisco_ios`), IP address, username, password, and enable password (if required).
3. Use `ConnectHandler(**device)` to establish an SSH connection to the device.
4. If required, use `connection.enable()` to enter enable mode.
5. Use `connection.send_command(command)` to send a command to the device and receive the output.
6. Print the output.
7. Use `connection.disconnect()` to close the SSH connection.

Before running this code, make sure you have the Netmiko library installed. You can install it using `pip`:

```bash
pip install netmiko
```

Note that you'll need to replace `'your_username'`, `'your_password'`, and `'enable_password'` with your actual login credentials. Also, ensure that you have SSH access enabled on the network device you're trying to connect to.

Keep in mind that Netmiko supports various device types, so you may need to adjust the `device_type` parameter depending on the type of network device you're connecting to (e.g., `cisco_ios`, `cisco_xr`, `juniper_junos`, etc.).

- `DO_netmiko.py` is present in the repo


## Scapy Library 

`Scapy` is a powerful packet manipulation tool in Python that allows you to create, send, and analyze network packets. It is widely used for network testing, analysis, and penetration testing. Below are some examples demonstrating the basic usage of `Scapy`:

### Example 1: Sending ICMP (Ping) Packet

```python
from scapy.all import *

# Create an ICMP packet
packet = IP(dst="www.google.com") / ICMP()

# Send the packet and receive a response
response = sr1(packet, timeout=2, verbose=False)

# Check if a response was received
if response:
    print(f"Received response from {response.src}")
else:
    print("No response received")
```

### Example 2: Sending TCP Packet

```python
from scapy.all import *

# Create a TCP packet
packet = IP(dst="www.example.com") / TCP(dport=80, flags="S")

# Send the packet and receive a response
response = sr1(packet, timeout=2, verbose=False)

# Check if a response was received
if response:
    print(f"Received response from {response.src}")
else:
    print("No response received")
```

### Example 3: Sniffing Packets

```python
from scapy.all import *

# Define a packet sniffing function
def packet_sniffer(packet):
    print(packet.summary())

# Start sniffing packets on the network
sniff(filter="icmp", prn=packet_sniffer, count=5)
```

### Example 4: Crafting a Custom Packet

```python
from scapy.all import *

# Create a custom packet
packet = Ether(src="00:11:22:33:44:55", dst="66:77:88:99:00:11") / \
         IP(src="192.168.1.100", dst="192.168.1.1") / \
         TCP(sport=1234, dport=80)

# Send the packet
sendp(packet, iface="eth0")
```

### Example 5: Creating and Sending ARP Request

```python
from scapy.all import *

# Create an ARP request packet
packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.1")

# Send the ARP request
response = srp1(packet, timeout=2, verbose=False)

# Check if a response was received
if response:
    print(f"Received response from {response.psrc}")
else:
    print("No response received")
```

Before running these examples, ensure that you have `Scapy` installed. You can install it using `pip`:

```bash
pip install scapy
```

Please note that some of these examples involve sending packets, which might not be appropriate or allowed in all environments. Always use caution and ensure you have appropriate permissions and legal rights to perform any network-related activities.


## Twisted Library 

The Twisted library is an event-driven networking framework for Python. It provides support for various protocols, including TCP, UDP, SSH, and more. Below are examples of using Twisted for a simple TCP server and client:

### Example 1: Twisted TCP Server

```python
from twisted.internet import protocol, reactor

class EchoProtocol(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return EchoProtocol()

reactor.listenTCP(12345, EchoFactory())
reactor.run()
```

In this example, we create a simple Echo server. It listens on port 12345 and echoes back any data it receives.

### Example 2: Twisted TCP Client

```python
from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(b'Hello, server!')

    def dataReceived(self, data):
        print(f'Received from server: {data.decode()}')
        self.transport.loseConnection()

class EchoClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print(f'Connection failed: {reason.getErrorMessage()}')
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print(f'Connection lost: {reason.getErrorMessage()}')
        reactor.stop()

connector = reactor.connectTCP('127.0.0.1', 12345, EchoClientFactory())
reactor.run()
```

In this example, we create a client that connects to a TCP server running on `127.0.0.1:12345`. It sends a message to the server and waits for a response.

Before running these examples, ensure that you have Twisted installed. You can install it using `pip`:

```bash
pip install twisted
```

These examples showcase a simple echo server and client. Twisted is capable of handling much more complex networking tasks, including protocols like HTTP, SMTP, IMAP, and more. It's a versatile library for building networked applications in Python.
