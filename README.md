# 🇧🇩 Bangladesh OSINT Toolkit — AIO Edition

All-in-One Legal OSINT Toolkit for Bangladesh:  
Domain, IP, Phone, Email, NID, Truecaller, Metadata, Website Health

---

### 🏆 Badges
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![OSINT](https://img.shields.io/badge/OSINT-Bangladesh-red)
![Platform](https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20Termux-orange)

---

## 👤 Author
**Tool by:** Sahikk  
**Instagram:** [ixe.67_](https://www.instagram.com/ixe.67_/)

---

## ⚡ Features
- WHOIS lookup
- DNS records & subdomain discovery (crt.sh)
- IP Geolocation
- Port scan & Website health
- Bangladesh Phone Intelligence
- Truecaller Open Search
- NID Validator (10/13/17 digit)
- Email OSINT & MX check
- File Metadata Extraction
- User-Agent Parsing

---

## 🚀 Installation

1. Download the ZIP file & extract it
Example: C:\Users\sahikk\Desktop\Bangladesh-OSINT-Toolkit-AIO
2. Open Terminal / PowerShell / VS Code terminal
3. Change folder:
cd C:\Users\sahikk\Desktop\Bangladesh-OSINT-Toolkit-AIO
4. Dependencies install
5. pip install -r requirements.txt

1️⃣ Domain / Network OSINT
| Option        | Description           | Example                                                                     |
| ------------- | --------------------- | --------------------------------------------------------------------------- |
| `--whois`     | WHOIS lookup          | `python "Bangladesh OSINT Toolkit AIO Edition.py" --whois google.com`       |
| `--dns`       | DNS resolution        | `python "Bangladesh OSINT Toolkit AIO Edition.py" --dns dhaka.gov.bd`       |
| `--subdomain` | Subdomains via crt.sh | `python "Bangladesh OSINT Toolkit AIO Edition.py" --subdomain robibank.com` |
| `--geo`       | IP Geolocation        | `python "Bangladesh OSINT Toolkit AIO Edition.py" --geo 103.78.84.1`        |
| `--scan`      | Port scan             | `python "Bangladesh OSINT Toolkit AIO Edition.py" --scan 103.78.84.1`       |
2️⃣ Bangladesh Phone
| Option         | Description                | Example                                                                     |
| -------------- | -------------------------- | --------------------------------------------------------------------------- |
| `--phone`      | BD mobile info             | `python "Bangladesh OSINT Toolkit AIO Edition.py" --phone 01712345678`      |
| `--truecaller` | Truecaller Open Search URL | `python "Bangladesh OSINT Toolkit AIO Edition.py" --truecaller 01712345678` |
3️⃣ BD NID / Email
| Option    | Description            | Example                                                                      |
| --------- | ---------------------- | ---------------------------------------------------------------------------- |
| `--nid`   | NID validator          | `python "Bangladesh OSINT Toolkit AIO Edition.py" --nid 19951234567890123`   |
| `--email` | Email OSINT & MX check | `python "Bangladesh OSINT Toolkit AIO Edition.py" --email example@gmail.com` |
4️⃣ File Metadata / User-Agent| Option   | Description       | Example                                              |
| -------- | ----------------- | ------------------------------------------------------------------------- |
| `--meta` | Extract metadata  | `python "Bangladesh OSINT Toolkit AIO Edition.py" --meta sample.jpg`      |
| `--ua`   | User-Agent parser | `python "Bangladesh OSINT Toolkit AIO Edition.py" --ua "Mozilla/5.0 ..."` |


5️⃣ Examples


# Domain / Network OSINT
python "Bangladesh OSINT Toolkit AIO Edition.py" --whois example.com
# DNS Lookup
python "Bangladesh OSINT Toolkit AIO Edition.py" --dns example.com
# Subdomain Discovery
python "Bangladesh OSINT Toolkit AIO Edition.py" --subdomain example.com
# IP Geolocation
python "Bangladesh OSINT Toolkit AIO Edition.py" --geo 103.78.84.1
# Port Scan
python "Bangladesh OSINT Toolkit AIO Edition.py" --scan 103.78.84.1

# Bangladesh Phone / Truecaller
python "Bangladesh OSINT Toolkit AIO Edition.py" --phone 01712345678
python "Bangladesh OSINT Toolkit AIO Edition.py" --truecaller 01712345678

# BD NID / Email OSINT
python "Bangladesh OSINT Toolkit AIO Edition.py" --nid 19951234567890123
python "Bangladesh OSINT Toolkit AIO Edition.py" --email example@gmail.com

# File Metadata Extraction
python "Bangladesh OSINT Toolkit AIO Edition.py" --meta sample.jpg
