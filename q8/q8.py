import json

requests_data = """
[
 {
  "id": "req-01",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 12,
  "verifiedBot": false,
  "origin": "",
  "ip": "203.0.113.26",
  "country": "BR",
  "threatScore": 8
 },
 {
  "id": "req-02",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "python-httpx/0.28.1",
  "botScore": 55,
  "verifiedBot": true,
  "origin": "https://app-312.example",
  "ip": "198.51.100.43",
  "country": "US",
  "threatScore": 60
 },
 {
  "id": "req-03",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "UptimeMonitor/1.2",
  "botScore": 31,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "34.194.13.191",
  "country": "DE",
  "threatScore": 20
 },
 {
  "id": "req-04",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "UptimeMonitor/1.2",
  "botScore": 23,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "198.51.100.43",
  "country": "BR",
  "threatScore": 29
 },
 {
  "id": "req-05",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 54,
  "verifiedBot": false,
  "origin": "",
  "ip": "193.65.156.177",
  "country": "BR",
  "threatScore": 41
 },
 {
  "id": "req-06",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "python-httpx/0.28.1",
  "botScore": 27,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "136.111.182.215",
  "country": "SG",
  "threatScore": 5
 },
 {
  "id": "req-07",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "python-httpx/0.28.1",
  "botScore": 60,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "196.48.64.69",
  "country": "IN",
  "threatScore": 16
 },
 {
  "id": "req-08",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 50,
  "verifiedBot": false,
  "origin": "",
  "ip": "87.54.185.201",
  "country": "BR",
  "threatScore": 54
 },
 {
  "id": "req-09",
  "method": "GET",
  "path": "/blog/post",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 2,
  "verifiedBot": false,
  "origin": "",
  "ip": "184.169.66.103",
  "country": "US",
  "threatScore": 35
 },
 {
  "id": "req-10",
  "method": "GET",
  "path": "/",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 89,
  "verifiedBot": false,
  "origin": "https://evil-84.example",
  "ip": "80.225.176.9",
  "country": "US",
  "threatScore": 36
 },
 {
  "id": "req-11",
  "method": "GET",
  "path": "/blog/post",
  "ua": "curl/8.6.0",
  "botScore": 35,
  "verifiedBot": false,
  "origin": "",
  "ip": "203.0.113.26",
  "country": "DE",
  "threatScore": 42
 },
 {
  "id": "req-12",
  "method": "GET",
  "path": "/blog/post",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 74,
  "verifiedBot": false,
  "origin": "https://evil-58.example",
  "ip": "198.51.100.43",
  "country": "DE",
  "threatScore": 55
 },
 {
  "id": "req-13",
  "method": "POST",
  "path": "/admin/settings",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 45,
  "verifiedBot": true,
  "origin": "https://app-312.example",
  "ip": "119.215.53.128",
  "country": "BR",
  "threatScore": 59
 },
 {
  "id": "req-14",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "python-httpx/0.28.1",
  "botScore": 67,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "198.51.100.43",
  "country": "DE",
  "threatScore": 48
 },
 {
  "id": "req-15",
  "method": "GET",
  "path": "/",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 62,
  "verifiedBot": false,
  "origin": "https://evil-99.example",
  "ip": "203.0.113.26",
  "country": "SG",
  "threatScore": 37
 },
 {
  "id": "req-16",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 19,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "106.3.188.186",
  "country": "SG",
  "threatScore": 14
 },
 {
  "id": "req-17",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 7,
  "verifiedBot": false,
  "origin": "https://evil-54.example",
  "ip": "124.191.81.208",
  "country": "IN",
  "threatScore": 33
 },
 {
  "id": "req-18",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "python-httpx/0.28.1",
  "botScore": 8,
  "verifiedBot": false,
  "origin": "",
  "ip": "198.51.100.43",
  "country": "US",
  "threatScore": 10
 },
 {
  "id": "req-19",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 45,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "47.10.241.140",
  "country": "SG",
  "threatScore": 48
 },
 {
  "id": "req-20",
  "method": "GET",
  "path": "/blog/post",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 21,
  "verifiedBot": true,
  "origin": "",
  "ip": "66.249.66.181",
  "country": "US",
  "threatScore": 5
 },
 {
  "id": "req-21",
  "method": "POST",
  "path": "/login",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 65,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "139.26.242.67",
  "country": "DE",
  "threatScore": 18
 },
 {
  "id": "req-22",
  "method": "GET",
  "path": "/blog/post",
  "ua": "python-httpx/0.28.1",
  "botScore": 17,
  "verifiedBot": true,
  "origin": "https://app-312.example",
  "ip": "149.202.218.154",
  "country": "US",
  "threatScore": 5
 },
 {
  "id": "req-23",
  "method": "GET",
  "path": "/login",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 32,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "20.178.228.253",
  "country": "SG",
  "threatScore": 41
 },
 {
  "id": "req-24",
  "method": "GET",
  "path": "/",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 55,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "160.45.241.21",
  "country": "DE",
  "threatScore": 41
 },
 {
  "id": "req-25",
  "method": "GET",
  "path": "/admin/settings",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 2,
  "verifiedBot": false,
  "origin": "",
  "ip": "198.51.100.43",
  "country": "US",
  "threatScore": 15
 },
 {
  "id": "req-26",
  "method": "POST",
  "path": "/blog/post",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 52,
  "verifiedBot": true,
  "origin": "https://evil-30.example",
  "ip": "58.210.123.195",
  "country": "SG",
  "threatScore": 26
 },
 {
  "id": "req-27",
  "method": "GET",
  "path": "/blog/post",
  "ua": "UptimeMonitor/1.2",
  "botScore": 84,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "198.51.100.43",
  "country": "BR",
  "threatScore": 58
 },
 {
  "id": "req-28",
  "method": "POST",
  "path": "/login",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 59,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "12.220.5.47",
  "country": "IN",
  "threatScore": 59
 },
 {
  "id": "req-29",
  "method": "GET",
  "path": "/blog/post",
  "ua": "python-httpx/0.28.1",
  "botScore": 51,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "56.119.4.5",
  "country": "DE",
  "threatScore": 23
 },
 {
  "id": "req-30",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 98,
  "verifiedBot": true,
  "origin": "https://evil-67.example",
  "ip": "150.169.110.254",
  "country": "IN",
  "threatScore": 57
 },
 {
  "id": "req-31",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "curl/8.6.0",
  "botScore": 28,
  "verifiedBot": false,
  "origin": "",
  "ip": "43.82.122.236",
  "country": "DE",
  "threatScore": 41
 },
 {
  "id": "req-32",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 29,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "35.97.34.233",
  "country": "SG",
  "threatScore": 32
 },
 {
  "id": "req-33",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 83,
  "verifiedBot": false,
  "origin": "",
  "ip": "97.154.37.3",
  "country": "US",
  "threatScore": 44
 },
 {
  "id": "req-34",
  "method": "GET",
  "path": "/blog/post",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 27,
  "verifiedBot": true,
  "origin": "https://app-312.example",
  "ip": "190.81.78.23",
  "country": "DE",
  "threatScore": 37
 },
 {
  "id": "req-35",
  "method": "GET",
  "path": "/admin/settings",
  "ua": "python-httpx/0.28.1",
  "botScore": 96,
  "verifiedBot": false,
  "origin": "https://evil-71.example",
  "ip": "165.42.157.152",
  "country": "SG",
  "threatScore": 53
 },
 {
  "id": "req-36",
  "method": "GET",
  "path": "/admin/settings",
  "ua": "python-httpx/0.28.1",
  "botScore": 55,
  "verifiedBot": false,
  "origin": "https://evil-21.example",
  "ip": "70.167.0.87",
  "country": "US",
  "threatScore": 15
 },
 {
  "id": "req-37",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "UptimeMonitor/1.2",
  "botScore": 63,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "125.33.123.95",
  "country": "IN",
  "threatScore": 60
 },
 {
  "id": "req-38",
  "method": "POST",
  "path": "/api/v2/search",
  "ua": "UptimeMonitor/1.2",
  "botScore": 55,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "120.203.58.109",
  "country": "US",
  "threatScore": 0
 },
 {
  "id": "req-39",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "UptimeMonitor/1.2",
  "botScore": 55,
  "verifiedBot": false,
  "origin": "https://evil-66.example",
  "ip": "203.0.113.26",
  "country": "US",
  "threatScore": 6
 },
 {
  "id": "req-40",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "python-httpx/0.28.1",
  "botScore": 27,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "31.68.48.216",
  "country": "DE",
  "threatScore": 27
 },
 {
  "id": "req-41",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 44,
  "verifiedBot": true,
  "origin": "https://app-312.example",
  "ip": "203.0.113.26",
  "country": "US",
  "threatScore": 33
 },
 {
  "id": "req-42",
  "method": "GET",
  "path": "/login",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 45,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "198.51.100.43",
  "country": "BR",
  "threatScore": 36
 },
 {
  "id": "req-43",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "curl/8.6.0",
  "botScore": 49,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "141.234.13.113",
  "country": "BR",
  "threatScore": 48
 },
 {
  "id": "req-44",
  "method": "GET",
  "path": "/admin/settings",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 3,
  "verifiedBot": false,
  "origin": "https://evil-51.example",
  "ip": "163.197.86.201",
  "country": "US",
  "threatScore": 53
 },
 {
  "id": "req-45",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 95,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "147.16.8.75",
  "country": "DE",
  "threatScore": 50
 },
 {
  "id": "req-46",
  "method": "GET",
  "path": "/login",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 45,
  "verifiedBot": true,
  "origin": "https://app-312.example",
  "ip": "135.135.106.101",
  "country": "BR",
  "threatScore": 2
 },
 {
  "id": "req-47",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "UptimeMonitor/1.2",
  "botScore": 38,
  "verifiedBot": true,
  "origin": "https://app-312.example",
  "ip": "45.45.228.45",
  "country": "SG",
  "threatScore": 4
 },
 {
  "id": "req-48",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 26,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "27.17.36.205",
  "country": "DE",
  "threatScore": 14
 },
 {
  "id": "req-49",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "UptimeMonitor/1.2",
  "botScore": 54,
  "verifiedBot": false,
  "origin": "https://evil-36.example",
  "ip": "203.0.113.26",
  "country": "DE",
  "threatScore": 31
 },
 {
  "id": "req-50",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "curl/8.6.0",
  "botScore": 40,
  "verifiedBot": false,
  "origin": "",
  "ip": "198.51.100.43",
  "country": "US",
  "threatScore": 16
 },
 {
  "id": "req-51",
  "method": "GET",
  "path": "/admin/settings",
  "ua": "curl/8.6.0",
  "botScore": 63,
  "verifiedBot": true,
  "origin": "https://app-312.example",
  "ip": "98.51.114.43",
  "country": "IN",
  "threatScore": 55
 },
 {
  "id": "req-52",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 61,
  "verifiedBot": true,
  "origin": "https://evil-22.example",
  "ip": "110.59.177.199",
  "country": "SG",
  "threatScore": 50
 },
 {
  "id": "req-53",
  "method": "GET",
  "path": "/blog/post",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 54,
  "verifiedBot": false,
  "origin": "https://evil-68.example",
  "ip": "198.51.100.43",
  "country": "SG",
  "threatScore": 7
 },
 {
  "id": "req-54",
  "method": "POST",
  "path": "/api/v2/items",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 35,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "128.231.129.118",
  "country": "DE",
  "threatScore": 45
 },
 {
  "id": "req-55",
  "method": "POST",
  "path": "/admin/settings",
  "ua": "curl/8.6.0",
  "botScore": 58,
  "verifiedBot": false,
  "origin": "https://evil-30.example",
  "ip": "12.186.72.155",
  "country": "BR",
  "threatScore": 0
 },
 {
  "id": "req-56",
  "method": "GET",
  "path": "/blog/post",
  "ua": "python-httpx/0.28.1",
  "botScore": 31,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "99.71.26.139",
  "country": "US",
  "threatScore": 33
 },
 {
  "id": "req-57",
  "method": "POST",
  "path": "/",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 21,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "82.121.238.132",
  "country": "US",
  "threatScore": 40
 },
 {
  "id": "req-58",
  "method": "GET",
  "path": "/login",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 73,
  "verifiedBot": false,
  "origin": "https://app-312.example",
  "ip": "203.0.113.26",
  "country": "IN",
  "threatScore": 16
 },
 {
  "id": "req-59",
  "method": "GET",
  "path": "/blog/post",
  "ua": "curl/8.6.0",
  "botScore": 70,
  "verifiedBot": false,
  "origin": "https://evil-93.example",
  "ip": "140.16.233.107",
  "country": "US",
  "threatScore": 38
 },
 {
  "id": "req-60",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 11,
  "verifiedBot": false,
  "origin": "",
  "ip": "203.0.113.26",
  "country": "IN",
  "threatScore": 18
 }
]
"""
requests = json.loads(requests_data)

class Rule:
    def __init__(self, action, condition):
        self.action = action
        self.condition = condition
    
    def eval(self, req):
        return self.condition(req)

rules_source = [
    ("LOG", lambda r: r['country'] in {"SG", "DE"}),
    ("BLOCK", lambda r: r['path'].startswith("/admin") and r['ip'] not in {"203.0.113.26", "198.51.100.43"}),
    ("BLOCK", lambda r: "curl" in r['ua']),
    ("BLOCK", lambda r: r['method'] == "POST" and r['origin'] != "https://app-312.example"),
    ("BLOCK", lambda r: r['botScore'] < 30),
    ("LOG", lambda r: r['threatScore'] > 56),
    ("BLOCK", lambda r: "python-httpx" in r['ua']),
    ("SKIP", lambda r: r['path'].startswith("/assets/")),
    ("CHALLENGE", lambda r: r['path'] == "/login" and r['threatScore'] > 31),
    ("CHALLENGE", lambda r: r['path'].startswith("/api") and r['botScore'] < 40),
    ("LOG", lambda r: r['method'] == "GET"),
    ("BLOCK", lambda r: "/.git" in r['path'] or "/.env" in r['path']),
    ("LOG", lambda r: r['country'] in {"US", "SG"}),
    ("BLOCK", lambda r: r['path'].startswith("/admin") and r['ip'] not in {"203.0.113.26", "198.51.100.43"}),
    ("BLOCK", lambda r: "curl" in r['ua']),
    ("SKIP", lambda r: r['verifiedBot'] == True),
    ("BLOCK", lambda r: r['method'] == "POST" and r['origin'] != "https://app-312.example"),
    ("LOG", lambda r: r['threatScore'] > 58),
    ("BLOCK", lambda r: "python-httpx" in r['ua']),
    ("SKIP", lambda r: r['path'].startswith("/assets/")),
    ("CHALLENGE", lambda r: r['path'] == "/login" and r['threatScore'] > 32),
    ("LOG", lambda r: r['method'] == "GET"),
    ("BLOCK", lambda r: "/.git" in r['path'] or "/.env" in r['path']),
    ("LOG", lambda r: r['country'] in {"US", "BR"}),
    ("BLOCK", lambda r: r['path'].startswith("/admin") and r['ip'] not in {"203.0.113.26", "198.51.100.43"}),
    ("BLOCK", lambda r: "curl" in r['ua']),
    ("BLOCK", lambda r: r['method'] == "POST" and r['origin'] != "https://app-312.example"),
    ("LOG", lambda r: r['threatScore'] > 47),
    ("BLOCK", lambda r: "python-httpx" in r['ua']),
    ("SKIP", lambda r: r['path'].startswith("/assets/")),
    ("CHALLENGE", lambda r: r['path'] == "/login" and r['threatScore'] > 25),
    ("LOG", lambda r: r['method'] == "GET"),
    ("BLOCK", lambda r: "/.git" in r['path'] or "/.env" in r['path'])
]

def eval_req(req, rules):
    for i, (action, cond) in enumerate(rules):
        if cond(req):
            if action in ["BLOCK", "CHALLENGE", "SKIP"]:
                return action
    return "ALLOW"

def run_scenario(rules):
    count = 0
    reaches = []
    for req in requests:
        res = eval_req(req, rules)
        if res in ["SKIP", "ALLOW"]:
            count += 1
            reaches.append(req['id'])
    return count, reaches

c1, r1 = run_scenario(rules_source)

rules_p2 = list(rules_source)
rules_p2[9], rules_p2[15] = rules_p2[15], rules_p2[9] # 0-indexed, so 10->9, 16->15
c2, r2 = run_scenario(rules_p2)

diff = list(set(r1) ^ set(r2))

rules_p3 = list(rules_source)
rules_p3[4] = ("BLOCK", lambda r: r['botScore'] < 30 and not r['verifiedBot'])
c3, r3 = run_scenario(rules_p3)

print(f"{c1}|{diff[0]}|{c3}")
