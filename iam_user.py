import boto3
import pprint
iam_re=boto3.resource("iam")

#pprint.pprint(dir(iam_re))
for each in iam_re.users.all():
    print(each)
