#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    import urllib.request
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(f"Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('UTF-8')}")
