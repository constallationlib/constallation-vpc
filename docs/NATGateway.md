
# NatGateway Class Documentation

The `NatGateway` class is an essential component of the `constellation_vpc` module, designed to manage and manipulate NAT Gateways (NGWs) in AWS. It extends the `_vpc` base class to provide a robust and efficient interface for handling various NAT Gateway operations within a Virtual Private Cloud (VPC).

## **Execution Arguments**

```python
nat_gateway = NatGateway(
    region="us-west-2",
    nat_gateway_id="example_nat_gateway_id",
    aws_access_key="example_key",
    aws_access_secret_key="secret_example_key"
)
```

### **Region**
- The AWS region where the NAT Gateway will be created, associated, or deleted.

### **NAT Gateway ID (NatGateway ID)**
- The identifier of the NAT Gateway. This is necessary for associating, disassociating, or deleting an existing NAT Gateway.

### **AWS Access Key & Secret Key**
- These are the credentials for authenticating API requests to AWS. They are optional if the environment is already configured with appropriate AWS credentials.

## **Core Methods**

### **Creating a NAT Gateway**
- The `_create_nat_gateway` method is responsible for creating a new NAT Gateway in the specified region.

```python
nat_creation_result = nat_gateway.create_nat_gateway(
    subnet_id="subnet-12345678",
    allocation_id="eipalloc-12345678",
    nat_gateway_name="custom-nat-gateway-name"
)
```

#### **Arguments:**
- **subnet_id:** The ID of the subnet in which to create the NAT Gateway.
- **allocation_id:** The Elastic IP allocation ID for the NAT Gateway.
- **nat_gateway_name:** Optional. The name to assign to the newly created NAT Gateway. Default is `"constellation-nat-gateway"`.

#### **Returns:**
- A dictionary containing the creation result or an error message.

### **Deleting a NAT Gateway**
- The `_delete_nat_gateway` method deletes an existing NAT Gateway.

```python
delete_result = nat_gateway.delete_nat_gateway()
```

#### **Returns:**
- A dictionary containing the deletion result or an error message if the NAT Gateway ID is not provided.

### **Describing NAT Gateways**
- The `_describe_nat_gateways` method provides details about existing NAT Gateways associated with a specific VPC or subnet.

```python
describe_result = nat_gateway.describe_nat_gateways(vpc_id="vpc-12345678")
```

#### **Arguments:**
- **vpc_id:** Optional. The VPC ID for which to describe the associated NAT Gateways.
- **subnet_id:** Optional. The Subnet ID for which to describe the associated NAT Gateways.

#### **Returns:**
- A dictionary containing the description of the NAT Gateways or an error message.

### **Associating a NAT Gateway with a Route Table**
- The `_associate_nat_gateway` method associates an existing NAT Gateway with a specified route table.

```python
associate_result = nat_gateway.associate_nat_gateway(route_table_id="rtb-12345678")
```

#### **Arguments:**
- **route_table_id:** The Route Table ID to which the NAT Gateway should be associated.

#### **Returns:**
- A dictionary containing the association result or an error message if the NAT Gateway ID is not provided.

### **Disassociating a NAT Gateway from a Route Table**
- The `_disassociate_nat_gateway` method disassociates an existing NAT Gateway from a specified route table.

```python
disassociate_result = nat_gateway.disassociate_nat_gateway(route_table_id="rtb-12345678")
```

#### **Arguments:**
- **route_table_id:** The Route Table ID from which the NAT Gateway should be disassociated.

#### **Returns:**
- A dictionary containing the disassociation result or an error message.

## **Error Handling**

The `NatGateway` class implements robust error handling to manage common issues that may occur during AWS operations.

### Common Errors:
- **ClientNotFoundError:** Raised when the AWS CLI is not installed.
- **NatGatewayNotFound:** Raised when the specified NAT Gateway is not found.
- **InvalidParameterError:** Raised when an invalid parameter is provided to the method.

These error checks ensure that operations are executed smoothly, and appropriate feedback is given for troubleshooting.

## **Additional Notes**

The `NatGateway` class provides an efficient interface for managing NAT Gateways within AWS, offering methods for creation, association, disassociation, deletion, and description. It is designed to be integrated seamlessly with the VPC management capabilities provided by the `VPC` class, allowing for a comprehensive VPC and NAT Gateway management experience in AWS.
