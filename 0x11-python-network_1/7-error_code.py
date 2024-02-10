#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
and displays the body of the response. If the HTTP status code is greater than
or equal to 400, will print Error code: followed by the HTTP status code"""

if __name__ == '__main__':
    import sys
    import requests
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
