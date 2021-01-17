import boto3
#ec2_con_re=boto3.resource("ec2")
ec2_con_cli=boto3.client("ec2")#(you have to use client for each operation you cant fing regions in trsource mrthod)
#print(dir(ec2_con_cli))
for each in ec2_con_cli.describe_regions()['Regions']:
    print(each['RegionName'])
