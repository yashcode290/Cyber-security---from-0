# ============================================
# Day 6 - Phishing URL Detector
# ============================================

import re
from urllib.parse import urlparse

# Suspicious keywords commonly used in phishing URLs
SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "update",
    "bank",
    "secure",
    "account",
    "free",
    "bonus",
    "paypal",
    "signin"
]

def check_https(url):
    return url.startswith("https://")

def check_ip_address(url):
    # Detect IP-based URLs
    ip_pattern = r"(https?:\/\/)?(\d{1,3}\.){3}\d{1,3}"
    return re.search(ip_pattern, url)

def check_long_url(url):
    return len(url) > 75

def check_suspicious_words(url):
    for word in SUSPICIOUS_KEYWORDS:
        if word in url.lower():
            return True
    return False

def analyze_url(url):
    
    score = 0
    reasons = []

    # Check HTTPS
    if not check_https(url):
        score += 1
        reasons.append("URL does not use HTTPS")

    # Check IP Address
    if check_ip_address(url):
        score += 2
        reasons.append("URL uses IP address instead of domain")

    # Check URL Length
    if check_long_url(url):
        score += 1
        reasons.append("URL is unusually long")

    # Check Suspicious Keywords
    if check_suspicious_words(url):
        score += 2
        reasons.append("Suspicious keywords detected")

    # Final Result
    if score >= 3:
        result = "⚠️ PHISHING / SUSPICIOUS URL"
    else:
        result = "✅ SAFE URL"

    return result, reasons

# ============================================
# Main Program
# ============================================

print("===================================")
print("   PHISHING URL DETECTOR")
print("===================================")
url = input("Enter URL: ")

result, reasons = analyze_url(url)

print("\nResult:")
print(result)

print("\nAnalysis Report:")
if reasons:
    for reason in reasons:
        print(f"- {reason}")
else:
    print("- No suspicious activity detected")