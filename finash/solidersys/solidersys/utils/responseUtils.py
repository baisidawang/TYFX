from django.shortcuts import HttpResponse
import json
def responseJson(msg,status,data={}):
	data={'msg':msg,'status':status,'data':data,}
	return HttpResponse(json.dumps(data, ensure_ascii=False),
		content_type="application/json,charset=utf-8")
