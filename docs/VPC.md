
# <code>VPC(<span style="color: #DA70D6;">_vpc</span>)</code>

- The `VPC` class is an integral part of the `constallation_vpc` module, designed to provide a powerful, object-oriented interface for managing Virtual Private Clouds (VPCs) in AWS. It enhances the capabilities of `boto3.resources`, giving you more granular control and flexibility over VPC operations.
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

- #### <span style="color: #DA70D6;">**vpc_id**</span>
  - If you have an existing VPC, you can provide its ID here (which must start with `vpc`). The class will automatically configure itself to interface with that VPC.

- #### <span style="color: #DA70D6;">**aws_access_key**</span>
  - Enter your AWS `access_key` here to authenticate requests. This is crucial for secure communication with AWS services.

- #### <span style="color: #DA70D6;">**aws_secret_access_key**</span>
  - The `secret_access_key` corresponding to your AWS `access_key` is required here to ensure secure access to AWS resources.

- #### <span style="color: #DA70D6;">**aws_sts_session_token**</span>
  - This optional argument allows you to configure the `VPC` client to use an AWS STS session token for temporary security credentials, adding an extra layer of security when necessary.

- #### <span style="color: #DA70D6;">**vpc_cidr_block**</span>
  - Provide the CIDR block to create a new VPC. If an existing VPC ID is provided, this argument can be omitted.

## <span style="color: #00d192;">**Example Usage**</span>

- ### <span style="color: #36a8ff;">**Create A VPC in us-west-2**</span>
  - ```python
    vpc = VPC(
        region = "us-west-2",
        vpc_cidr_block = "10.0.0.0/16"
    )
    ```

- ### <span style="color: #36a8ff;">**Interact With An Existing VPC**</span>
  - ```python
    vpc = VPC(
        region = "us-west-2",
        vpc_id = "example_vpc_id"
    )
    ```
  - Initializes a VPC client around your `vpc_id` in `us-west-2`.
  
  - ```python
    print(vpc.describe_vpc())
    ```
  - Retrieves details about the specified VPC and prints them out.

- ### <span style="color: #36a8ff;">**Get All Subnets Associated With The VPC**</span>
  - ```python
    subnets = vpc.get_subnets()
    for subnet in subnets:
        print(subnet.subnet_id())
    ```
  - Retrieves all subnets associated with the VPC and prints out their details.
****