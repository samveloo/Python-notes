import os

DIRECTORY = "NOT-MY-PROJECT"

repo_urls = [
    'https://github.com' # repository links
]

os.chdir(DIRECTORY)

for url in repo_urls:
    result = os.system(f'git clone {url}')

    if result == 0:
        print('Repository successfully added')
    else:
        print(f'Failed to clone repository: {url}')