<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/CustomTkinter-GUI-1E90FF?style=for-the-badge" alt="CustomTkinter"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge" alt="Platform"/>
</p>

<h1 align="center">👑 LAN File Sharer — Premium Edition</h1>

<p align="center">
  <strong>A feature-rich, zero-config local network file sharing & real-time chat application with a premium desktop GUI and modern web interface.</strong>
</p>

<p align="center">
  Share files, folders, and messages across all devices on your LAN — instantly. No internet required. No sign-ups. Just launch, share, and go.
</p>

---

## ✨ Features at a Glance

| Category | Feature | Description |
|---|---|---|
| 📁 **File Sharing** | Drag & Drop Sharing | Share individual files or entire folders with one click |
| 📦 **Bulk Download** | Multi-Select ZIP | Clients can select multiple files and download as a single ZIP archive |
| 🔒 **Security** | PIN-Protected Server | Optional 4-digit PIN gate — only authorized users can access shared content |
| 🔐 **Per-File Locks** | Individual File PINs | Set unique PINs on sensitive files for granular access control |
| 💬 **Live Chat** | Real-Time Messaging | Built-in group & private chat with image/video/file attachments |
| 📱 **QR Code Access** | Instant Device Onboarding | Auto-generated QR code for quick mobile/tablet connections |
| 👥 **User Management** | Device Dashboard | See connected devices, rename users, toggle upload permissions, and kick users |
| 📤 **Client Uploads** | Bidirectional Transfers | Connected devices can upload files back to the host (permission-based) |
| 🌐 **Responsive Web UI** | Mobile-First Design | Premium dark-themed web interface that adapts to any screen size |
| 📊 **Live Logs** | Server Activity Monitor | Real-time activity feed with device tracking and event logging |

---

## 🖥️ Screenshots

### Desktop Admin Dashboard
```
┌─────────────────────────────────────────────────────────┐
│  👑 My LAN File Sharer — Premium Edition                │
│  ┌──────────────────┬──────────────────┐                │
│  │  📁 Shared Files  │  ⚙️ Settings     │                │
│  │  ┌──────────────┐ │  Host Name: Admin│                │
│  │  │ 📄 report.pdf│ │  Port: 5000      │                │
│  │  │ 📁 photos/   │ │  🔒 Secure Mode  │                │
│  │  │ 🎬 demo.mp4  │ │                  │                │
│  │  └──────────────┘ │  [🚀 Start Server]│               │
│  │  [+ Files][+Folder]│  ┌────────────┐ │                │
│  └──────────────────┴──┤  QR Code     │─┘                │
│  ⚡ Live Logs           │  [████████]  │ 📱 Devices (3)  │
│  > User1 downloaded... └────────────┘                   │
│  > User2 uploaded...                                     │
└─────────────────────────────────────────────────────────┘
```

### Mobile Web Client
```
┌───────────────────┐
│ 👑 Admin's Server │
│    🔒 SECURE      │
│                   │
│ 📤 Share a File   │
│ ┌───────────────┐ │
│ │ Choose File   │ │
│ └───────────────┘ │
│                   │
│ 📄 report.pdf     │
│    142 KB [⬇ DL]  │
│ 📁 photos/        │
│    12 MB  [⬇ DL]  │
│ 🔒 secret.zip     │
│    5 MB  [Decrypt]│
│                   │
│            💬     │
└───────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** installed on the host machine
- All devices must be connected to the **same local network** (Wi-Fi / Ethernet)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/PoojanPatel7/LAN_POOJAN.git
cd LAN_POOJAN

# 2. Install dependencies
pip install customtkinter flask qrcode pillow

# 3. Launch the application
python local_lan.py
```

### One-Liner Setup

```bash
pip install customtkinter flask qrcode pillow && python local_lan.py
```

---

## 📖 Usage Guide

### For the Host (Admin)

1. **Launch** `local_lan.py` — the Premium Dashboard opens
2. **Configure** your host name, port, and security preferences
3. **Add files/folders** using the `+ Files` and `+ Folder` buttons
4. **Start the server** with the green `🚀 Start Server` button
5. **Share access** — copy the link, open the web view, or let clients scan the QR code
6. **Monitor** connected devices, manage permissions, and chat in real time

### For Clients (Any Device on LAN)

1. **Scan the QR code** or enter the server URL in any browser
2. **Enter your name** when prompted
3. **Enter the PIN** (if the server is secured)
4. **Browse, search, and download** shared files
5. **Upload files** back to the host (if permitted)
6. **Chat** with the host and other connected users via the 💬 button

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────┐
│                    HOST MACHINE                       │
│                                                       │
│  ┌─────────────────┐     ┌─────────────────────────┐ │
│  │  CustomTkinter   │◄───►│     Flask Web Server     │ │
│  │  Desktop GUI     │     │     (Threaded)           │ │
│  │                  │     │                          │ │
│  │  • File Manager  │     │  • REST API (/api/files) │ │
│  │  • User Manager  │     │  • Chat API (/api/chat)  │ │
│  │  • Chat Hub      │     │  • File Streaming        │ │
│  │  • Activity Logs │     │  • Auth Middleware        │ │
│  └─────────────────┘     └───────────┬─────────────┘ │
│         ▲                            │                │
│         │     gui_command_queue       │                │
│         └────────────────────────────┘                │
└──────────────────────────┬───────────────────────────┘
                           │  HTTP (Port 5000)
          ─────────────────┼──────────────────
                           │  Local Network
              ┌────────────┼────────────────┐
              ▼            ▼                ▼
         ┌────────┐  ┌──────────┐    ┌──────────┐
         │📱Phone │  │💻 Laptop │    │📱 Tablet │
         │Browser │  │ Browser  │    │ Browser  │
         └────────┘  └──────────┘    └──────────┘
```

### Key Components

| Component | Technology | Role |
|---|---|---|
| Desktop GUI | `CustomTkinter` | Admin dashboard for managing files, users, and chat |
| Web Server | `Flask` + `Werkzeug` | Serves the web client and handles API requests |
| Web Client | Vanilla HTML/CSS/JS | Responsive, mobile-first interface for connected devices |
| QR Generator | `qrcode` + `Pillow` | Generates scannable access codes for quick onboarding |
| Threading | `threading` + `queue` | Decouples the GUI from the web server for smooth operation |

---

## 🔐 Security Model

| Layer | Mechanism | Details |
|---|---|---|
| **Server Access** | Global PIN (4-digit) | Optional — blocks all unauthenticated access |
| **Per-File Lock** | Individual PIN (4+ digits) | Encrypts download access per file |
| **QR Auto-Login** | PIN embedded in URL | Secure QR codes include the PIN for seamless auth |
| **Session Cookies** | Flask sessions | Authenticated state persists per client session |
| **User Control** | Kick / Permission Toggle | Host can disconnect users or revoke upload access |

> ⚠️ **Note:** This application is designed for **trusted local networks**. It does not implement TLS/SSL encryption. Do not expose the server to the public internet.

---

## 🛠️ Configuration

| Parameter | Default | Description |
|---|---|---|
| `Port` | `5000` | Server port (also supports 8000, 8080, 8888, 9000) |
| `Host Name` | `Admin` | Display name shown to all connected clients |
| `Secure Mode` | `Off` | Toggle PIN-protected server access |
| `Upload Permission` | `On` | Per-user toggle — allow or deny file uploads |
| `Live Chat` | `Off` | Enable/disable the real-time chat room |

---

## 📂 Project Structure

```
lan-file-sharer/
├── local_lan.py           # Main application (GUI + Server + Web Client)
├── README.md              # Project documentation
├── LICENSE                 # MIT License
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore rules
└── LAN_Shared_Uploads/    # Runtime directory for uploaded files (auto-created)
    └── Chat_Media/        # Runtime directory for chat attachments (auto-created)
```

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| `customtkinter` | Latest | Modern themed Tkinter GUI framework |
| `flask` | Latest | Lightweight WSGI web server |
| `qrcode` | Latest | QR code generation for device access |
| `Pillow` | Latest | Image processing for QR codes and thumbnails |

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code style
- Keep the single-file architecture for simplicity
- Test on at least two devices before submitting network-related changes
- Maintain backward compatibility with Python 3.8+

---

## 📋 Roadmap

- [ ] Drag-and-drop file sharing on the web client
- [ ] End-to-end encrypted file transfers
- [ ] Persistent chat history (SQLite)
- [ ] File preview (images, PDFs) in the web client
- [ ] Bandwidth throttling and transfer speed display
- [ ] Multi-language support (i18n)
- [ ] Packaged executable (PyInstaller / cx_Freeze)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Poojan** — [GitHub Profile](https://github.com/PoojanPatel7)

---

<p align="center">
  <strong>Built with ❤️ for seamless local file sharing</strong>
</p>

<p align="center">
  <sub>If you found this project useful, consider giving it a ⭐ on GitHub!</sub>
</p>
