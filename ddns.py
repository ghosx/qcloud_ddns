import requests
import json
import time
import os

class DDNS:
	def __init__(self,Id,Token):
		self.login_token=str(Id)+","+str(Token)
		self.format="json"
		self.lang="cn"
		self.headers={"User-Agent":"ddns_for_raspberry_pi/0.1(heeeepin@gmail.com)"}
		self.api='https://dnsapi.cn/'
		self.ip='http://members.3322.org/dyndns/getip'
		self.data={"login_token":self.login_token,"format":self.format,"lang":self.lang}
		self.path=os.path.dirname(os.path.realpath(__file__))
		self.domain_list=self.load()

	def load(self):
		file=self.path+'/config.json'
		with open(file,'r') as f:
			data=json.load(f)
		return data

	def get_new_ip(self):
		return requests.get(url=self.ip).text

	def get_record_list(self):
		url=self.api+"Record.List"
		res = []
		for i in self.domain_list:
			data=self.data.copy()
			data.update({"domain":i[0]})
			r=json.loads(requests.post(url=url,data=data,headers=self.headers).text)
			for j in r["records"]:
				if (j["type"]=="A" and j["name"] in i):
					j["domain"]=i[0]
					res.append(j)
		return res

	def update(self):
		url=self.api+"Record.Modify"
		record=self.get_record_list()
		new_ip=self.get_new_ip()
		new_ip=str(new_ip).strip()
		for i in record:
			if(i["value"]==new_ip):
				log = "%s.%s 指向的ip地址未发生变化" %(i["name"],i["domain"])
				self.write_log(log)
				continue
			d=self.data.copy()
			d.update({"domain":i["domain"],"record_id":i["id"],"sub_domain":i["name"],"record_type":"A","record_line":i["line"],"value":new_ip})
			r=json.loads(requests.post(url=url,data=d,headers=self.headers).text)
			if (r["status"]["code"]=="1"):
				log = "%s.%s 成功被指向新的ip地址：%s" % (i["name"],i["domain"],new_ip)
			else:
				log = r["status"]["message"]
			self.write_log(log)

	def write_log(self,content):
		t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		content=t+"\t"+content+"\n"
		file=self.path+'/result.log'
		with open(file,"a+") as f:
			f.write(content)
