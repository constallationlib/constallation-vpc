# Errors

## SubnetError
SubnetError is a base class for all Subnet Query Exceptions
- ### SubnetCIDRConflicts
  - When creating a subnet, if the subnet cidr conflicts with another subnet in the vpc, it will throw **SubnetCIDRConflicts**
  - #### **AWS CLI Error Code:** `InvalidSubnet.Conflict`