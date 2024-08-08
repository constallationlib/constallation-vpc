class SubnetError(Exception):
    pass

class SubnetNotFoundError(SubnetError):
    def __init__(self, subnet_id, region):
        super().__init__(f"Subnet {subnet_id} not found in region: {region}")