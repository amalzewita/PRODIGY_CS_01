# Caesar Cipher Encryption and Decryption in Python

This project provides a Python implementation of the **Caesar Cipher**, a classic encryption algorithm where each letter in the plaintext is shifted by a certain number of positions in the alphabet. The program allows users to input a message and a shift value to both encrypt and decrypt the message.

## Features

- **Encrypt a message** using a specified shift value.
- **Decrypt a message** that was encrypted with the Caesar Cipher.
- Handles **both uppercase and lowercase letters**.
- **Non-alphabetic characters** (e.g., spaces, punctuation) are left unchanged.

## How It Works

The Caesar Cipher shifts each letter by a fixed number of positions in the alphabet (shift value). For example, with a shift of `3`, `A` becomes `D`, `B` becomes `E`, and so on. After `Z`, the alphabet wraps around to `A` again. The same principle is applied for decryption, but the shift is reversed.

### Example

- **Plaintext**: `Hello, World!`
- **Shift Value**: `3`
- **Encrypted Message**: `Khoor, Zruog!`
- **Decrypted Message**: `Hello, World!`

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Running the Program

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/your-username/caesar-cipher.git
