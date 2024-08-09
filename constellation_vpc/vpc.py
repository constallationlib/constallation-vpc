from _vpc import _vpc

class VPC(_vpc):
    def __init__(self, region:str, vpc_id:str=None, aws_access_key:str=None, aws_access_secret_key:str=None, vpc_cidr_block:str=None):
        self._vpc_id = vpc_id
        self._region = region
        self._aws_access_key = aws_access_key
        self._aws_access_secret_key = aws_access_secret_key
        self._vpc_cidr_block = vpc_cidr_block
