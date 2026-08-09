import json
with open("index.json", "r") as f:
    data = json.load(f)
targets = {
    "https://data.waterworks.example/notices/audit-749.pdf",
    "https://data.waterworks.example/notices/audit-793.pdf",
    "https://data.waterworks.example/open-data/audit-975.pdf",
    "https://data.waterworks.example/reports/audit-332.pdf",
    "https://docs.waterworks.example/notices/audit-557.pdf",
    "https://docs.waterworks.example/open-data/audit-425.pdf",
    "https://waterworks.example/notices/audit-406.pdf",
    "https://waterworks.example/reports/audit-900.pdf"
}
other_docs = [d for d in data if d["url"] not in targets]

def match_token(d, token):
    token = token.lower()
    neg = token.startswith('-')
    if neg: token = token[1:]
    res = False
    if token.startswith("site:"):
        val = token[5:]
        host = d["host"].lower()
        res = host == val or host.endswith("." + val)
    elif token.startswith("filetype:"):
        res = d["filetype"].lower() == token[9:]
    elif token.startswith("inurl:"):
        res = token[6:] in d["url"].lower()
    elif token.startswith("intitle:"):
        res = token[8:] in d["title"].lower()
    elif token.startswith("intext:"):
        res = token[7:] in d["body"].lower()
    elif token.startswith("after:"):
        res = d["year"] > int(token[6:])
    elif token.startswith("before:"):
        res = d["year"] < int(token[7:])
    else:
        val = token[1:-1] if token.startswith('"') and token.endswith('"') else token
        res = val in d["title"].lower() or val in d["body"].lower()
    return not res if neg else res

def score_query(tokens):
    return [d for d in other_docs if all(match_token(d, t) for t in tokens)]

print(len(score_query(["audit", "filetype:pdf", "evaluation", "-inurl:drafts", "after:2021", "site:waterworks.example"])))
