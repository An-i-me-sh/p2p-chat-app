# P2P Chat Application

A terminal-based multi-client chat application using Python sockets.  
This project is being developed as a foundation for a decentralized communication system.

## Features
- Multi-client support
- Real-time messaging
- Message broadcasting across clients
- Username-based messaging
- Threaded client handling
- Length-prefixed protocol
- Works over LAN (local network)

## Recent Updates
- Implemented multi-client broadcasting
- Fixed client receive logic for real-time updates
- Improved terminal prompt behavior

## Tech Stack
- Python
- Socket Programming
- Threading

## How to Run

### Start server
```bash
python server.py
```

### Start client
```bash
python client.py
```
Run multiple clients in separate terminals.

## Future Work
- JSON-based message protocol
- Private messaging (@username)
- File transfer (chunk-based)
- Message acknowledgment and retry
- End-to-End Encryption
- Peer-to-peer (decentralized communication)

## Project Status
Currently in development, focusing on building core networking and messaging features.