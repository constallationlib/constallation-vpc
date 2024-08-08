import subprocess as _subprocess

class _vpc:
    def __init__(self, region: str = None, aws_access_key: str = None, aws_access_secret_key: str = None, aws_sts_session_token: str = None):
        self.region_name = region
        self._access_key = aws_access_key
        self._secret_key = aws_access_secret_key
        self._session_token = aws_sts_session_token