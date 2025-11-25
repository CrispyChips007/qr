#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

# === ENTER YOUR VALUES HERE ===
# You can use decimal, or 0x-prefixed hex.

p_str = "PASTE_P_HERE"
q_str = "PASTE_Q_HERE"
e_str = "65537"

# --- parse values (supports hex like 0xABCD or decimal) ---
def parse_int(s):
    s = s.strip()
    if s.lower().startswith("0x"):
        return int(s, 16)
    return int(s)

p = parse_int(p_str)
q = parse_int(q_str)
e = parse_int(e_str)

# sanity check
if p >= q:
    print("[*] Note: p >= q (that's fine, just unusual)")
n = p * q
phi = (p - 1) * (q - 1)

# compute private exponent d
d = inverse(e, phi)

print("[+] Reconstructed values:")
print(f"  n  = {n}")
print(f"  e  = {e}")
print(f"  d  = {d}")
print(f"  p  = {p}")
print(f"  q  = {q}")

# build RSA key
key = RSA.construct((n, e, d, p, q))

pem = key.export_key()
with open("recovered.pem", "wb") as f:
    f.write(pem)

print("\n[+] Wrote private key to recovered.pem")
print("[+] You can now decrypt with something like:")
print("    openssl rsautl -decrypt -inkey recovered.pem -in mission.enc -out mission.txt")

