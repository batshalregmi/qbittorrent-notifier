###############################

PUSHOVER_APP_TOKEN = "YOUR_APP_TOKEN_HERE"
PUSHOVER_USER      = "YOUR_USER_KEY_HERE"

##############################

import sys
import http.client, urllib
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": PUSHOVER_APP_TOKEN,
    "user": PUSHOVER_USER,
    "message": sys.argv[1],
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()