from cli import


def create_repo(repo_name, file_name, file_content):
    headers = {"Accept": "application/vnd.github.v3+json", "Authorization": f"token {TOKEN}"}
    data = {'name': repo_name}
    r = requests.post("https://api.github.com/user/repos", headers=headers, data=json.dumps(data))
    print("Repo created")

    data = {
        'message': 'Initial commit',
        'content': b64encode(file_content.encode('utf-8')).decode('utf-8'),
    }
    response = requests.put(f"https://api.github.com/repos/{USERNAME}/{repo_name}/contents/{file_name}", headers=headers, data=json.dumps(data))
    pprint(response.json())
