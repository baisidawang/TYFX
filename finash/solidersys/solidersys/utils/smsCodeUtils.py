import requests
class SMSCode(object):
	"""docstring for SMSCode"""
	def __init__(self, api_key):
		self.api_key = api_key
		self.single_send_url='HTTP://sms.yunpian.com/v2/sms/single_send.json'
	def send_sms(self,code,mobile):
		# parmas={
		# 'apikey':self.api_key,
		# 'mobile':mobile,
		# 'text':"验证码是{code}".format(code=code)
		# }
		# r=requests.post(self.single_send_url,data=parmas)
		# print(r)
		return {"code":"3333"}
	
if __name__=="__main__":
	smscodeU=SMSCode('b29e83ce649aea5951aa33935a7db9ab')
	smscodeU.send_sms('1234', '13591995551')