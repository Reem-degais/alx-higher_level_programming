#!/bin/bash
# displays only the status code of the response
curl -sLX HEAD -w "%{http_code}" "$1"
