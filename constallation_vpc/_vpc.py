import subprocess as _subprocess

class _vpc:
    def __init__(self, region_name: str = None, vpc_id: str = None, subnet_id: str = None):
        self.region_name = region_name
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id

    def _run_aws_cli_command(self, command: list) -> dict:
        command.insert(0, 'aws')
        result = _subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Error: {result.stderr}")
        return result.stdout

    def describe_vpc(self) -> dict:
        command = ['ec2', 'describe-vpcs']
        if self.vpc_id:
            command.extend(['--vpc-ids', self.vpc_id])
        if self.region_name:
            command.extend(['--region', self.region_name])
        return self._run_aws_cli_command(command)

    def describe_subnet(self) -> dict:
        command = ['ec2', 'describe-subnets']
        if self.subnet_id:
            command.extend(['--subnet-ids', self.subnet_id])
        if self.region_name:
            command.extend(['--region', self.region_name])
        return self._run_aws_cli_command(command)

    def create_vpc(self, cidr_block: str) -> dict:
        command = ['ec2', 'create-vpc', '--cidr-block', cidr_block]
        if self.region_name:
            command.extend(['--region', self.region_name])
        return self._run_aws_cli_command(command)

    def delete_vpc(self) -> dict:
        if not self.vpc_id:
            raise ValueError("vpc_id must be specified to delete a VPC")
        command = ['ec2', 'delete-vpc', '--vpc-id', self.vpc_id]
        if self.region_name:
            command.extend(['--region', self.region_name])
        return self._run_aws_cli_command(command)

    def create_subnet(self, vpc_id: str, cidr_block: str) -> dict:
        command = ['ec2', 'create-subnet', '--vpc-id', vpc_id, '--cidr-block', cidr_block]
        if self.region_name:
            command.extend(['--region', self.region_name])
        return self._run_aws_cli_command(command)

    def delete_subnet(self) -> dict:
        if not self.subnet_id:
            raise ValueError("subnet_id must be specified to delete a subnet")
        command = ['ec2', 'delete-subnet', '--subnet-id', self.subnet_id]
        if self.region_name:
            command.extend(['--region', self.region_name])
        return self._run_aws_cli_command(command)
