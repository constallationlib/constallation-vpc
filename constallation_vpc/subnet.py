from _vpc import _vpc

class Subnet(_vpc):
    def __init__(self, region:str, subnet_id:str=None, avalibility_zone:str=None,
                 cidr_block:str=None, ipv6_cidr_block:str=None, vpc_id:str=None,
                 assign_ipv6_address_on_creation:bool=None, map_public_ip_on_creation:bool=None,
                 tags:dict=None, aws_access_key:str=None, aws_access_secret_key:str=None, aws_sts_session_token:str=None):
        self._subnet_id = subnet_id
        self._avalibility_zone = avalibility_zone
        self._cidr_block = cidr_block
        self._ipv6_cidr_block = ipv6_cidr_block
        self._vpc_id = vpc_id
        self._assign_ipv6_address_on_creation = assign_ipv6_address_on_creation
        self._map_public_ip_on_creation = map_public_ip_on_creation
        self._tags = tags

        self._region = region
        self._aws_access_key = aws_access_key
        self._aws_access_secret_key = aws_access_secret_key
        self._aws_sts_token = aws_sts_session_token

        super().__init__(region=region, aws_access_key=self._aws_access_key, aws_access_secret_key=self._aws_access_secret_key, aws_sts_session_token=self._aws_sts_token)
        del self._aws_sts_token, self._aws_access_key, self._aws_access_secret_key
        self._initualize_subnet()

    def _initualize_subnet(self):
        if self._subnet_id is not None:
            super().describe_subnet(self._subnet_id)


if __name__ == '__main__':
    x = Subnet(region='us-west-1', subnet_id='subnet-0c0036e53c417c552')