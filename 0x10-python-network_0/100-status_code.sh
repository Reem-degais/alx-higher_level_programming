#!/bin/bash
# displays only the status code of the response
curl -s -L -X HEAD -w "%{http-code}" "$1"
