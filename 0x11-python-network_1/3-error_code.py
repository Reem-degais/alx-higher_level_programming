#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
  req = Request(argv[1])
  try:
      response = urlopen(req)
  except HTTPError as e:
      print('Error code: ', e.code)
