import constellation_vpc as vpc

testsubnet = vpc.VPC(region="us-west-2", vpc_id="vpc-08ed1a1cd357c0dab", aws_access_key="ASIASL5DHQSM5TADKAPU", aws_access_secret_key="PV4Coyrj6S/6rOJch9S4O4wGM5IVqr9/daUGxAaR")
for x in testsubnet.subnets:
    print(x)