#!/usr/bin/env python

# Home Assistant Things
HA_URL = "https://homeassistant.local/"
HA_ENTITY_ID = "binary_sensor.sunsynk_serial_data"
HA_API_KEY = "my_key"

# Time between polls
POLL_INTERVAL = 10  # seconds
# Sleep longer after restart
RESTART_POLL_INTERVAL = 360  # seconds

# MBUSD Service
MBUSD_SERVICE_NAME = "mbusd@ttyUSB0.service"
