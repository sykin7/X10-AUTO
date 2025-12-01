import requests
import os
import sys

token = os.environ.get("XSRF_TOKEN")
session_id = os.environ.get("X10_SESSION")

if not token or not session_id:
    print("Missing environment variables.")
    sys.exit(1)

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Referer": "https://x10hosting.com/login",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Upgrade-Insecure-Requests": "1"
}

cookies = {
    "XSRF-TOKEN": token,
    "x10hosting_session": session_id
}

try:
    response = session.get("https://x10hosting.com/panel", headers=headers, cookies=cookies, timeout=30)
    
    if response.status_code == 200:
        if "Dashboard" in response.text or "Logout" in response.text:
            print("Login successful.")
        else:
            print("Status 200 but session invalid.")
            sys.exit(1)
    else:
        print(f"Request failed with status: {response.status_code}")
        sys.exit(1)

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
