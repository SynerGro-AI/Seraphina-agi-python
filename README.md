# Seraphina AGI Companion (Python)

Pure Python AGI companion for Seraphina - no mining, no wallets.

## Install

### From GitHub (Recommended)

```bash
pip install git+https://github.com/yourusername/seraphina-agi-python.git
```

Replace `yourusername` with your GitHub username.

### Local Install

```bash
cd seraphina-agi-python
pip install -e .
```

Note: The script installs to `%APPDATA%\Python\Python313\Scripts\seraphina-agi.exe` (user install). Add this to PATH or run directly.

## Usage

### CLI

```bash
seraphina-agi process --input "Hello, world!"
# Or directly: %APPDATA%\Python\Python313\Scripts\seraphina-agi.exe process --input "Hello, world!"
```

### API

```bash
seraphina-agi serve --port 8080
# Or directly: %APPDATA%\Python\Python313\Scripts\seraphina-agi.exe serve --port 8080
```

Then POST to http://localhost:8080/process with JSON {"input": "text"}

## Features

- Language processing with encryption
- HTTP API
- Pure Python