#!/usr/bin/env python
"""
 monitor_mbusd: Monitor Home Assistant and restart mbusd if not updating.

 Author: Louis Rossouw
"""

from config_defaults import *
from config import *
from requests import get
from time import sleep
from pprint import pprint
import subprocess

api_url = HA_URL + "api/"
state_url = HA_URL + "api/states/" + HA_ENTITY_ID
bearer_token = "Bearer {}".format(HA_API_KEY)

headers = {
    "Authorization": bearer_token,
    "content-type": "application/json",
}


def get_state(api_url, state_url, headers):
    try:
        response = get(url=api_url, headers=headers)
        data = response.json()
        if data["message"] == "API running.":
            response = get(url=state_url, headers=headers)
            data = response.json()
            return data["state"]
        else:
            return "unknown"
    except:
        return "unknown"


while True:
    state = get_state(api_url, state_url, headers)
    if state == "on":
        try:
            subprocess.run(["systemctl", "restart", MBUSD_SERVICE_NAME])
        except:
            pass
        sleep(RESTART_POLL_INTERVAL)
    else:
        sleep(POLL_INTERVAL)
