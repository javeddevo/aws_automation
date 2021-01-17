import boto3
#to work with particular iam user you have pass session)
session=boto3.Session(profile_name="deepika",region_name="us-east-1")
ec2_con_re=session.resource("ec2")
for each in ec2_con_re.instances.all():
    print(each)
