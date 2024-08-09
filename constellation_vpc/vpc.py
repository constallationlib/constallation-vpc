    def describe_vpc(self, vpc_id: str = None) -> dict:
        if vpc_id:
            return super()._describe_vpc(vpc_id)
        return super()._describe_vpc(self._vpc_id)

    def create_vpc(self, cidr_block: str) -> dict:
        vpc = super()._create_vpc(cidr_block)
        if "Error" in vpc:
            raise Exception(vpc["Error"])
        return vpc

    def delete_vpc(self, vpc_id: str = None) -> dict:
        if vpc_id:
            return super()._delete_vpc(vpc_id)
        return super()._delete_vpc(self._vpc_id)

    def associate_vpc_cidr_block(self, cidr_block: str, vpc_id: str = None) -> dict:
        if vpc_id is None:
            vpc_id = self._vpc_id
        return super()._associate_vpc_cidr_block(vpc_id, cidr_block)

    def disassociate_vpc_cidr_block(self, association_id: str) -> dict:
        return super()._disassociate_vpc_cidr_block(association_id)

    def modify_vpc_attribute(self, attribute_name: str, attribute_value) -> dict:
        return super()._modify_vpc_attribute(self._vpc_id, attribute_name, attribute_value)

    def describe_vpc_cidr_reservations(self) -> dict:
        return super()._describe_vpc_cidr_reservations(self._vpc_id)

    def create_subnet(self, cidr_block: str, availability_zone: str) -> dict:
        return super()._create_subnet(self._vpc_id, cidr_block, availability_zone)

    def delete_subnet(self, subnet_id: str) -> dict:
        return super()._delete_subnet(subnet_id)

    def describe_subnet(self, subnet_id: str) -> dict:
        return super()._describe_subnet(subnet_id)

    def modify_subnet_attribute(self, subnet_id: str, attribute_name: str, attribute_value) -> dict:
        return super()._modify_subnet_attribute(subnet_id, attribute_name, attribute_value)

if __name__ == '__main__':
    vpc = VPC('us-west-2', vpc_id="vpc-017f9600d16474436")
    print(vpc.describe_vpc())