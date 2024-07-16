# text2hash

A simple Python script to generate hashes of input text using different hashing algorithms.

## Overview

This script takes user input text and generates a hash using specified hashing algorithms provided by Python's hashlib module.

## Features

- Supports various hashing algorithms such as MD5, SHA-1, SHA-256, etc.
- Command-line interface for easy interaction.
- Error handling for invalid algorithm selections.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/a-generation/text2hash.git
   cd text2hash
   ```

2. **Run the script:**

   ```bash
   python text2hash.py
   ```

3. **Follow the prompts:**

   - Enter the text you want to hash.
   - Choose an algorithm from the list displayed (e.g., md5, sha1, sha256).

4. **Output:**

   The script will output the hash value of the input text using the selected algorithm.

## Example

```bash
Enter text to hash: Hello, World!
Available algorithms: ['blake2b', 'blake2s', 'md4', 'md5', 'md5-sha1', 'ripemd160', 'sha1', 'sha224', 'sha256', 'sha3-224', 'sha3-256', 'sha3-384', 'sha3-512', 'sha384', 'sha512', 'shake_128', 'shake_256', 'sm3', 'whirlpool']
Choose an algorithm (e.g., md5, sha1, sha256): sha256
Hash (sha256): a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
