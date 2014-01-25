#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import urllib

api_key = "ENTER YOUR KEY HERE"
api_secret = "ENTER YOUR SECRET KEY HERE"
to = "+886987654321"
text = "hello 安安你好"
lg = "zh-cn"
voice = "male"

urlencodetext = urllib.urlencode({'text': text})
requests.post('https://rest.nexmo.com/tts/json?api_key='+api_key+'&api_secret='+api_secret+'&to='+to+'&'+urlencodetext+'&lg='+lg'&voice='+voice)
