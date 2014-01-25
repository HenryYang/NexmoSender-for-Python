#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

endpoint = 'https://rest.nexmo.com/sms/json'
msg = {
        'reqtype': 'json',
        'api_key': 'ENTER YOUR KEY HERE',
        'api_secret': 'ENTER YOUR SECRET KEY HERE',
        'from': '+886987654321',
        'to': '+886912345678',
        'type': 'unicode',
        'text': 'Hello  安安你好'
      }

r = requests.post(endpoint, data=msg)
