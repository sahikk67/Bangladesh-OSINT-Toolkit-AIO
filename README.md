# 🇧🇩 Bangladesh OSINT Toolkit — AIO Edition

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![OSINT](https://img.shields.io/badge/OSINT-Bangladesh-red)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Termux-orange)

All-in-One, legal OSINT helper tailored for Bangladesh — domain, IP, phone, email, NID validation, Truecaller lookup, metadata extraction, website health checks, and more.

---

Table of contents
- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage & Examples](#usage--examples)
- [Flags / Options Reference](#flags--options-reference)
- [Notes & Limitations](#notes--limitations)
- [Contributing](#contributing)
- [Author & Contact](#author--contact)
- [License](#license)

---

## Features
- WHOIS lookup
- DNS records & subdomain discovery (crt.sh)
- IP geolocation
- Port scan & basic website health checks
- Bangladesh mobile intelligence (operator, validity hint)
- Truecaller open-search URL generator
- NID validator (10 / 13 / 17 digit formats)
- Email OSINT including MX checks
- File metadata extraction (EXIF) and simple User-Agent parsing

---

## Quick start
1. Clone or download this repo to your machine:
   ```bash
   git clone https://github.com/sahikk67/Bangladesh-OSINT-Toolkit-AIO.git
   cd Bangladesh-OSINT-Toolkit-AIO
   ```
2. Use a virtual environment (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux / macOS
   .venv\Scripts\activate      # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Run the tool:
```bash
python "Bangladesh OSINT Toolkit AIO Edition.py" --help
```

Notes:
- Use `python3` if your system maps `python` to Python 2.
- On Termux, make sure you have python and pip installed: `pkg install python` then proceed.

---

## Usage & Examples

General pattern:
```bash
python "Bangladesh OSINT Toolkit AIO Edition.py" <flag> <value>
```

Domain / Network OSINT:
```bash
python "Bangladesh OSINT Toolkit AIO Edition.py" --whois example.com
python "Bangladesh OSINT Toolkit AIO Edition.py" --dns dhaka.gov.bd
python "Bangladesh OSINT Toolkit AIO Edition.py" --subdomain robibank.com
python "Bangladesh OSINT Toolkit AIO Edition.py" --geo 103.78.84.1
python "Bangladesh OSINT Toolkit AIO Edition.py" --scan 103.78.84.1
```

Bangladesh Phone:
```bash
python "Bangladesh OSINT Toolkit AIO Edition.py" --phone 01712345678
python "Bangladesh OSINT Toolkit AIO Edition.py" --truecaller 01712345678
```

NID / Email:
```bash
python "Bangladesh OSINT Toolkit AIO Edition.py" --nid 19951234567890123
python "Bangladesh OSINT Toolkit AIO Edition.py" --email example@gmail.com
```

File metadata / User-Agent:
```bash
python "Bangladesh OSINT Toolkit AIO Edition.py" --meta sample.jpg
python "Bangladesh OSINT Toolkit AIO Edition.py" --ua "Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."
```

---

## Flags / Options Reference

- Domain / Network
  - --whois <domain>       : Fetch WHOIS information
  - --dns <domain>         : Resolve DNS records (A, AAAA, MX, NS, TXT)
  - --subdomain <domain>   : Discover subdomains via crt.sh
  - --geo <ip>             : IP geolocation lookup
  - --scan <ip>            : Basic port scanning (use responsibly)

- Bangladesh Phone
  - --phone <mobile>       : BD mobile operator and quick info
  - --truecaller <mobile>  : Generate Truecaller open-search URL (not scraping)

- NID / Email
  - --nid <nid_number>     : Validate NID format (10/13/17 digits)
  - --email <email>        : Email intel & MX record check

- Files / UA
  - --meta <file>          : Extract file metadata / EXIF
  - --ua "<user-agent>"    : Parse user-agent string into platform/browser details

Use `--help` to show flags implemented in code, and confirm exact script name if you renamed the file.

---

## Notes & Limitations
- This repository contains tools for passive and open-source information gathering. Do not use it for illegal activities.
- Respect target site terms of service, rate limits, and privacy laws. Always obtain authorization before scanning or collecting personal data that you don't own.
- Some lookups rely on third-party services (crt.sh, WHOIS servers, Truecaller URL patterns). If those services change, results may be affected.
- Port scanning can be intrusive — only scan systems you own or have explicit permission to test.

---

## Contributing
Contributions are welcome! A few ways to help:
- Open an issue if something breaks or a command fails.
- Send a pull request to:
  - fix bugs
  - add platform instructions (Termux tips, Windows notes)
  - add tests or CI
- Follow the repo style and include tests/examples for new features.

Please include clear commit messages and update README/examples when adding new flags.

---

## Author & Contact
Tool by: Sahikk (sahikk67)
- Instagram: https://www.instagram.com/ixe.67_/

If you want features added or help packaging the tool (PyPI, single-file exe), open an issue or PR.

---

## License
MIT — [see LICENSE file for details.](https://github.com/sahikk67/Bangladesh-OSINT-Toolkit-AIO/blob/main/LICENSE)

---

Ethics: This toolkit is strictly for lawful investigations, research & digital forensics only.
Do NOT use on unauthorized systems.
