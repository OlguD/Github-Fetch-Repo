from bs4 import BeautifulSoup
import requests

class GitHubRepo():
    def __init__(self, username):
        self.username = username
        self.url = f'https://github.com/{self.username}?tab=repositories'
    
    def fetchRepo(self):
        global repository
        repository = []
        html = requests.get(self.url)
        soup = BeautifulSoup(html.content, 'html.parser')
        for line in soup.findAll("li", {"itemtype": "http://schema.org/Code"}):
            for repoLink in line.findAll("a", itemprop="name codeRepository"): 
                repository.append(repoLink.text)
        rep = []
        for x in repository:
            rep.append(x.replace("\n", ""))

        new_REPOSITORY = []
        for k in rep:
            new_REPOSITORY.append(k.replace("        ",""))

        try:
            new_REPOSITORY.remove('  config')
            new_REPOSITORY.remove('  github-config')
        except ValueError:
            pass
        
        print(f"{self.username} Repository")
        
        for k in enumerate(new_REPOSITORY, 1):
            print(k)

if __name__ == "__main__":
    username = str(input("GitHub Username: "))
    github = GitHubRepo(username)
    work_co = github.fetchRepo()
    print(work_co)

