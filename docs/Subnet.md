
# <code>Subnet(<span style="color: #DA70D6;">_vpc</span>)</code>

- The `Subnet` class was the pioneering class in the `constallation_vpc` module. It provides a unique, object-oriented interface that differentiates itself from `boto3.resources`, offering enhanced control and flexibility.
- <span style="color: #DA70D6;">[`_vpc`]("_vpc")</span> is the foundational base class and the backbone of the `constallation_vpc` module. The `Subnet` class leverages `_vpc` to efficiently execute CLI requests to AWS.

## <span style="color: #9932CC;">**Execution Arguments**</span>

```python
subnet = Subnet(
    region = "us-west-2",
    subnet_id = "example_id",
    aws_access_key = "example_key",
    aws_secret_access_key = "secret_example_key",
    aws_sts_session_token = "example_token",
    vpc_id = "example_vpc_id",
    cidr_block = "10.0.0.0/24",
    availability_zone = 'us-west-2a'
)
```

- #### <span style="color: #DA70D6;">**Region**</span>
  - Specify the AWS region where the subnet will be created or managed.

- #### <span style="color: #DA70D6;">**Subnet ID**</span>
  - The identifier of the subnet to manage or modify.

- #### <span style="color: #DA70D6;">**AWS Access Key & Secret Key**</span>
  - Credentials for authenticating API requests to AWS. These are optional if using a configured environment.

- #### <span style="color: #DA70D6;">**VPC ID**</span>
  - The identifier of the VPC that the subnet is associated with.

- #### <span style="color: #DA70D6;">**CIDR Block**</span>
  - The IPv4 network range for the subnet, in CIDR notation.

- #### <span style="color: #DA70D6;">**Availability Zone**</span>
  - The specific availability zone within the AWS region where the subnet will be located.

## <span style="color: #9932CC;">**Routing Table Integration**</span>

- The `Subnet` class supports integration with AWS routing tables, allowing you to assign and manage routing tables for specific subnets within a VPC.

### Example:

```python
# Assuming 'subnet' is an instance of the Subnet class
routing_table = RoutingTable(
    region="us-west-2",
    route_table_id="rtb-12345678",
    aws_access_key="example_key",
    aws_secret_access_key="secret_example_key"
)

# Associate the routing table with the subnet
subnet.associate_routing_table(routing_table)
```

## <span style="color: #9932CC;">**Error Handling**</span>

- The `Subnet` class includes comprehensive error handling to manage potential issues during subnet operations.

### Common Errors:

- **SubnetCIDRConflicts**: Raised when there is a CIDR block conflict during subnet creation or modification.
- **SubnetRangeError**: Raised when the specified subnet range is invalid.

These errors help ensure that any issues are clearly communicated, allowing for easier resolution.

## <span style="color: #9932CC;">**Additional Functions**</span>

- The `Subnet` class may offer additional functions for managing subnet-specific operations, such as creating, deleting, and describing subnets.

### Example:

```python
subnet.describe_subnet()
```

This method retrieves details about the specified subnet, including its associated routing tables, CIDR block, and availability zone.

