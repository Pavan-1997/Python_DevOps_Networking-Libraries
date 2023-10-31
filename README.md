# Python_DevOps_Networking-Libraries

## Socket Library

The socket library provides low-level networking capabilities. It allows you to create sockets for communication between processes. Here's a basic example of a Python server-client communication using the `socket` library. The server will listen for incoming connections, and the client will connect to the server and send a message.

**Implementation**

1. Save the server script in a file, e.g., `server.py`.
2. Save the client script in another file, e.g., `client.py`.
3. Open two terminal windows.
4. In the first terminal, run `python server.py` to start the server.
5. In the second terminal, run `python client.py` to start the client.

    You should see output indicating that the client sends a message, the server receives it, and then echoes it back to the client.

- Both the `server.py` and `client.py` are present in the repo 


##  Requests Library

The `requests` library in Python is a widely-used library for making HTTP requests. It simplifies the process of sending HTTP requests and handling responses. Below is an example that demonstrates how to use the `requests` library to make a simple HTTP GET request:

**Implementation**

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
