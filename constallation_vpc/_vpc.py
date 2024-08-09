import subprocess as _subprocess
import json


class _vpc:
    def __init__(self, region: str = None, aws_access_key: str = None, aws_access_secret_key: str = None,
                 aws_sts_session_token: str = None):
        self.region_name = region
        self._access_key = aws_access_key
        self._secret_key = aws_access_secret_key
        self._session_token = aws_sts_session_token

    def _run_aws_command(self, cmd: list) -> dict:
        if self._access_key and self._secret_key:
            cmd.extend(["--aws-access-key-id", self._access_key])
            cmd.extend(["--aws-secret-access-key", self._secret_key])

        if self._session_token:
            cmd.extend(["--aws-session-token", self._session_token])

        process = _subprocess.Popen(cmd, stdout=_subprocess.PIPE, stderr=_subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            return {"Error": stderr}

        try:
            return json.loads(stdout)
        except json.JSONDecodeError:
            return {"Error": "Failed to parse JSON output"}

    def _describe_subnet(self, subnet_id: str) -> dict:
        cmd = [
            "aws", "ec2", "describe-subnets",
            "--subnet-ids", subnet_id,
            "--region", self.region_name
        ]
        data = self._run_aws_command(cmd)

        if "Error" in data:
            return data

        try:
            subnet_info = data['Subnets'][0]
            return {
                "AvailabilityZone": subnet_info.get("AvailabilityZone"),
                "AvailabilityZoneId": subnet_info.get("AvailabilityZoneId"),
                "AvailableIpAddressCount": subnet_info.get("AvailableIpAddressCount"),
                "CidrBlock": subnet_info.get("CidrBlock"),
                "DefaultForAz": subnet_info.get("DefaultForAz"),
                "MapPublicIpOnLaunch": subnet_info.get("MapPublicIpOnLaunch"),
                "MapCustomerOwnedIpOnLaunch": subnet_info.get("MapCustomerOwnedIpOnLaunch"),
                "State": subnet_info.get("State"),
                "SubnetId": subnet_info.get("SubnetId"),
                "VpcId": subnet_info.get("VpcId"),
                "OwnerId": subnet_info.get("OwnerId"),
                "AssignIpv6AddressOnCreation": subnet_info.get("AssignIpv6AddressOnCreation"),
                "Ipv6CidrBlockAssociationSet": subnet_info.get("Ipv6CidrBlockAssociationSet"),
                "SubnetArn": subnet_info.get("SubnetArn"),
                "EnableDns64": subnet_info.get("EnableDns64"),
                "Ipv6Native": subnet_info.get("Ipv6Native"),
                "PrivateDnsNameOptionsOnLaunch": subnet_info.get("PrivateDnsNameOptionsOnLaunch")
            }
        except (KeyError, IndexError):
            return {"Error": "Unexpected response structure"}

    def _create_subnet(self, vpc_id: str, cidr_block: str, availability_zone: str = None) -> dict:
        cmd = [
            "aws", "ec2", "create-subnet",
            "--vpc-id", vpc_id,
            "--cidr-block", cidr_block,
            "--region", self.region_name
        ]

        if availability_zone:
            cmd.extend(["--availability-zone", availability_zone])

        return self._run_aws_command(cmd)

    def _delete_subnet(self, subnet_id: str) -> dict:
        cmd = [
            "aws", "ec2", "delete-subnet",
            "--subnet-id", subnet_id,
            "--region", self.region_name
        ]

        return self._run_aws_command(cmd)

    @property
    def region(self) -> str:
        if self.region_name:
            return self.region_name