# <code>Subnet(<span style="color: #DA70D6;">[_vpc]("_vpc.md")</span>)</code>
- The subnet class was the first class developed in constallation_vpc. It serves to provide an object based interface unique from boto3.resources.
- [_vpc]("_vpc.md") is the base class and also backbone of constallation_vpc. Subnet uses it to make CLI requests to AWS
### Execution Arguments
```python
Subnet(
    region = "us-west-2",
    subnet_id = "example_id",
    aws_access_key = "example_key",
    aws_secret_access_key = "secret_example_key",
    aws_sts_token = "example_token",
    vpc_id = "example_vpc_id",
    cidr_block = "10.0.0.0/24,
    availability_zone = 'us-west-2a'"
)
```