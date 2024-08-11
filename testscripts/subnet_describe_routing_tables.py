from constellation_vpc import Subnet

STS_ACCESS_KEY = ("ASIASL5DHQSMRVD5SPSL", "/W2Ee8JLw0+ogAHd0/ZVblsv7cuvns2285wOBNhp")
SUBNET_ID = "subnet-00c83ee308bb6cfe1"

S = Subnet(region="us-west-2", subnet_id=SUBNET_ID, aws_access_key=STS_ACCESS_KEY[0], aws_access_secret_key=STS_ACCESS_KEY[1])
S.describe_route_tables()