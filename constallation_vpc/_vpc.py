import subprocess as _subprocess

class _vpc:
    def __init__(self, region_name: str = None, vpc_id: str = None, subnet_id: str = None, 
                 access_key: str = None, secret_key: str = None, session_token: str = None):
        self.region_name = region_name
        self._vpc_id = vpc_id
        self._subnet_id = subnet_id
        self._access_key = access_key
        self._secret_key = secret_key
        self._session_token = session_token

    def _run_aws_cli_command(self, command: list) -> dict:
        command.insert(0, 'aws')
        if self.region_name:
            command.extend(['--region', self.region_name])
        if self._access_key and self._secret_key:
            command.extend(['--access-key', self._access_key, '--secret-key', self._secret_key])
        if self._session_token:
            command.extend(['--session-token', self._session_token])
        
        result = _subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Error: {result.stderr}")
        return result.stdout

    def describe_vpc(self) -> dict:
        command = ['ec2', 'describe-vpcs']
        if self._vpc_id:
            command.extend(['--vpc-ids', self._vpc_id])
        return self._run_aws_cli_command(command)

    def describe_subnet(self) -> dict:
        command = ['ec2', 'describe-subnets']
        if self._subnet_id:
            command.extend(['--subnet-ids', self._subnet_id])
        return self._run_aws_cli_command(command)

    def create_vpc(self, cidr_block: str) -> dict:
        command = ['ec2', 'create-vpc', '--cidr-block', cidr_block]
        return self._run_aws_cli_command(command)

    def delete_vpc(self) -> dict:
        if not self._vpc_id:
            raise ValueError("vpc_id must be specified to delete a VPC")
        command = ['ec2', 'delete-vpc', '--vpc-id', self._vpc_id]
        return self._run_aws_cli_command(command)

    def create_subnet(self, vpc_id: str, cidr_block: str) -> dict:
        command = ['ec2', 'create-subnet', '--vpc-id', vpc_id, '--cidr-block', cidr_block]
        return self._run_aws_cli_command(command)

    def delete_subnet(self) -> dict:
        if not self._subnet_id:
            raise ValueError("subnet_id must be specified to delete a subnet")
        command = ['ec2', 'delete-subnet', '--subnet-id', self._subnet_id]
        return self._run_aws_cli_command(command)
    
    def modify_vpc_attribute(self, enable_dns_support: bool = None, enable_dns_hostnames: bool = None) -> dict:
        if not self._vpc_id:
            raise ValueError("vpc_id must be specified to modify a VPC attribute")
        command = ['ec2', 'modify-vpc-attribute', '--vpc-id', self._vpc_id]
        if enable_dns_support is not None:
            command.extend(['--enable-dns-support', str(enable_dns_support).lower()])
        if enable_dns_hostnames is not None:
            command.extend(['--enable-dns-hostnames', str(enable_dns_hostnames).lower()])
        return self._run_aws_cli_command(command)

    def create_tags(self, resource_id: str, tags: dict) -> dict:
        command = ['ec2', 'create-tags', '--resources', resource_id]
        tag_list = [{'Key': k, 'Value': v} for k, v in tags.items()]
        for tag in tag_list:
            command.extend(['--tags', f'Key={tag["Key"]},Value={tag["Value"]}'])
        return self._run_aws_cli_command(command)

    def describe_vpc_endpoints(self) -> dict:
        command = ['ec2', 'describe-vpc-endpoints']
        if self._vpc_id:
            command.extend(['--filters', f'Name=vpc-id,Values={self._vpc_id}'])
        return self._run_aws_cli_command(command)

    def create_route_table(self, vpc_id: str) -> dict:
        command = ['ec2', 'create-route-table', '--vpc-id', vpc_id]
        return self._run_aws_cli_command(command)

    def delete_route_table(self, route_table_id: str) -> dict:
        command = ['ec2', 'delete-route-table', '--route-table-id', route_table_id]
        return self._run_aws_cli_command(command)

    def describe_vpc_attribute(self, attribute: str) -> dict:
        if not self._vpc_id:
            raise ValueError("vpc_id must be specified to describe a VPC attribute")
        command = ['ec2', 'describe-vpc-attribute', '--vpc-id', self._vpc_id, '--attribute', attribute]
        return self._run_aws_cli_command(command)

    def describe_route_tables(self) -> dict:
        command = ['ec2', 'describe-route-tables']
        if self._vpc_id:
            command.extend(['--filters', f'Name=vpc-id,Values={self._vpc_id}'])
        return self._run_aws_cli_command(command)

    def associate_route_table(self, subnet_id: str, route_table_id: str) -> dict:
        command = ['ec2', 'associate-route-table', '--subnet-id', subnet_id, '--route-table-id', route_table_id]
        return self._run_aws_cli_command(command)

    def disassociate_route_table(self, association_id: str) -> dict:
        command = ['ec2', 'disassociate-route-table', '--association-id', association_id]
        return self._run_aws_cli_command(command)

    def create_vpc_peering_connection(self, peer_vpc_id: str, peer_region: str = None, peer_owner_id: str = None) -> dict:
        command = ['ec2', 'create-vpc-peering-connection', '--vpc-id', self._vpc_id, '--peer-vpc-id', peer_vpc_id]
        if peer_region:
            command.extend(['--peer-region', peer_region])
        if peer_owner_id:
            command.extend(['--peer-owner-id', peer_owner_id])
        return self._run_aws_cli_command(command)

    def accept_vpc_peering_connection(self, vpc_peering_connection_id: str) -> dict:
        command = ['ec2', 'accept-vpc-peering-connection', '--vpc-peering-connection-id', vpc_peering_connection_id]
        return self._run_aws_cli_command(command)

    def delete_vpc_peering_connection(self, vpc_peering_connection_id: str) -> dict:
        command = ['ec2', 'delete-vpc-peering-connection', '--vpc-peering-connection-id', vpc_peering_connection_id]
        return self._run_aws_cli_command(command)

    def describe_vpc_peering_connections(self) -> dict:
        command = ['ec2', 'describe-vpc-peering-connections']
        if self._vpc_id:
            command.extend(['--filters', f'Name=requester-vpc-info.vpc-id,Values={self._vpc_id}', 
                            f'Name=accepter-vpc-info.vpc-id,Values={self._vpc_id}'])
        return self._run_aws_cli_command(command)
    
    def create_internet_gateway(self) -> dict:
        command = ['ec2', 'create-internet-gateway']
        return self._run_aws_cli_command(command)

    def attach_internet_gateway(self, internet_gateway_id: str) -> dict:
        if not self._vpc_id:
            raise ValueError("vpc_id must be specified to attach an internet gateway")
        command = ['ec2', 'attach-internet-gateway', '--internet-gateway-id', internet_gateway_id, '--vpc-id', self._vpc_id]
        return self._run_aws_cli_command(command)

    def detach_internet_gateway(self, internet_gateway_id: str) -> dict:
        if not self._vpc_id:
            raise ValueError("vpc_id must be specified to detach an internet gateway")
        command = ['ec2', 'detach-internet-gateway', '--internet-gateway-id', internet_gateway_id, '--vpc-id', self._vpc_id]
        return self._run_aws_cli_command(command)

    def delete_internet_gateway(self, internet_gateway_id: str) -> dict:
        command = ['ec2', 'delete-internet-gateway', '--internet-gateway-id', internet_gateway_id]
        return self._run_aws_cli_command(command)

    def describe_internet_gateways(self) -> dict:
        command = ['ec2', 'describe-internet-gateways']
        if self._vpc_id:
            command.extend(['--filters', f'Name=attachment.vpc-id,Values={self._vpc_id}'])
        return self._run_aws_cli_command(command)
