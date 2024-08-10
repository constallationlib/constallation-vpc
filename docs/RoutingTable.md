

# <code>RoutingTable(<span style="color: #DA70D6;">_vpc</span>)</code>

- The `RoutingTable` class is an integral part of the `constallation_vpc` module, designed to provide a powerful, object-oriented interface for managing Route Tables in AWS. It extends the `_vpc` class to leverage AWS CLI for route table operations.

## <span style="color: #9932CC;">**Execution Arguments**</span>

```python
route_table = RoutingTable(
    region = "us-west-2",
    route_table_id = "example_route_table_id",
    vpc_id = "example_vpc_id",
    aws_access_key = "example_key",
    aws_secret_access_key = "secret_example_key",
    aws_sts_session_token = "example_token"
)
```

- #### <span style="color: #DA70D6;">**Region**</span>
  - Specify the AWS region where the route table will be created or managed.

- #### <span style="color: #DA70D6;">**route_table_id**</span>
  - If you have an existing Route Table, you can provide its ID here. The class will automatically configure itself to interface with that Route Table.

- #### <span style="color: #DA70D6;">**vpc_id**</span>
  - The ID of the VPC that the route table is associated with.

- #### <span style="color: #DA70D6;">**aws_access_key**</span>
  - Enter your AWS `access_key` here to authenticate requests. This is crucial for secure communication with AWS services.

- #### <span style="color: #DA70D6;">**aws_secret_access_key**</span>
  - The `secret_access_key` corresponding to your AWS `access_key` is required here to ensure secure access to AWS resources.

- #### <span style="color: #DA70D6;">**aws_sts_session_token**</span>
  - This optional argument allows you to configure the `RoutingTable` client to use an AWS STS session token for temporary security credentials, adding an extra layer of security when necessary.

## <span style="color: #00d192;">**Example Usage**</span>

- ### <span style="color: #36a8ff;">**Create A Route Table in us-west-2**</span>
  - ```python
    route_table = RoutingTable(
        region = "us-west-2",
        vpc_id = "example_vpc_id"
    )
    ```

- ### <span style="color: #36a8ff;">**Interact With An Existing Route Table**</span>
  - ```python
    route_table = RoutingTable(
        region = "us-west-2",
        route_table_id = "example_route_table_id"
    )
    ```
  - Initializes a RoutingTable client around your `route_table_id` in `us-west-2`.
  
  - ```python
    print(route_table.describe_route_table())
    ```
  - Retrieves details about the specified Route Table and prints them out.

- ### <span style="color: #36a8ff;">**Associate Route Table with a Subnet**</span>
  - ```python
    route_table.associate_route_table(subnet_id="example_subnet_id")
    ```
  - Associates the Route Table with the specified Subnet.

- ### <span style="color: #36a8ff;">**Create a Route in the Route Table**</span>
  - ```python
    route_table.create_route(destination_cidr_block="0.0.0.0/0", gateway_id="example_gateway_id")
    ```
  - Creates a route in the Route Table for the specified destination CIDR block.
