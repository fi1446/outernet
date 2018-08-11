#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
path = '/path/to/outernet.wav'
# APIキーを差し込む
url = "https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY={}".format("")
files = {"a": open(path, 'rb'), "v":"on"}
r = requests.post(url, files=files)
print (r.json()['text'])
