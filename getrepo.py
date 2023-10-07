import requests

def get_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repos = response.json()
        repo_names = [repo['name'] for repo in repos]
        return repo_names
    else:
        print("Error:", response.status_code)
        return None

if __name__ == "__main__":
    github_username = str(input("Enter Username: "))

    repo_names = get_user_repositories(github_username)
    if repo_names:
        for repo_name in repo_names:
            print(repo_name)
    else:
        print("Failed to retrieve repository names.")
