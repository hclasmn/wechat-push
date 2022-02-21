#!/usr/bin/env python

import json
import requests
 
class WeChat:
	def __init__(self):
		self.CORPID = 'XXXX' 
		self.CORPSECRET = 'XXXX' 
		self.AGENTID = 'XXXX'  
		self.TOUSER = "XXXX"   
	def _get_access_token(self):
		url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
		values = {'corpid': self.CORPID,
				'corpsecret': self.CORPSECRET,
				}
		req = requests.post(url, params=values)
		return req
 
	def get_access_token(self):
		get_req = self._get_access_token()
		get_req_json = json.loads(get_req.text)
		access_token = get_req_json['access_token']
		return access_token
 
	def send_data(self, message):
		send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.get_access_token()
		send_values = {
			"touser": self.TOUSER,
			"msgtype": "text",
			"agentid": self.AGENTID,
			"text": {
				"content": message
			},
			"safe": ""
		}
		send_msges = json.dumps(send_values, ensure_ascii=False, indent=4).encode('utf-8')
		respone = requests.post(send_url, send_msges)
		respone = respone.json()
		return respone["errmsg"]
 
if __name__ == "__main__":
	wx = WeChat()
	wx.send_data("群发消息")