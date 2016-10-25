#!/usr/bin/python3
from pylgtv import WebOsClient
import sys

try:
    ip = sys.argv[1]
    msg = sys.argv[2]
except:
    print("Usage : %s <ip> <msg>"%(sys.argv[0]))
    exit(-1)
webos_client = WebOsClient(ip)
webos_client.send_message(msg)
