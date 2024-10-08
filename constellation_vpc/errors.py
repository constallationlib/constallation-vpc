import re as _re


class ClientNotFoundError(Exception):
    def __init__(self):
        super().__init__(
            "It appears like the AWS CLI client is not installed! To fix please visit 'https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html'")


class SubnetError(Exception):
    def __init__(self, operation, message, *args):
        self.operation = operation
        self.message = message
        super().__init__(message, *args)


class SubnetCIDRConflicts(SubnetError):
    def __init__(self, operation, original_message, *args):
        if (cidr_match := _re.search(r"'(.*?)'", original_message)):
            cidr = cidr_match.group(1)
            formatted_message = f"The CIDR {cidr} conflicts with another subnet"
        else:
            formatted_message = "The CIDR conflicts with another subnet"
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidSubnet.Conflict"


class SubnetRangeError(SubnetError):
    def __init__(self, operation, original_message, *args):
        if (range_match := _re.search(r"'(.*?)'", original_message)):
            ip_range = range_match.group(1)
            formatted_message = f"The IP range {ip_range} is invalid or out of range"
        else:
            formatted_message = "The IP range is invalid or out of range"
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidSubnet.Range"


class SubnetIDNotFound(SubnetError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The specified subnet ID was not found."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidSubnet.ID.NotFound"


class SubnetZoneMismatch(SubnetError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The specified subnet is in the wrong availability zone."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidSubnet.ZoneMismatch"


class SubnetInUse(SubnetError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The subnet is currently in use and cannot be modified or deleted."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidSubnet.InUse"


class SubnetAssociationError(SubnetError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "There was an error associating the subnet with the specified resource."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidSubnet.Association"


class SubnetDependentServiceError(SubnetError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The subnet is being used by a dependent service and cannot be modified or deleted."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidSubnet.DependentService"


class SubnetAttachmentError(SubnetError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "There was an error attaching the subnet to the specified resource."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidSubnet.Attachment"


class VPCError(Exception):
    def __init__(self, operation, message, *args):
        self.operation = operation
        self.message = message
        super().__init__(message, *args)


class VPCCIDRConflicts(VPCError):
    def __init__(self, operation, original_message, *args):
        if (cidr_match := _re.search(r"'(.*?)'", original_message)):
            cidr = cidr_match.group(1)
            formatted_message = f"The CIDR {cidr} conflicts with another VPC"
        else:
            formatted_message = "The CIDR conflicts with another VPC"
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidVpc.Conflict"


class VPCIDNotFound(VPCError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The specified VPC ID was not found."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidVpc.ID.NotFound"


class VPCInUse(VPCError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The VPC is currently in use and cannot be modified or deleted."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidVpc.InUse"


class VPCDependentServiceError(VPCError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The VPC is being used by a dependent service and cannot be modified or deleted."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidVpc.DependentService"


class VPCAttachmentError(VPCError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "There was an error attaching the VPC to the specified resource."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidVpc.Attachment"


class RouteTableIDNotFound(VPCError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The specified route table ID was not found."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidRouteTableID.NotFound"


class InvalidRouteTableIDMalformed(VPCError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The specified route table ID is malformed."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidRouteTableID.Malformed"


class RouteNotFound(VPCError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The specified route was not found."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidRoute.NotFound"


class RouteAlreadyExists(VPCError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The specified route already exists."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "RouteAlreadyExists"


class InvalidRouteTableAssociationIDNotFound(VPCError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The specified route table association ID was not found."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidRouteTableAssociationID.NotFound"


class AccessDeniedError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "Access denied. You do not have the necessary permissions for this operation."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "AccessDenied"


class UnauthorizedOperationError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "You are not authorized to perform this operation."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "UnauthorizedOperation"


class AuthFailureError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "Authentication failed. Please check your AWS credentials."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "AuthFailure"


class RequestLimitExceededError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "Request limit exceeded. Please wait and try again later."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "RequestLimitExceeded"


class ThrottlingExceptionError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "Request was throttled. Please wait and try again later."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "ThrottlingException"


class ResourceNotFoundExceptionError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "The specified resource could not be found."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "ResourceNotFoundException"


class InvalidParameterValueError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "One or more parameters are invalid. Please check the input values."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidParameterValue"


class ServiceUnavailableError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "The service is currently unavailable. Please try again later."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "ServiceUnavailable"


class InternalFailureError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "An internal error occurred. Please try again later."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InternalFailure"


class ValidationExceptionError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "The input provided does not meet the required constraints."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "ValidationException"


class InvalidClientTokenIdError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "The security token included in the request is invalid."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidClientTokenId"


class OptInRequiredError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "You must opt in to use this service."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "OptInRequired"


class DependencyViolationError(Exception):
    def __init__(self, operation, message, *args):
        formatted_message = "The request failed because a resource is dependent on this resource."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "DependencyViolation"


class NatGatewayError(Exception):
    def __init__(self, operation, message, *args):
        self.operation = operation
        self.message = message
        super().__init__(message, *args)


class NatGatewayIDNotFound(NatGatewayError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The specified NAT Gateway ID was not found."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidNatGatewayID.NotFound"


class NatGatewayInUse(NatGatewayError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The NAT Gateway is currently in use and cannot be deleted."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidNatGateway.InUse"


class NatGatewayLimitExceeded(NatGatewayError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The maximum number of NAT Gateways has been reached."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "NatGatewayLimitExceeded"


class NatGatewayNotFound(NatGatewayError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The NAT Gateway was not found."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "NatGatewayNotFound"


class NatGatewayDependencyViolation(NatGatewayError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The NAT Gateway is being used by a dependent resource and cannot be deleted."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "NatGatewayDependencyViolation"


class PeeringConnectionError(Exception):
    def __init__(self, operation, message, *args):
        self.operation = operation
        self.message = message
        super().__init__(message, *args)


class PeeringConnectionIDNotFound(PeeringConnectionError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The specified VPC Peering Connection ID was not found."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidVpcPeeringConnectionID.NotFound"


class PeeringConnectionAlreadyExists(PeeringConnectionError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The specified VPC Peering Connection already exists."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "VpcPeeringConnectionAlreadyExists"


class PeeringConnectionLimitExceeded(PeeringConnectionError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The maximum number of VPC Peering Connections has been reached."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "VpcPeeringConnectionLimitExceeded"


class PeeringConnectionInUse(PeeringConnectionError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The VPC Peering Connection is currently in use and cannot be deleted."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidVpcPeeringConnection.InUse"


class PeeringConnectionInvalidState(PeeringConnectionError):
    def __init__(self, operation, original_message, *args):
        formatted_message = "The VPC Peering Connection is in an invalid state."
        super().__init__(operation, formatted_message, *args)
        self.error_code = "VpcPeeringConnectionInvalidState"


class UnknownAWSClientError(Exception):
    def __init__(self, error_code):
        super().__init__(f"PLEASE READ: The AWS Client threw an unknown error code '{error_code}'! Please report this immediatly by submitting an issue on https://github.com/constallationlib/constallation-vpc and using the tag 'Unknown Client Code'")
        exit(0) # Halt immediately

class ErrorHandler:
    def parse_and_raise(self, error):
        error_message = error.get('Error', '')
        code_match = _re.search(r'\((.*?)\)', error_message)
        operation_match = _re.search(r'when calling the (.*?) operation', error_message)

        if code_match and operation_match:
            error_code = code_match.group(1)
            operation = operation_match.group(1)

            if error_code == "InvalidSubnet.Conflict":
                raise SubnetCIDRConflicts(operation, error_message)
            elif error_code == "InvalidSubnet.Range":
                raise SubnetRangeError(operation, error_message)
            elif error_code == "InvalidSubnet.ID.NotFound":
                raise SubnetIDNotFound(operation, error_message)
            elif error_code == "InvalidSubnet.ZoneMismatch":
                raise SubnetZoneMismatch(operation, error_message)
            elif error_code == "InvalidSubnet.InUse":
                raise SubnetInUse(operation, error_message)
            elif error_code == "InvalidSubnet.Association":
                raise SubnetAssociationError(operation, error_message)
            elif error_code == "InvalidSubnet.DependentService":
                raise SubnetDependentServiceError(operation, error_message)
            elif error_code == "InvalidSubnet.Attachment":
                raise SubnetAttachmentError(operation, error_message)
            elif error_code == "InvalidVpc.Conflict":
                raise VPCCIDRConflicts(operation, error_message)
            elif error_code == "InvalidVpc.ID.NotFound":
                raise VPCIDNotFound(operation, error_message)
            elif error_code == "InvalidVpc.InUse":
                raise VPCInUse(operation, error_message)
            elif error_code == "InvalidVpc.DependentService":
                raise VPCDependentServiceError(operation, error_message)
            elif error_code == "InvalidVpc.Attachment":
                raise VPCAttachmentError(operation, error_message)
            elif error_code == "InvalidRouteTableID.NotFound":
                raise RouteTableIDNotFound(operation, error_message)
            elif error_code == "InvalidRouteTableID.Malformed":
                raise InvalidRouteTableIDMalformed(operation, error_message)
            elif error_code == "InvalidRouteTableAssociationID.NotFound":
                raise InvalidRouteTableAssociationIDNotFound(operation, error_message)
            elif error_code == "InvalidRoute.NotFound":
                raise RouteNotFound(operation, error_message)
            elif error_code == "RouteAlreadyExists":
                raise RouteAlreadyExists(operation, error_message)
            elif error_code == "AccessDenied":
                raise AccessDeniedError(operation, error_message)
            elif error_code == "UnauthorizedOperation":
                raise UnauthorizedOperationError(operation, error_message)
            elif error_code == "AuthFailure":
                raise AuthFailureError(operation, error_message)
            elif error_code == "RequestLimitExceeded":
                raise RequestLimitExceededError(operation, error_message)
            elif error_code == "ThrottlingException":
                raise ThrottlingExceptionError(operation, error_message)
            elif error_code == "ResourceNotFoundException":
                raise ResourceNotFoundExceptionError(operation, error_message)
            elif error_code == "InvalidParameterValue":
                raise InvalidParameterValueError(operation, error_message)
            elif error_code == "ServiceUnavailable":
                raise ServiceUnavailableError(operation, error_message)
            elif error_code == "InternalFailure":
                raise InternalFailureError(operation, error_message)
            elif error_code == "ValidationException":
                raise ValidationExceptionError(operation, error_message)
            elif error_code == "InvalidClientTokenId":
                raise InvalidClientTokenIdError(operation, error_message)
            elif error_code == "OptInRequired":
                raise OptInRequiredError(operation, error_message)
            elif error_code == "DependencyViolation":
                raise DependencyViolationError(operation, error_message)
            elif error_code == "InvalidNatGatewayID.NotFound":
                raise NatGatewayIDNotFound(operation, error_message)
            elif error_code == "InvalidNatGateway.InUse":
                raise NatGatewayInUse(operation, error_message)
            elif error_code == "NatGatewayLimitExceeded":
                raise NatGatewayLimitExceeded(operation, error_message)
            elif error_code == "NatGatewayNotFound":
                raise NatGatewayNotFound(operation, error_message)
            elif error_code == "NatGatewayDependencyViolation":
                raise NatGatewayDependencyViolation(operation, error_message)
            elif error_code == "InvalidVpcPeeringConnectionID.NotFound":
                raise PeeringConnectionIDNotFound(operation, error_message)
            elif error_code == "VpcPeeringConnectionAlreadyExists":
                raise PeeringConnectionAlreadyExists(operation, error_message)
            elif error_code == "VpcPeeringConnectionLimitExceeded":
                raise PeeringConnectionLimitExceeded(operation, error_message)
            elif error_code == "InvalidVpcPeeringConnection.InUse":
                raise PeeringConnectionInUse(operation, error_message)
            elif error_code == "VpcPeeringConnectionInvalidState":
                raise PeeringConnectionInvalidState(operation, error_message)
            else:
                raise UnknownAWSClientError(error_code)
        else:
            raise Exception("Unknown error occurred without specific details")
