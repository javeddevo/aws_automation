#read command line arguments script_name,region,instance-id
#stop
#stop

import sys,pprint
try:
    import boto3
    print("successfully imported boto3")
except Exception as e:
    print(e)
    sys.exit(1)
my_ec2_re=boto3.resource("ec2")
#pprint.pprint(dir(my_ec2_re.Instance("i-055efa620e660f477")))
#my_ins=my_ec2_re.Instance("i-055efa620e660f477")
#print(my_ins.state["Name"])

def  re_ob(region_="us-east-1"):
    return boto3.resource("ec2",region_name=region_)
def client_ob(region_="us-east-1"):
    return boto3.client("ec2",region_name=region_)

def validate_region(region_name):
    client_region=client_ob()
    region=[]
    for each in client_region.describe_regions()["Regions"]:
        region.append(each["RegionName"])
    if not region_name  in region:
      print("plz pass the valid region name")
      sys.exit(3)
def validate_instances(region_name,instance_id):
    ins_ob=re_ob(region_name)
    inst_id=[]
    for each in ins_ob.instances.all():
        inst_id.append(each.id)
    if not instance_id in inst_id:
      print("plz pass valid id")
      sys.exit(4)
def wait_until_run(ec2):
    while True:
       my_state=ec2.state["Name"]
       if my_state=="running":
           break
def validate_ec2(re,inid):
    ob=re_ob(re)
    my_in=ob.Instance(inid)
    current_state=my_in.state["Name"]
    if current_state=="stopped":
        print("your instance is ready to run.....")
        my_in.start()
        wait_unitil_run(my_in)
    
def usage(args):
    if len(args)!=3:
        print("plz pass the arguments as folows:")
        print(args[0],",","instace-id")
        sys.exit(2)
def main(args):
    usage(args)
    validate_region(args[1])
    validate_instances(args[1],args[2])
    validate_ec2(args[1],args[2])

if __name__=="__main__":
    main(sys.argv)
