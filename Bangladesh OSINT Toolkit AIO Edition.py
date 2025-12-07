#!/usr/bin/env python3
"""
Bangladesh OSINT Toolkit — AIO Edition (improved / working)
---------------------------------------------------------
All-in-One Legal OSINT Toolkit for Bangladesh:
- Phone Lookup
- Email OSINT
- NID Validator
- Domain & Subdomain Scan (crt.sh)
- IP Geolocation
- Website Health
- SSL Scan (basic)
- Port Scan
- Metadata Extraction (exiftool or exifread fallback)
- Truecaller Lookup URL generator

Tool by: Sahikk
Instagram: https://www.instagram.com/ixe.67_/

⚠ Legal & safe OSINT only! Do not use on unauthorized systems.
"""

import argparse
import socket
import requests
import json
import re
import subprocess
import os
import shutil
from urllib.parse import quote

# ------------------------
# Helpers
# ------------------------

def check_command(name):
    return shutil.which(name)

def safe_print_json(obj):
    try:
        print(json.dumps(obj, indent=2, ensure_ascii=False))
    except Exception:
        print(obj)

# ------------------------
# DOMAIN / NETWORK OSINT
# ------------------------

def whois_lookup(target):
    whois_cmd = check_command("whois")
    if whois_cmd:
        try:
            output = subprocess.check_output([whois_cmd, target], stderr=subprocess.STDOUT, timeout=20)
            print(output.decode(errors="ignore"))
            return
        except Exception as e:
            print("[!] WHOIS lookup failed:", e)

    try:
        import whois as pywhois
        w = pywhois.whois(target)
        safe_print_json(w)
        return
    except Exception:
        pass

    print("[!] WHOIS not available. Install 'whois' or 'python-whois'.")

def dns_lookup(target):
    try:
        addrs = socket.getaddrinfo(target, None)
        ips = sorted({ai[4][0] for ai in addrs})
        print(f"[DNS] {target} => {', '.join(ips)}")
    except Exception as e:
        print("[!] DNS lookup failed:", e)

    try:
        import dns.resolver
        types = ["A","AAAA","MX","NS","TXT"]
        details = {}
        for t in types:
            try:
                answers = dns.resolver.resolve(target, t)
                details[t] = [r.to_text() for r in answers]
            except:
                details[t] = []
        print("\n[DNS Records]")
        safe_print_json(details)
    except:
        pass

def crtsh_subdomains(domain):
    query = quote(f"%{domain}")
    url = f"https://crt.sh/?q={query}&output=json"
    headers = {"User-Agent": "Bangladesh-OSINT-Toolkit/1.0"}
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            try:
                data = r.json()
                subs = set()
                for item in data:
                    nv = item.get("name_value", "")
                    for line in nv.splitlines():
                        if line:
                            subs.add(line.strip())
                if subs:
                    print("[Subdomains found]:")
                    for s in sorted(subs):
                        print(" -", s)
                    return
            except:
                pass

        page = r.text
        possible = set(re.findall(r"[a-z0-9\-\._]*\." + re.escape(domain), page, flags=re.IGNORECASE))
        if possible:
            print("[Subdomains (fallback)]:")
            for s in sorted(possible):
                print(" -", s)
            return

        print("[!] No subdomains found.")
    except Exception as e:
        print("[!] Could not fetch subdomains:", e)

def geo_ip(ip):
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=8)
        if r.status_code == 200:
            print("[IP Info - ipinfo.io]")
            safe_print_json(r.json())
            return
    except:
        pass

    try:
        r2 = requests.get(f"http://ip-api.com/json/{ip}", timeout=8)
        if r2.status_code == 200:
            print("[IP Info - ip-api.com]")
            safe_print_json(r2.json())
            return
    except Exception as e:
        print("[!] IP lookup failed:", e)

def port_scan(host):
    try:
        ip = socket.gethostbyname(host)
    except:
        ip = host

    print(f"[+] Scanning common ports on {host} ({ip})")
    common_ports = [21,22,23,25,53,80,110,143,443,445,587,993,995,3306,3389,8080]
    open_ports = []
    for port in common_ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((ip, port)) == 0:
                    print(f"[OPEN] {port}")
                    open_ports.append(port)
        except:
            pass

    if not open_ports:
        print("[*] No common ports open.")

# ------------------------
# BANGLADESH MOBILE OSINT
# ------------------------

operators = {
    "013": "Grameenphone",
    "014": "Banglalink",
    "015": "Teletalk",
    "016": "Airtel",
    "017": "Grameenphone",
    "018": "Robi",
    "019": "Banglalink",
}

def normalize_bd_phone(number):
    number = re.sub(r"[^\d+]", "", number)
    number = re.sub(r"^\+?88", "", number)
    if re.match(r"^01[0-9]{9}$", number):
        return number
    return None

def phone_intel(number):
    norm = normalize_bd_phone(number)
    if not norm:
        print("[!] Invalid BD phone format.")
        return
    prefix = norm[:3]
    operator = operators.get(prefix, "Unknown")
    print(f"""
📱 Bangladesh Phone Intelligence
--------------------------------
Number     : {norm}
Operator   : {operator}
Prefix     : {prefix}
Valid      : YES
""")

def truecaller_open(number):
    norm = normalize_bd_phone(number)
    if not norm:
        print("[!] Invalid BD phone format.")
        return
    url = f"https://www.truecaller.com/search/bd/{norm}"
    print(f"[+] Truecaller URL:\n{url}\n")

# ------------------------
# BD NID VALIDATOR
# ------------------------

def validate_nid(nid):
    nid = nid.strip()
    if re.match(r"^[0-9]{10}$", nid):
        print("✔ Valid 10-digit OLD BD NID")
    elif re.match(r"^[0-9]{13}$", nid):
        print("✔ Valid 13-digit BD NID")
    elif re.match(r"^[0-9]{17}$", nid):
        print(f"✔ Valid 17-digit NEW BD NID\nBirth Year: {nid[:4]}")
    else:
        print("❌ Invalid NID format.")

# ------------------------
# EMAIL OSINT
# ------------------------

def email_osint(email):
    email = email.strip()
    regex = r"^[\w\.\-+%]+@[\w\.\-]+\.\w+$"
    valid_format = bool(re.match(regex, email))
    domain = email.split("@")[-1] if "@" in email else None
    result = {"email": email, "valid_format": valid_format, "domain": domain, "mx": [], "resolves": None}

    if not domain:
        safe_print_json(result)
        return

    try:
        import dns.resolver
        try:
            answers = dns.resolver.resolve(domain, "MX")
            result["mx"] = [str(r.exchange).rstrip(".") for r in answers]
        except:
            pass
    except:
        pass

    try:
        ip = socket.gethostbyname(domain)
        result["resolves"] = ip
    except:
        pass

    safe_print_json(result)

# ------------------------
# FILE METADATA
# ------------------------

def extract_metadata(file):
    if not os.path.exists(file):
        print("[!] File not found.")
        return

    exiftool = check_command("exiftool")
    if exiftool:
        try:
            out = subprocess.check_output([exiftool, file], stderr=subprocess.STDOUT, timeout=20)
            print(out.decode(errors="ignore"))
            return
        except:
            pass

    try:
        import exifread
        with open(file, "rb") as fh:
            tags = exifread.process_file(fh)
            for k, v in tags.items():
                print(f"{k}: {v}")
            return
    except:
        pass

    print("[!] exiftool/exifread not installed.")

# ------------------------
# USER-AGENT PARSER
# ------------------------

def parse_ua(ua):
    ua = ua.strip()
    print("\n🔎 User-Agent Analysis\n------------------------")
    try:
        from user_agents import parse as ua_parse
        parsed = ua_parse(ua)
        print(f"OS      : {parsed.os.family} {parsed.os.version_string}")
        print(f"Browser : {parsed.browser.family} {parsed.browser.version_string}")
        print(f"Device  : {parsed.device.family}")
        print(f"Mobile  : {parsed.is_mobile}  Tablet: {parsed.is_tablet}  PC: {parsed.is_pc}")
        print(f"UA      : {ua}")
        return
    except:
        pass

    os_name = "Windows" if "Windows" in ua else \
              "Android" if "Android" in ua else \
              "iOS" if ("iPhone" in ua or "iPad" in ua) else \
              "Linux" if "Linux" in ua else "Unknown"

    browser = "Chrome" if "Chrome" in ua else \
              "Firefox" if "Firefox" in ua else \
              "Safari" if "Safari" in ua and "Chrome" not in ua else \
              "Edge" if "Edge" in ua else "Unknown"

    print(f"OS      : {os_name}")
    print(f"Browser : {browser}")
    print(f"UA      : {ua}")

# ------------------------
# CREDITS
# ------------------------

def show_credits():
    print("\n" + "-"*50)
    print("💡 Tool by Sahikk")
    print("📸 Instagram: https://www.instagram.com/ixe.67_/")
    print("-"*50 + "\n")

# ------------------------
# MAIN CLI
# ------------------------

def build_parser():
    filename = 'Bangladesh OSINT Toolkit AIO Edition.py'
    p = argparse.ArgumentParser(
        description="Bangladesh OSINT Toolkit — AIO Edition",
        epilog=(
            f"Examples:\n"
            f'  python "{filename}" --whois example.com\n'
            f'  python "{filename}" --phone +8801712345678\n'
            f'  python "{filename}" --email test@gmail.com'
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    p.add_argument("--whois", metavar="DOMAIN")
    p.add_argument("--dns", metavar="DOMAIN")
    p.add_argument("--subdomain", metavar="DOMAIN")
    p.add_argument("--geo", metavar="IP")
    p.add_argument("--scan", metavar="HOST")
    p.add_argument("--phone", metavar="NUMBER")
    p.add_argument("--truecaller", metavar="NUMBER")
    p.add_argument("--nid", metavar="NID")
    p.add_argument("--email", metavar="EMAIL")
    p.add_argument("--meta", metavar="FILE")
    p.add_argument("--ua", metavar="USERAGENT")

    return p

def main():
    parser = build_parser()
    args = parser.parse_args()
    used = False

    if args.whois: whois_lookup(args.whois); used = True
    if args.dns: dns_lookup(args.dns); used = True
    if args.subdomain: crtsh_subdomains(args.subdomain); used = True
    if args.geo: geo_ip(args.geo); used = True
    if args.scan: port_scan(args.scan); used = True
    if args.phone: phone_intel(args.phone); used = True
    if args.truecaller: truecaller_open(args.truecaller); used = True
    if args.nid: validate_nid(args.nid); used = True
    if args.email: email_osint(args.email); used = True
    if args.meta: extract_metadata(args.meta); used = True
    if args.ua: parse_ua(args.ua); used = True

    if not used:
        parser.print_help()

    show_credits()

if __name__ == "__main__":
    main()
