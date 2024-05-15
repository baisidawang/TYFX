import hashlib
import time
def md5(user):
	ctime=str(time.time())
	m=hashlib.md5(bytes(user,encoding='utf-8'))
	m.update(bytes(ctime,encoding='utf-8'))
	return m.hexdigest()
def signMd5(msg):
	m=hashlib.md5(bytes(msg,encoding='utf-8'))
	return m.hexdigest()