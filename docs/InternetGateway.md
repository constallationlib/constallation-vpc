
# InternetGateway Class Documentation

The `InternetGateway` class is a critical component of the `constellation_vpc` module, designed to manage and manipulate Internet Gateways (IGWs) in AWS. It extends the `_vpc` base class to provide a seamless and efficient interface for handling various IGW operations within a Virtual Private Cloud (VPC).

## **Execution Arguments**

```python
igw = InternetGateway(
    region="us-west-2",
    igw_id="example_igw_id",
    aws_access_key="example_key",
    aws_access_secret_key="secret_example_key"
)
```

### **Region**
- The AWS region where the Internet Gateway will be created, attached, detached, or deleted.

### **Internet Gateway ID (IGW ID)**
- The identifier of the Internet Gateway. This is necessary for attaching, detaching, or deleting an existing IGW.

### **AWS Access Key & Secret Key**
- These are the credentials for authenticating API requests to AWS. They are optional if the environment is already configured with appropriate AWS credentials.

## **Core Methods**

### **Creating an Internet Gateway**
- The `_create_internet_gateway` method is responsible for creating a new Internet Gateway in the specified region.

```python
igw_creation_result = igw._create_internet_gateway(igw_name="custom-igw-name")
```

#### **Arguments:**
- **igw_name:** Optional. The name to assign to the newly created Internet Gateway. Default is `"constellation-igw"`.

#### **Returns:**
- A dictionary containing the creation result or an error message.

### **Attaching an Internet Gateway to a VPC**
- The `_attach_internet_gateway` method attaches an existing Internet Gateway to a specified VPC.

```python
attach_result = igw._attach_internet_gateway(vpc_id="vpc-12345678")
```

#### **Arguments:**
- **vpc_id:** The VPC ID to which the Internet Gateway should be attached.

#### **Returns:**
- A dictionary containing the attachment result or an error message if the IGW ID is not provided.

### **Detaching an Internet Gateway from a VPC**
- The `_detach_internet_gateway` method detaches an existing Internet Gateway from a specified VPC.

```python
detach_result = igw._detach_internet_gateway(vpc_id="vpc-12345678")
```

#### **Arguments:**
- **vpc_id:** The VPC ID from which the Internet Gateway should be detached.

#### **Returns:**
- A dictionary containing the detachment result or an error message if the IGW ID is not provided.

### **Deleting an Internet Gateway**
- The `_delete_internet_gateway` method deletes an existing Internet Gateway.

```python
delete_result = igw._delete_internet_gateway()
```

#### **Returns:**
- A dictionary containing the deletion result or an error message if the IGW ID is not provided.

### **Describing Internet Gateways**
- The `_describe_internet_gateways` method provides details about existing Internet Gateways associated with a specific VPC.

```python
describe_result = igw._describe_internet_gateways(vpc_id="vpc-12345678")
```

#### **Arguments:**
- **vpc_id:** Optional. The VPC ID for which to describe the associated Internet Gateways.

#### **Returns:**
- A dictionary containing the description of the Internet Gateways or an error message.

## **Error Handling**

The `InternetGateway` class implements robust error handling to manage common issues that may occur during AWS operations.

### Common Errors:
- **ClientNotFoundError:** Raised when the AWS CLI is not installed.
- **InternetGatewayNotFound:** Raised when the specified Internet Gateway is not found.
- **InvalidParameterError:** Raised when an invalid parameter is provided to the method.

These error checks ensure that operations are executed smoothly, and appropriate feedback is given for troubleshooting.

## **Additional Notes**

The `InternetGateway` class provides an efficient interface for managing IGWs within AWS, offering methods for creation, attachment, detachment, deletion, and description. It is designed to be integrated seamlessly with the VPC management capabilities provided by the `VPC` class, allowing for a comprehensive VPC and IGW management experience in AWS.
