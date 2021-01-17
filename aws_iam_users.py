import subprocess as sp
import json
cmd="aws iam list-users --output json"
out=sp.Popen(cmd,shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
output=out.wait()
o,e=out.communicate()
out_dic=json.loads(o)
for each in out_dic["Users"]:
    print(each["UserName"])
