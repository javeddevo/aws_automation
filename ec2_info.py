import boto3
import pprint
re_ec2=boto3.resource("ec2")
pprint.pprint(re_ec2)
