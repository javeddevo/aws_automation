import sys
try:
    import boto3
    print("successfully imported boto3")
except Exception as e:
    print(e)
    print("plz install the module boto3")
ami_re=boto3.resource('iam')
for each in ami_re.users.all():
    print(each,each.create_date)
    #print(dir(each))
