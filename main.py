import requests
import os

# 从 GitHub Secrets 中读取敏感数据
# 注意：稍后会在 GitHub 设置里填入这两个具体的值
XSRF_TOKEN_VALUE = os.environ.get("XSRF_TOKEN")
X10_SESSION_VALUE = os.environ.get("X10_SESSION")

if not XSRF_TOKEN_VALUE or not X10_SESSION_VALUE:
    print("错误：未检测到 Cookie 信息，请在 GitHub Secrets 中配置 XSRF_TOKEN 和 X10_SESSION")
    exit(1)

# 创建 session 对象
session = requests.Session()

# 你的 User-Agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

# 设置请求头
headers = {
    "User-Agent": user_agent,
    "Referer": "https://x10hosting.com/login",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}

# 你的 Cookies (自动从 Secrets 读取)
cookies = {
    "XSRF-TOKEN": XSRF_TOKEN_VALUE,
    "x10hosting_session": X10_SESSION_VALUE
}

print("正在尝试访问 x10hosting 面板...")

try:
    # 访问面板页面
    response = session.get("https://x10hosting.com/panel", headers=headers, cookies=cookies, timeout=30)

    # 检查是否成功访问
    if response.status_code == 200:
        # 为了确认真的进去了，检查一下页面里有没有典型的关键词，比如 "Dashboard" 或 "Logout"
        if "Dashboard" in response.text or "Logout" in response.text or "Sign out" in response.text:
            print(">>> 登录保号成功！状态码: 200")
        else:
            print(f">>> 状态码 200，但未检测到登录特征。Cookie 可能已过期，或者被 Cloudflare 拦截。")
            print("页面部分内容预览:", response.text[:200]) # 打印前200个字符看看情况
    else:
        print(f">>> 登录失败，状态码: {response.status_code}")

except Exception as e:
    print(f"发生错误: {e}")
