# 🔐 File Encryption System

A secure file encryption and decryption tool built with Python, leveraging industry-standard cryptographic algorithms (AES & RSA) to protect sensitive files.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Supported File Types](#supported-file-types)
- [Cryptographic Algorithms](#cryptographic-algorithms)
- [Security Considerations](#security-considerations)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 Overview

The **File Encryption System** is a Python-based application that enables users to securely encrypt and decrypt files using strong cryptographic algorithms. It supports password-based encryption via AES and asymmetric encryption via RSA, making it suitable for both individual use and secure data transfer scenarios.

Output is available in multiple formats including **hexadecimal** and **Base64**, and a simple CLI or UI interface makes interaction straightforward.

---

## ✨ Features

- 🔒 **AES Encryption** – Symmetric encryption using AES-256 in CBC/GCM mode
- 🔑 **RSA Encryption** – Asymmetric encryption for secure key exchange
- 📁 **Multi-format Support** – Works with `.txt`, `.pdf`, `.docx`, and more
- 🧂 **Salted Key Derivation** – Uses PBKDF2 to derive keys from user passwords
- 📤 **Base64 / Hex Output** – Ciphertext rendered in human-readable formats
- 🔓 **Decryption Support** – Full round-trip: encrypt → decrypt back to original
- 🖥️ **CLI Interface** – Clean command-line interface for ease of use
- 🛡️ **Secure IV/Nonce Handling** – Unique initialization vectors per encryption

---

## 🛠️ Tech Stack

| Component        | Technology                          |
|------------------|--------------------------------------|
| Language         | Python 3.8+                          |
| Crypto Library   | `cryptography` / `PyCryptodome`      |
| Key Derivation   | PBKDF2-HMAC-SHA256                   |
| Encoding         | Base64, Hexadecimal                  |
| Interface        | CLI (argparse) / Optional Tkinter UI |

---

## 📂 Project Structure

```
file-encryption-system/
│
├── src/
│   ├── encrypt.py          # Encryption logic (AES, RSA)
│   ├── decrypt.py          # Decryption logic
│   ├── key_manager.py      # Key generation and derivation
│   └── utils.py            # File I/O, encoding helpers
│
├── keys/
│   ├── public_key.pem      # RSA public key (generated)
│   └── private_key.pem     # RSA private key (generated)
│
├── tests/
│   └── test_encryption.py  # Unit tests
│
├── sample_files/           # Sample files for testing
├── requirements.txt
├── main.py                 # Entry point
└── README.md
```

---

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Mayank34784/file-encryption-system.git
cd file-encryption-system

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### `requirements.txt`

```
cryptography>=41.0.0
PyCryptodome>=3.19.0
argparse
```

---

## 🚀 Usage

### Encrypt a File

```bash
python main.py encrypt --file sample_files/document.pdf --password mySecurePass123 --output encrypted_doc.enc
```

### Decrypt a File

```bash
python main.py decrypt --file encrypted_doc.enc --password mySecurePass123 --output restored_document.pdf
```

### Generate RSA Key Pair

```bash
python main.py generate-keys --keysize 2048
```

### Encrypt with RSA Public Key

```bash
python main.py encrypt --file document.txt --mode rsa --pubkey keys/public_key.pem
```

### CLI Help

```bash
python main.py --help
```

---

## 📄 Supported File Types

| File Type    | Extension       |
|--------------|-----------------|
| Text Files   | `.txt`, `.csv`  |
| Documents    | `.pdf`, `.docx` |
| Images       | `.jpg`, `.png`  |
| Any Binary   | `.*`            |

> The system reads files as binary, so virtually any file type can be encrypted.

---

## 🔬 Cryptographic Algorithms

### AES (Advanced Encryption Standard)
- Key size: **256-bit**
- Mode: **GCM** (Galois/Counter Mode) for authenticated encryption
- IV: Randomly generated per session (stored with ciphertext)
- Key derivation: **PBKDF2-HMAC-SHA256** with random salt

### RSA
- Key size: **2048-bit** (configurable up to 4096-bit)
- Used for secure encryption of the AES session key (hybrid encryption)
- Keys stored as **PEM** format

### Key Derivation Flow (Password-based)

```
Password + Salt ──► PBKDF2-HMAC-SHA256 ──► 256-bit AES Key ──► Encrypt File
```

---

## 🛡️ Security Considerations

- **Never hardcode** passwords or keys in source code
- Always store private keys securely and **never commit them** to version control (add `keys/` to `.gitignore`)
- The salt and IV are prepended to the encrypted output — they are not secret but must be preserved for decryption
- Use strong, unique passwords for best security
- This tool is intended for **legal and ethical use only** — ensure you have authorization before encrypting files on any system you do not own

---

## 🖼️ Screenshots


```
$ python main.py encrypt --file report.pdf --password ••••••••
[✔] Reading file: report.pdf (245 KB)
[✔] Deriving encryption key...
[✔] Encrypting with AES-256-GCM...
[✔] File encrypted successfully → report.pdf.enc
    Output format : Base64
    Output size   : 328 KB
```

---

## 🧪 Running Tests

```bash
python -m pytest tests/
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@Mayank34784](https://github.com/Mayank34784)
- LinkedIn: [Mayank Shekhar](https://linkedin.com/in/mayank-cybersec)

---

> ⚠️ **Disclaimer:** This tool is developed for educational purposes and legitimate data protection use cases. Always ensure compliance with applicable laws and regulations before use.
