from _vpc import _vpc

class VPC(_vpc):
    def __init__(self, region:str, vpc_id:str=None, aws_access_key:str=None, aws_access_secret_key:str=None, aws_session_token:str=None, vpc_cidr_block:str=None):
        self._vpc_id = vpc_id
        self._region = region
        self._aws_access_key = aws_access_key
        self._aws_access_secret_key = aws_access_secret_key
        self._aws_sts_token = aws_session_token
        self._vpc_cidr_block = vpc_cidr_block
        super().__init__(region=region, aws_access_key=self._aws_access_key, aws_access_secret_key=self._aws_access_secret_key, aws_sts_session_token=self._aws_sts_token)
        del self._aws_sts_token, self._aws_access_key, self._aws_access_secret_key

    def _initialize_vpc(self):
        if self._vpc_id is not None:
            print(super()._describe_vpc(self._vpc_id))

if __name__ == '__main__':
vpc = VPC('us-east-1')