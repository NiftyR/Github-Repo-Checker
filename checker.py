import asyncio, requests
from settings import *

class Checker():

    async def GetGithubRepo():
        while True:
            req = requests.get(f"https://api.github.com/users/{github_username}/repos").json() 
            print(req)
            counter = 0
            try:
                while(req[counter] != None):
                    curRepo = req[counter]
                    currentRepos.append({"id": curRepo["id"], "name": curRepo["name"], "fullName": curRepo["full_name"], "url": curRepo["html_url"], "stars": curRepo["stargazers_count"], "watchers": curRepo["watchers_count"], "language": curRepo["language"], "issues": curRepo["open_issues"]})
                    counter+=1
            except Exception:
                pass
            await asyncio.sleep(120)
            currentRepos.clear()


    def Start_Task():
        asyncio.run(Checker.GetGithubRepo())
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(Checker.GetGithubRepo)