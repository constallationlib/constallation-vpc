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
            print(super().describe_subnet(self._subnet_id))


if __name__ == '__main__':
    x = Subnet(region='us-west-2', subnet_id='subnet-0c0036e53c417c552')