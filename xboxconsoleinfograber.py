import requests
import json
a=requests.get("https://192.168.0.21:11443/api/os/devicefamily", verify=False)
b=requests.get("https://192.168.0.21:11443/api/os/machinename", verify=False)
c=requests.get("https://192.168.0.21:11443/ext/xbox/info", verify=False)
d=requests.get("https://192.168.0.21:11443/ext/xboxlive/sandbox", verify=False)
loaded_json = json.loads(a.text)
for x in loaded_json:
	print("%s : %s" % (x, loaded_json[x]))

loaded_json = json.loads(b.text)
for x in loaded_json:
	print("%s : %s" % (x, loaded_json[x]))

loaded_json = json.loads(c.text)
for x in loaded_json:

	print("%s : %s" % (x, loaded_json[x]))
loaded_json = json.loads(d.text)
for x in loaded_json:
	print("%s : %s" % (x, loaded_json[x]))
