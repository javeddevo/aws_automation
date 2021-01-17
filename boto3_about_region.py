import boto3
aws_co=boto3.resource("ec2",region_name="us-east-1")#(by default it will take region_name as argument if u dont provide)
#(you can take region_nme=us-east-1 or us-east-1)
for each in aws_co.instances.all():
    print(each,each.id)
