import re


class SubnetError(Exception):
    def __init__(self, operation, message, *args):
        self.operation = operation
        self.message = message
        super().__init__(message, *args)


class InvalidSubnetCIDR(SubnetError):
    def __init__(self, operation, original_message, *args):
        cidr_match = re.search(r"'(.*?)'", original_message)
        if cidr_match:
            cidr = cidr_match.group(1)
            formatted_message = f"The CIDR {cidr} conflicts with another subnet"
        else:
            formatted_message = "The CIDR conflicts with another subnet"

        super().__init__(operation, formatted_message, *args)
        self.error_code = "InvalidSubnet.Conflict"


class ErrorHandler:
    def parse_and_raise(self, error_dict):
        # Extract the error message
        error_message = error_dict.get('Error', '')

        # Use regex to extract the error code and operation from the error message
        code_match = re.search(r'\((.*?)\)', error_message)
        operation_match = re.search(r'when calling the (.*?) operation', error_message)

        if code_match and operation_match:
            error_code = code_match.group(1)
            operation = operation_match.group(1)

            # Raise the appropriate error based on the error code
            if error_code == "InvalidSubnet.Conflict":
                raise InvalidSubnetCIDR(operation, error_message)
            else:
                raise SubnetError(operation, error_message)
        else:
            raise SubnetError("UnknownOperation", error_message)