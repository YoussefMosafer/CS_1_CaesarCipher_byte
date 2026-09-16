# CS_1_CaesarCipher_byte
A Python based Caesar Cipher tool for text encryption and decryption built for the AVIP 2026 Cybersecurity Internship at Arithmatrix.

# CS_1_CaesarCipher_byte

**Task 1 — Caesar Cipher (Text Encryption / Decryption)**
AVIP 2026 · Cybersecurity Track · B.Y.T.E by Arithmatrix

## Overview

A simple Python tool that encrypts and decrypts text using the classic
Caesar Cipher technique. Each alphabetic character in the input is shifted
by a configurable number of positions in the alphabet, while all
non-alphabet characters (spaces, digits, punctuation) are left unchanged.

## How It Works

- Encryption shifts each letter **forward** by `shift` positions (e.g., shift 3: A → D).
- Decryption shifts each letter **backward** by the same amount (D → A).
- Case is preserved (A stays uppercase, a stays lowercase).
- Non-alphabet characters pass through unchanged.
- Shift values wrap correctly (shift 27 behaves like shift 1); negative shifts supported.

## Usage

```bash
python caesar.py --mode encrypt --text "Hello, World!" --shift 3
python caesar.py --mode decrypt --text "Khoor, Zruog!" --shift 3
```

Or run with no arguments for interactive mode.

## Example Input/Output

| Mode    | Input             | Shift | Output            |
|---------|-------------------|-------|--------------------|
| Encrypt | Hello, World!     | 3     | Khoor, Zruog!      |
| Decrypt | Khoor, Zruog!     | 3     | Hello, World!      |

See `sample_input.txt` / `sample_output.txt` for full examples, and
`transcript.txt` for a recorded terminal session.

## Requirements Covered

- [x] Accepts plaintext and shift/key input
- [x] Encryption and decryption supported
- [x] Configurable shift values
- [x] Preserves non-alphabet characters
- [x] Example input/output included
- [x] Sample execution transcript included

## Requirements

- Python 3.6+, no external libraries needed
