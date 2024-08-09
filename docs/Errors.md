# Errors Documentation

---

### 📋 **Table of Contents**

| **Class & Error**                                      | **Description**                            |
|--------------------------------------------------------|--------------------------------------------|
| [SubnetError](#subneterror)                            | Base class for all Subnet-related errors   |
| [SubnetError.SubnetCIDRConflicts](#subnetcidrconflicts) | Raised when a subnet CIDR conflicts        |
| [SubnetError.SubnetRangeError](#subnetrangeerror)      | Raised when a subnet IP range is invalid   |
| [SubnetError.SubnetIDNotFound](#subnetidnotfound)      | Raised when a subnet ID is not found       |
| [SubnetError.SubnetZoneMismatch](#subnetzonemismatch)  | Raised when a subnet is in the wrong zone  |
| [SubnetError.SubnetInUse](#subnetinuse)                | Raised when a subnet is in use             |
| [SubnetError.SubnetAssociationError](#subnetassociationerror) | Raised when a subnet association fails  |
| [SubnetError.SubnetDependentServiceError](#subnetdependentserviceerror) | Raised when a subnet is used by a dependent service |
| [SubnetError.SubnetAttachmentError](#subnetattachmenterror) | Raised when a subnet attachment fails   |
| [VPCError](#vpcerror)                                  | Base class for all VPC-related errors      |
| [VPCError.VPCCIDRConflicts](#vpccidrconflicts)         | Raised when a VPC CIDR conflicts           |
| [VPCError.VPCIDNotFound](#vpcidnotfound)               | Raised when a VPC ID is not found          |
| [VPCError.VPCInUse](#vpcinuse)                         | Raised when a VPC is in use                |
| [VPCError.VPCDependentServiceError](#vpcdependentserviceerror) | Raised when a VPC is used by a dependent service |
| [VPCError.VPCAttachmentError](#vpcattachmenterror)     | Raised when a VPC attachment fails         |
| [General AWS Errors](#general-aws-errors)              | General AWS errors                         |
| [AccessDeniedError](#accessdeniederror)                | Raised when access is denied               |
| [AuthFailureError](#authfailureerror)                  | Raised when authentication fails           |
| [RequestLimitExceededError](#requestlimitexceedederror) | Raised when request limit is exceeded  |
| [ThrottlingExceptionError](#throttlingexceptionerror)  | Raised when a request is throttled         |
| [ResourceNotFoundExceptionError](#resourcenotfoundexceptionerror) | Raised when a resource is not found |
| [InvalidParameterValueError](#invalidparametervalueerror) | Raised when a parameter is invalid     |
| [ServiceUnavailableError](#serviceunavailableerror)    | Raised when the service is unavailable     |
| [InternalFailureError](#internalfailureerror)          | Raised when an internal failure occurs     |
| [ValidationExceptionError](#validationexceptionerror)  | Raised when input fails validation         |
| [InvalidClientTokenIdError](#invalidclienttokeniderror) | Raised when a token is invalid             |
| [OptInRequiredError](#optinrequirederror)              | Raised when opt-in is required             |

---

## <span style="color: purple;">SubnetError</span>
`SubnetError` is a base class for all Subnet-related exceptions. It encapsulates the common behavior and attributes that specific Subnet exceptions inherit.

- ### <span style="color: cyan;">SubnetError.SubnetCIDRConflicts</span>
  - **Description**: Raised when a subnet CIDR conflicts with another subnet in the VPC.
  - **AWS CLI Error Code:** `InvalidSubnet.Conflict`

- ### <span style="color: cyan;">SubnetError.SubnetRangeError</span>
  - **Description**: Raised when the IP range specified for a subnet is invalid or out of range.
  - **AWS CLI Error Code:** `InvalidSubnet.Range`

- ### <span style="color: cyan;">SubnetError.SubnetIDNotFound</span>
  - **Description**: Raised when attempting to describe or delete a subnet that does not exist.
  - **AWS CLI Error Code:** `InvalidSubnet.ID.NotFound`

- ### <span style="color: cyan;">SubnetError.SubnetZoneMismatch</span>
  - **Description**: Raised when a subnet is specified in the wrong availability zone.
  - **AWS CLI Error Code:** `InvalidSubnet.ZoneMismatch`

- ### <span style="color: cyan;">SubnetError.SubnetInUse</span>
  - **Description**: Raised when a subnet is currently in use and cannot be modified or deleted.
  - **AWS CLI Error Code:** `InvalidSubnet.InUse`

- ### <span style="color: cyan;">SubnetError.SubnetAssociationError</span>
  - **Description**: Raised when there is an error associating the subnet with the specified resource.
  - **AWS CLI Error Code:** `InvalidSubnet.Association`

- ### <span style="color: cyan;">SubnetError.SubnetDependentServiceError</span>
  - **Description**: Raised when the subnet is being used by a dependent service and cannot be modified or deleted.
  - **AWS CLI Error Code:** `InvalidSubnet.DependentService`

- ### <span style="color: cyan;">SubnetError.SubnetAttachmentError</span>
  - **Description**: Raised when there is an error attaching the subnet to the specified resource.
  - **AWS CLI Error Code:** `InvalidSubnet.Attachment`

## <span style="color: purple;">VPCError</span>
`VPCError` is a base class for all VPC-related exceptions. It encapsulates the common behavior and attributes that specific VPC exceptions inherit.

- ### <span style="color: cyan;">VPCError.VPCCIDRConflicts</span>
  - **Description**: Raised when a VPC CIDR conflicts with another VPC.
  - **AWS CLI Error Code:** `InvalidVpc.Conflict`

- ### <span style="color: cyan;">VPCError.VPCIDNotFound</span>
  - **Description**: Raised when attempting to describe or delete a VPC that does not exist.
  - **AWS CLI Error Code:** `InvalidVpc.ID.NotFound`

- ### <span style="color: cyan;">VPCError.VPCInUse</span>
  - **Description**: Raised when a VPC is currently in use and cannot be modified or deleted.
  - **AWS CLI Error Code:** `InvalidVpc.InUse`

- ### <span style="color: cyan;">VPCError.VPCDependentServiceError</span>
  - **Description**: Raised when the VPC is being used by a dependent service and cannot be modified or deleted.
  - **AWS CLI Error Code:** `InvalidVpc.DependentService`

- ### <span style="color: cyan;">VPCError.VPCAttachmentError</span>
  - **Description**: Raised when there is an error attaching the VPC to the specified resource.
  - **AWS CLI Error Code:** `InvalidVpc.Attachment`

## <span style="color: purple;">General AWS Errors</span>
These are exceptions that can occur during any AWS operation, not limited to VPCs or Subnets.

- ### <span style="color: cyan;">AccessDeniedError</span>
  - **Description**: Raised when you do not have the necessary permissions to perform an operation.
  - **AWS CLI Error Code:** `AccessDenied`

- ### <span style="color: cyan;">AuthFailureError</span>
  - **Description**: Raised when authentication fails due to invalid AWS credentials.
  - **AWS CLI Error Code:** `AuthFailure`

- ### <span style="color: cyan;">RequestLimitExceededError</span>
  - **Description**: Raised when the request limit is exceeded.
  - **AWS CLI Error Code:** `RequestLimitExceeded`

- ### <span style="color: cyan;">ThrottlingExceptionError</span>
  - **Description**: Raised when the request is throttled by AWS.
  - **AWS CLI Error Code:** `ThrottlingException`

- ### <span style="color: cyan;">ResourceNotFoundExceptionError</span>
  - **Description**: Raised when the specified resource cannot be found.
  - **AWS CLI Error Code:** `ResourceNotFoundException`

- ### <span style="color: cyan;">InvalidParameterValueError</span>
  - **Description**: Raised when one or more parameters are invalid.
  - **AWS CLI Error Code:** `InvalidParameterValue`

- ### <span style="color: cyan;">ServiceUnavailableError</span>
  - **Description**: Raised when the AWS service is currently unavailable.
  - **AWS CLI Error Code:** `ServiceUnavailable`

- ### <span style="color: cyan;">InternalFailureError</span>
  - **Description**: Raised when an internal error occurs within AWS.
  - **AWS CLI Error Code:** `InternalFailure`

- ### <span style="color: cyan;">ValidationExceptionError</span>
  - **Description**: Raised when the input provided does not meet the required constraints.
  - **AWS CLI Error Code:** `ValidationException`

- ### <span style="color: cyan;">InvalidClientTokenIdError</span>
  - **Description**: Raised when the security token included in the request is invalid.
  - **AWS CLI Error Code:** `InvalidClientTokenId`

- ### <span style="color: cyan;">OptInRequiredError</span>
  - **Description**: Raised when you must opt in to use a service.
  - **AWS CLI Error Code:** `OptInRequired`

---
