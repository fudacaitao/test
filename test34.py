# -*- coding:utf-8 -*-
"""
@desc: 
"""
__author__ = 'caitao'
def cmp(src_data,dst_data):
	
	if isinstance(src_data, dict):
		"""若为dict格式"""
		for key,val in dst_data.items():
			if key not in src_data:
				print("src不存在这个key:"+key+":"+val)
			elif key in src_data:
				if (dst_data[key] == src_data[key]):
					pass
				else:
					print(str(key) +":"+ str(dst_data[key]))
			else:
				print("dst不存在这个key:"+key)


if __name__ == "__main__":
	dict1 = {"id": "504","id2": "504", "name": "班级优化", "info": {"uid":"2017","stuName":["张三","李四","李四2"]}}
	dict2 = {"id": "503","id3": "504", "name": "班级优化2", "info": {"uid":"2017","stuName":["张三","赵五"]}}
	# for key,va in dict2.items():
	# 	print(key,va)
	cmp(dict1,dict2)