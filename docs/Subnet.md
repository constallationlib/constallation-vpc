# <code>Subnet(<span style="color: #DA70D6;">[_vpc]("_vpc.md")</span>)</code>
- The subnet class was the first class developed in constallation_vpc. It serves to provide an object based interface unique from boto3.resources.
- [_vpc]("_vpc.md") is the base class and also backbone of constallation_vpc. Subnet uses it to make CLI requests to AWS
### Execution Arguments
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
  - The region you would like to query to
- #### <span style="color: #DA70D6;">**subnet_id**</span>
  - If you would like to associate the class with a pre-existing subnet it will automatically set itself up. 
  - ID must start with subnet
- #### <span style="color: #DA70D6;">**aws_access_key**</span>
  - if you would like to use an access_key to authenticate with aws you would put your access key in here
- #### <span style="color: #DA70D6;">**aws_secret_access_key**</span>
  - The secret_access_key for the aws_access_key
- #### <span style="color: #DA70D6;">**aws_sts_session_token**</span>
  - You can configure the Subnet client to use an sts session token for temporary credentials. 
- #### <span style="color: #DA70D6;">**vpc_id**</span>
  - If you would like to preassign a vpc for vpc_creation you would put the id of that vpc here
- #### <span style="color: #DA70D6;">**cidr_block**</span>
  - If you want to create a subnet put the cidr block here
- #### <span style="color: #DA70D6;">**availability_zone**</span>
  -   - If you want to create a subnet put the avalibility_zone 