#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and 
displays the value of the X-Request-Id"""

import urllib
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        r = respons.Request-Id()
        print(r)
