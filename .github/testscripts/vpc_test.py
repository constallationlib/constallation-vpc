import constellation_vpc as vpc

testsubnet = vpc.VPC(region="us-west-2", vpc_id="vpc-08ed1a1cd357c0dab", aws_access_key=)
for x in testsubnet.subnets:
    print(x)

