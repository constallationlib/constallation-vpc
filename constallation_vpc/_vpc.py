import subprocess as _subprocess

class _vpc:
    def __init__(self, region: str = None, aws_access_key: str = None, aws_access_secret_key: str = None, aws_sts_session_token: str = None):
        self.region_name = region
        self._access_key = aws_access_key
        self._secret_key = aws_access_secret_key
        self._session_token = aws_sts_session_token

    def describe_subnet(self, subnet_id: str) -> str:
        cmd = [
            "aws", "ec2", "describe-subnets",
            "--subnet-ids", subnet_id,
            "--region", self.region_name
        ]

        if self._access_key and self._secret_key:
            cmd.extend(["--aws-access-key-id", self._access_key])
            cmd.extend(["--aws-secret-access-key", self._secret_key])

        if self._session_token:
            cmd.extend(["--aws-session-token", self._session_token])

        process = _subprocess.Popen(cmd, stdout=_subprocess.PIPE, stderr=_subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            return f"Error: {stderr}"
        return stdout
