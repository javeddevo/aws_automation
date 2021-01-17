import boto3
s3_con=boto3.resource('s3')
for each in s3_con.buckets.all():
    print(each,each.creation_date)
