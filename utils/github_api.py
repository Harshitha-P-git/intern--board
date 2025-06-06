import requests

def get_github_events(username, token):
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com/users/{username}/events/public"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []
