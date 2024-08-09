
# <code>Subnet(<span style="color: #DA70D6;">[_vpc]("_vpc.md")</span>)</code>

- The `Subnet` class was the pioneering class in the `constallation_vpc` module. It provides a unique, object-oriented interface that differentiates itself from `boto3.resources`, offering enhanced control and flexibility.
- <span style="color: #DA70D6;">[`_vpc`]("_vpc.md")</span> is the foundational base class and the backbone of the `constallation_vpc` module. The `Subnet` class leverages `_vpc` to efficiently execute CLI requests to AWS.

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
  - Specify the AWS region where you want to perform the query.
  
- #### <span style="color: #DA70D6;">**subnet_id**</span>
  - If you have a pre-existing subnet, providing its ID (which must start with `subnet`) will allow the class to automatically configure itself to interface with that subnet.
  
- #### <span style="color: #DA70D6;">**aws_access_key**</span>
  - Enter your AWS `access_key` here to authenticate requests. This is crucial for secure communication with AWS services.
  
- #### <span style="color: #DA70D6;">**aws_secret_access_key**</span>
  - The `secret_access_key` corresponding to your AWS `access_key` is required here to ensure secure access to AWS resources.
  
- #### <span style="color: #DA70D6;">**aws_sts_session_token**</span>
  - This optional argument allows you to configure the `Subnet` client to use an AWS STS session token for temporary security credentials, adding an extra layer of security when necessary.
  
- #### <span style="color: #DA70D6;">**vpc_id**</span>
  - Preassign a specific VPC by providing its ID here. This is particularly useful for VPC-related operations where you want to work within a designated VPC environment.
  
- #### <span style="color: #DA70D6;">**cidr_block**</span>
  - Provide the CIDR block to create a subnet within your specified VPC.
  
- #### <span style="color: #DA70D6;">**availability_zone**</span>
  - Specify the Availability Zone within the specified region where the subnet should be created.

## <span style="color: #007854;">**Example Usage**</span>