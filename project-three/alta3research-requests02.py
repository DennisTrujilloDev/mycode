#!/usr/bin/env python3
import requests
from pprint import pprint

URL= "http://0.0.0.0:2225/"

resp= requests.get(URL)

pprint(resp)
