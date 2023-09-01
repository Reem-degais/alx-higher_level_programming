#!/bin/bash
# displays only the status code of the response
curl -LsX HEAD -w "%{http_code}" "$1"
