from _vpc import _vpc

class Subnet(_vpc):
    def __init__(self, region:str, subnet_id:str=None, avalibility_zone:str=None,
                 cidr_block:str=None, ipv6_cidr_block:str=None, vpc_id:str=None,
                 assign_ipv6_address_on_creation:bool=None, map_public_ip_on_creation:bool=None,
                 tags:dict=None, ):
        self._subnet_id = subnet_id
        self._avalibility_zone = avalibility_zone
        self._cidr_block = cidr_block
        self._ipv6_cidr_block = ipv6_cidr_block
        self._vpc_id = vpc_id
        self._assign_ipv6_address_on_creation = assign_ipv6_address_on_creation
        self._map_public_ip_on_creation = map_public_ip_on_creation
        self._tags = tags