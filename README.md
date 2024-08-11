# constallation-vpc
## Version 0.2.0a4
### **<span style="color:red;">Warning | Do Not Use for anything important</span>**
**The version _0.2.0a4 is a package from the alpha stages and also pre-release** and has **undergone very minimal testing.** This version was built on `08/10/2024` Please use something more modern and closer to latest as this package is not secure for any actual use and its release serves archival means. 

***
### Changelist
- #### **<span style="color:red;">0.2.0a0</span>**
  - Added Routing Table Class
    - Potentially unstable and untested!
- #### **<span style="color:red;">0.2.0a1</span>**
  - Update Docs, integration preperation
- #### **<span style="color:red;">0.2.0a2</span>**
  - Integrate Into VPCs
- #### **<span style="color:red;">0.2.0a4</span>**
  - Integrate Into Subnets
  - Catch AWS Client Not Installed Error
- #### **<span style="color:red;">0.2.0a4</span>**
  - Handle The Following AWS CLI Error Codes
    - `InvalidRouteTableID.NotFound`
    - `InvalidRoute.NotFound`
    - `RouteAlreadyExists`
- #### **<span style="color:red;">0.2.0a5 (Planned)</span>**
  - Handle The Following AWS CLI Error Codes
      - `DependencyViolation`
      - `InvalidRouteTableAssociationID.NotFound`
    - Update Docs for VPCs
- #### **<span style="color:red;">0.2.0a6 (Planned)</span>**
  - Handle The Following AWS CLI Error Codes
    - `InvalidRouteTableID.Malformed`
    - `UnauthorizedOperation`
  - Update Docs For RoutingTable
- #### **<span style="color:red;">0.2.0a7 (Planned)</span>**
  - Handle The Following AWS CLI Error Codes
    - `InvalidParameterValue`
    - `RequestLimitExceeded`
  - Update Docs For Subnet
  - Update Errors Docs