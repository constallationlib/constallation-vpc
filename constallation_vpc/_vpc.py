import subprocess as _subprocess

class _vpc:
    def __init__(self, region_name: str = None, vpc_id: str = None, subnet_id: str = None, 
                 access_key: str = None, secret_key: str = None, session_token: str = None):
        self.region_name = region_name
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.access_key = access_key
        self.secret_key = secret_key
        self.session_token = session_token

    def _run_aws_cli_command(self, command: list) -> dict:
        command.insert(0, 'aws')
        if self.region_name:
            command.extend(['--region', self.region_name])
        if self.access_key and self.secret_key:
            command.extend(['--access-key', self.access_key, '--secret-key', self.secret_key])
        if self.session_token:
            command.extend(['--session-token', self.session_token])
        
        result = _subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Error: {result.stderr}")
        return result.stdout

    def describe_vpc(self) -> dict:
        command = ['ec2', 'describe-vpcs']
        if self.vpc_id:
            command.extend(['--vpc-ids', self.vpc_id])
        return self._run_aws_cli_command(command)

    def describe_subnet(self) -> dict:
        command = ['ec2', 'describe-subnets']
        if self.subnet_id:
            command.extend(['--subnet-ids', self.subnet_id])
        return self._run_aws_cli_command(command)

    def create_vpc(self, cidr_block: str) -> dict:
        command = ['ec2', 'create-vpc', '--cidr-block', cidr_block]
        return self._run_aws_cli_command(command)

    def delete_vpc(self) -> dict:
        if not self.vpc_id:
            raise ValueError("vpc_id must be specified to delete a VPC")
        command = ['ec2', 'delete-vpc', '--vpc-id', self.vpc_id]
        return self._run_aws_cli_command(command)

    def create_subnet(self, vpc_id: str, cidr_block: str) -> dict:
        command = ['ec2', 'create-subnet', '--vpc-id', vpc_id, '--cidr-block', cidr_block]
        return self._run_aws_cli_command(command)

    def delete_subnet(self) -> dict:
        if not self.subnet_id:
            raise ValueError("subnet_id must be specified to delete a subnet")
        command = ['ec2', 'delete-subnet', '--subnet-id', self.subnet_id]
        return self._run_aws_cli_command(command)
