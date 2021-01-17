import boto3
import pprint
re_ob=boto3.resource("ec2")
pprint.pprint(dir(re_ob))
