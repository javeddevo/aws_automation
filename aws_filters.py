import boto3
ec2_re=boto3.resource("ec2","us-east-1")
f1={"Name":"instance-type" , "Values":["t2-micro"]}
#f2={"Name":"key-name" , "Values":["ch"]}
#f3={"Name":"instance-state-name","Values":["stopped"]}
for each in ec2_re.instances.filter(Filters=[f1]):
    print(each.state["Name"],each.id)
    
