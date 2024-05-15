from datetime import date, time , datetime
class Param(object):
	def __init__(self):
		self.propertyName = ""
		self.propertyValue = ""
		self.operator = ""
		self.params=[]

	def add(self,propertyName,propertyValue,operator='eq'):
		param=Param()
		param.propertyName=propertyName
		param.propertyValue=propertyValue
		param.operator=operator
		self.params.append(param)

	def create(self):
		filter_dict=dict()
		for i in range(len(self.params)):
			if self.params[i].propertyValue:
				if self.params[i].operator=="eq":
					filter_dict[self.params[i].propertyName]=self.params[i].propertyValue
				elif self.params[i].operator=="gt":
					filter_dict[self.params[i].propertyName+"__gt"]=self.params[i].propertyValue
				elif self.params[i].operator=="gte":
					filter_dict[self.params[i].propertyName+"__gte"]=self.params[i].propertyValue
				elif self.params[i].operator=="lt":
					filter_dict[self.params[i].propertyName+"__lt"]=self.params[i].propertyValue
				elif self.params[i].operator=="lte":
					filter_dict[self.params[i].propertyName+"__lte"]=self.params[i].propertyValue
				elif self.params[i].operator=="like":
					filter_dict[self.params[i].propertyName+"__icontains"]=self.params[i].propertyValue
		return filter_dict
#User.objects.filter().exclude(age=10)
# __startswith 以…开头
# __istartswith 以…开头 忽略大小写
# __endswith 以…结尾
# __iendswith 以…结尾，忽略大小写
# __isnull
def model_to_dict(model_obj, ignore=()):
    '''
    将一个model对象转换成字典
    '''
    att_dict = {}
    for field in model_obj._meta.fields:
        name = field.attname                 # 获取字段名
        value = getattr(model_obj, name)      #获取对象属性
        if name in ignore:
            continue
        # print(name,value)
        #检查传入的数据能否被序列化
        if isinstance(value, (datetime, date,time)):
            att_dict[name] = str(value)               #生成字典
    return att_dict

def saveLog(obj,uid,tbname):
	obj.save()
	log=Log()
	log.uid=uid
	log.time=datetime.now()
	log.tbname=tbname
	log.save()