#!/usr/bin/python3
"""challenge to get commits"""


if __name__ == "__main__":
    import sys
    from requests import get, auth

    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        req = get(url)
        json_o = req.json()
        for i in range(0, 10):
            print("{}: {}".format(json_o[i].get('sha'), json_o[i].get('commit')
                                  .get('author').get('name')))
    except Exception:
        pass
