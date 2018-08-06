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
		for key in src_data:
			if key in dst_data:
				"""递归"""
				cmp(src_data[key], dst_data[key])
			else:
				print("dst不存在这个key:"+key)
	elif isinstance(src_data, list):
		"""若为list格式"""
		if len(src_data) != len(dst_data):
			print("list len: '{}' != '{}'".format(len(src_data), len(dst_data)))
		for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
			"""递归"""
			cmp(src_list, dst_list)
	else:
		if str(src_data) != str(dst_data):
			print(src_data)

if __name__ == "__main__":
	dict1 = {"id": "504","id2": "504", "name": "班级优化", "info": {"uid":"2017","stuName":["张三","李四","李四2"]}}
	dict2 = {"id": "503","id3": "504", "name": "班级优化2", "info": {"uid":"2017","stuName":["张三","赵五"]}}
	# for key,va in dict2.items():
	# 	print(key,va)
	cmp(dict1,dict2)