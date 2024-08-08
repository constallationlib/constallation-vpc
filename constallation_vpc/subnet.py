from _vpc import _vpc

class Subnet(_vpc):
    def __init__(self, region:str, subnet_id:str=None, aws_access_key:str=None, aws_access_secret_key:str=None, aws_sts_session_token:str=None):
        self._subnet_id = subnet_id
        self._region = region
        self._aws_access_key = aws_access_key
        self._aws_access_secret_key = aws_access_secret_key
        self._aws_sts_token = aws_sts_session_token

        super().__init__(region=region, aws_access_key=self._aws_access_key, aws_access_secret_key=self._aws_access_secret_key, aws_sts_session_token=self._aws_sts_token)
        del self._aws_sts_token, self._aws_access_key, self._aws_access_secret_key
        self._initualize_subnet()

    def _initualize_subnet(self):
        if self._subnet_id is not None:
            subnet = super().describe_subnet(self._subnet_id)
            self._availability_zone = subnet.get('AvailabilityZone')
            self._availability_zone_id = subnet.get('AvailabilityZoneId')
            self._available_ip_address_count = subnet.get('AvailableIpAddressCount')
            self._cidr_block = subnet.get('CidrBlock')
            self._default_for_az = subnet.get('DefaultForAz')
            self._map_public_ip_on_launch = subnet.get('MapPublicIpOnLaunch')
            self._map_customer_owned_ip_on_launch = subnet.get('MapCustomerOwnedIpOnLaunch')
            self._state = subnet.get('State')
            self._subnet_id = subnet.get('SubnetId')
            self._vpc_id = subnet.get('VpcId')
            self._owner_id = subnet.get('OwnerId')
            self._assign_ipv6_address_on_creation = subnet.get('AssignIpv6AddressOnCreation')
            self._ipv6_cidr_block_association_set = subnet.get('Ipv6CidrBlockAssociationSet')
            self._subnet_arn = subnet.get('SubnetArn')
            self._enable_dns64 = subnet.get('EnableDns64')
            self._ipv6_native = subnet.get('Ipv6Native')
            self._private_dns_name_options_on_launch = subnet.get('PrivateDnsNameOptionsOnLaunch')


if __name__ == '__main__':
    x = Subnet(region='us-west-2', subnet_id='subnet-0c0036e53c417c552')