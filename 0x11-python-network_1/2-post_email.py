#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'emial': sys.argv[2]}

    data = urllib.parse.urlencode(values).encode()
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        r = response.read().decode('utf8')
    print("Your email is: {}".format(r))
