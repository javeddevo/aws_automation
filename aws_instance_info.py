import boto3
ec2_ob_re=boto3.resource('ec2')
#print(dir(ec2_ob_re)for all operations
for each in ec2_ob_re.instances.all():
    #print(dir(ec2_ob_re.instances.all()))
    print(each.state,each.key_name)
    
