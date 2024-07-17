import requests

repo_owner = "smaugue"
repo_name = "GameBot"
file_path = "Version"
token = "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"

def get_version():
    data = open("Version")
    line = data.readline()
    v, u, p = line.split("=")[1].strip().replace('"', '').replace("'", "").split(".")
    return int(v), int(u), int(p)

def get_github_version(repo_owner: str, repo_name: str, file_path: str, token: str):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.json().get('content', '')
        if content:
            import base64
            decoded_content = base64.b64decode(content).decode('utf-8')
            for line in decoded_content.split("\n"):
                if "VERSION" in line:
                    v, u, p = line.split("=")[1].strip().replace('"', '').replace("'", "").split(".")
                    return int(v), int(u), int(p)
    else:
        response.raise_for_status()
    return None

bv, bu, bp = get_github_version(repo_owner,repo_name, file_path, token)
v,u,p = get_version()

LASTER_VERSION = f"{bv}.{bu}.{bp}"
BOT_VERSION = f"{v}.{u}.{p}"

class Version:

    def cmp(version: str):
        if v < bv:
            return "o"
        if v == bv and u < bu:
            return "o"
        if v == bv and u == bu and p < bp:
            return "o"
        if v > bv:
            return "b"
        if v == bv and u > bu:
            return "b"
        if v == bv and u == bu and p > bp:
            return "b"
        return "j"
    
    def check():
        return Version.cmp(BOT_VERSION)