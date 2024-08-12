
# <code>VPC(<span style="color: #DA70D6;">_vpc</span>)</code>

- The `VPC` class is an integral part of the `constellation_vpc` module, designed to provide a powerful, object-oriented interface for managing Virtual Private Clouds (VPCs) in AWS. It enhances the capabilities of `boto3.resources`, giving you more granular control and flexibility over VPC operations.
- <span style="color: #DA70D6;">[`_vpc`]("_vpc")</span> is the foundational base class that the `VPC` class extends to interact seamlessly with AWS CLI, allowing efficient execution of VPC-related operations.

## <span style="color: #9932CC;">**Execution Arguments**</span>

```python
vpc = VPC(
    region = "us-west-2",
    vpc_id = "example_vpc_id",
    aws_access_key = "example_key",
    aws_secret_access_key = "secret_example_key",
    aws_sts_session_token = "example_token",
    vpc_cidr_block = "10.0.0.0/16"
)
```

- #### <span style="color: #DA70D6;">**Region**</span>
  - Specify the AWS region where the VPC will be created or managed.

- #### <span style="color: #DA70D6;">**VPC ID**</span>
  - The identifier of the VPC to manage or modify.

- #### <span style="color: #DA70D6;">**AWS Access Key & Secret Key**</span>
  - Credentials for authenticating API requests to AWS. These are optional if using a configured environment.

- #### <span style="color: #DA70D6;">**VPC CIDR Block**</span>
  - The IPv4 network range for the VPC, in CIDR notation.

## <span style="color: #9932CC;">**Routing Table Integration**</span>

- The `VPC` class allows integration with AWS routing tables, providing methods to associate, disassociate, and manage routing tables within the VPC context.
- You can utilize the `RoutingTable` class in conjunction with the `VPC` class to assign specific routing tables to your VPC or subnets.

### Example:

```python
# Assuming 'vpc' is an instance of the VPC class
routing_table = RoutingTable(
    region="us-west-2",
    route_table_id="rtb-12345678",
    aws_access_key="example_key",
    aws_secret_access_key="secret_example_key"
)

# Associate the routing table with the VPC
vpc.associate_routing_table(routing_table)
```

## <span style="color: #9932CC;">**Error Handling**</span>

- The `VPC` class has robust error handling to manage common issues that may arise during AWS operations.

### Common Errors:

- **ClientNotFoundError**: Raised when the AWS CLI is not installed.
- **SubnetCIDRConflicts**: Raised when there is a CIDR block conflict during subnet operations within the VPC.
- **SubnetRangeError**: Raised when the subnet range is invalid.

These errors ensure that issues are caught early, and meaningful feedback is provided to help with troubleshooting.

## <span style="color: #9932CC;">**Additional Functions**</span>

- The `VPC` class may include additional functions to facilitate various AWS operations, such as describing, creating, and deleting VPCs, subnets, and other related resources.

### Example:

```python
vpc.describe_vpc()
```

This method retrieves details about the specified VPC, including its associated subnets, routing tables, and other configurations.

