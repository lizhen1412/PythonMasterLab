# Python 3.11+ Network and Security Basics (Chapter 31)

This chapter covers network programming and security modules:
- urllib.parse and request building
- hashlib and hmac
- ssl (SSL/TLS wrapped sockets and HTTPS clients)
- selectors (I/O multiplexing for scalable servers)
- socketserver (high-level TCP/UDP server framework)

All examples use localhost to avoid external network issues.

---

## 1) How to run

From repo root:

- Index: `python3 01_Basics/31_Network_Security/01_overview.py`
- Single lesson: `python3 01_Basics/31_Network_Security/02_urllib_parse_basics.py`
- Exercises index: `python3 01_Basics/31_Network_Security/Exercises/01_overview.py`

---

## 2) Key topics checklist

- urlparse, urlencode, parse_qs
- Request building without sending
- hashlib digest and hexdigest
- hmac with compare_digest
- **ssl.create_default_context, SSL wrapped sockets, HTTPS clients**
- **selectors.DefaultSelector, I/O multiplexing, scalable echo servers**
- **socketserver.TCPServer/UDPServer, request handlers, mixins for concurrency**

---

## 3) Files

| No. | File | What it covers |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | Index of lessons |
| 02 | [`02_urllib_parse_basics.py`](02_urllib_parse_basics.py) | URL parsing and encoding |
| 03 | [`03_urllib_request_build.py`](03_urllib_request_build.py) | Build Request objects |
| 04 | [`04_hashlib_basics.py`](04_hashlib_basics.py) | Hashing basics |
| 05 | [`05_hmac_basics.py`](05_hmac_basics.py) | HMAC basics |
| 06 | [`06_ssl_context_basics.py`](06_ssl_context_basics.py) | SSL context basics |
| 07 | [`07_chapter_summary.py`](07_chapter_summary.py) | Summary |
| 08 | [`08_ssl_wrapped_socket.py`](08_ssl_wrapped_socket.py) | SSL wrapped sockets and HTTPS client |
| 09 | [`09_selectors_basics.py`](09_selectors_basics.py) | selectors: I/O multiplexing |
| 10 | [`10_socketserver_basics.py`](10_socketserver_basics.py) | socketserver: TCP/UDP servers |
| 11 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | Exercises index |

---

## 4) Network Programming Coverage

### 4.1 Socket Module (covered in Chapter 15)
- TCP client/server: bind(), listen(), accept(), connect()
- UDP client/server: sendto(), recvfrom()
- Socket options: SO_REUSEADDR, SO_KEEPALIVE, TCP_NODELAY
- Non-blocking I/O with select()

### 4.2 SSL Module (this chapter)
- Creating SSL contexts with custom settings
- Wrapping sockets with SSL/TLS
- Certificate verification modes (CERT_NONE, CERT_OPTIONAL, CERT_REQUIRED)
- Building HTTPS clients
- SSL socket methods (getpeercert(), cipher(), version())

### 4.3 Selectors Module (this chapter)
- selectors.DefaultSelector for cross-platform I/O multiplexing
- Registering file descriptors for read/write events
- Building scalable single-threaded servers
- Cross-platform abstraction (select/poll/epoll/kqueue)

### 4.4 Socketserver Module (this chapter)
- socketserver.TCPServer and UDPServer
- BaseRequestHandler for custom request handling
- StreamRequestHandler for file-like I/O
- ThreadingMixIn and ForkingMixIn for concurrency
- Server customization (allow_reuse_address, timeout, etc.)

---

## 5) Comparison: Low-level vs High-level APIs

| Task | Low-level (socket) | High-level (socketserver) | Async (asyncio) |
|------|-------------------|---------------------------|-----------------|
| TCP Server | socket + bind/listen/accept loop | TCPServer + handler | asyncio.start_server |
| UDP Server | socket + bind/sendto/recvfrom loop | UDPServer + handler | DatagramProtocol |
| Concurrency | Manual threading/forking | ThreadingMixIn/ForkingMixIn | Tasks/coroutines |
| Complexity | High | Medium | Medium |

---

## 6) Exercises

Run: `python3 01_Basics/31_Network_Security/Exercises/01_overview.py`

- `Exercises/02_parse_query_params.py`: Parse query params
- `Exercises/03_build_query_url.py`: Build URL with query
- `Exercises/04_hash_password.py`: Compute sha256
- `Exercises/05_hmac_verify.py`: Verify HMAC

---

## 7) Network Programming Best Practices

- Always use `with` statements for socket cleanup
- Set SO_REUSEADDR to avoid TIME_WAIT issues during development
- Use SSL/TLS for all production network communication
- Prefer selectors over select for cross-platform compatibility
- Use socketserver for simple servers, asyncio for complex async I/O
- Handle network exceptions gracefully (timeout, connection refused, etc.)
- Use connection pools for HTTP clients (see Requests framework)
