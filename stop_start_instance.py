import sys
try:
    import boto3
    print("Successfully imported")
except Exception as e:
    print(e)
    print("plz install boto3 module")
    sys.exit(1)
ec2_re=boto3.resource("ec2")
my_req=ec2_re.Instance("i-055efa620e660f477")#(for particular instance)
#print(my_req.state["Name"])


def ec2_re(region_="us-east-1"):
    return boto3.resource("ec2",region_name=region_)
def ec2_cli(region_="us-east-1"):
    return boto3.client("ec2",region_name=region_)

def usage(args):
    if len(sys.argv)!=3:
        print("plz pass the command line arguments as follows:")
        print(args[0],"region","instance-id")
        sys.exit(2)
    return None
def validate_given_region(region_name):
    client=ec2_cli()
    my_region=[]
    for each in client.describe_regions()["Regions"]:
        my_region.append(each["RegionName"])
    #print(my_region)
    if not region_name in my_region:
        print("plz pass the proper region name")
        sys.exit(3)
def validate_given_instances(region_name,instance_id):
    re=ec2_re(region_name)
    id_name=[]
    for each in re.instances.all():
        id_name.append(each.id)
        #print(id_name)
    if not instance_id in id_name:
        print("plz pass the id name correct")
        sys.exit(4)
def start_ec2(r_n,i_d):
    my_op=ec2_re(r_n)
    my_par=my_op.Instance(i_d)
    current_state=my_par.state["Name"]
    if current_state=="stopped":
        print("your cuttent status is : stopped and we are running out instance wait....")
        my_par.start()
        my_par.wait_until_running()#waiters
        print("instances has started")
    #elif current_state!="stopped":
        #my_par.stop()   
def main(args):
    usage(args)
    validate_given_region(args[1])
    validate_given_instances(args[1],args[2])
    start_ec2(args[1],args[2])


if __name__=="__main__":
    main(sys.argv)
