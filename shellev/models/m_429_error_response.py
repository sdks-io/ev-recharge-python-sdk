# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellev.api_helper import APIHelper
from shellev.models.m_429_error_response_error import M429ErrorResponseError


class M429ErrorResponse(object):

    """Implementation of the '429ErrorResponse' model.

    Too Many Requests

    Attributes:
        request_id (str): Mandatory UUID (according to RFC 4122 standards) for
            requests and responses. This will be played back in the response
            from the request.
        status (str): Indicates overall status of the request
        errors (List[M429ErrorResponseError]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "status": 'Status',
        "errors": 'Errors'
    }

    _optionals = [
        'errors',
    ]

    def __init__(self,
                 request_id=None,
                 status=None,
                 errors=APIHelper.SKIP):
        """Constructor for the M429ErrorResponse class"""

        # Initialize members of the class
        self.request_id = request_id 
        self.status = status 
        if errors is not APIHelper.SKIP:
            self.errors = errors 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else None
        status = dictionary.get("Status") if dictionary.get("Status") else None
        errors = None
        if dictionary.get('Errors') is not None:
            errors = [M429ErrorResponseError.from_dictionary(x) for x in dictionary.get('Errors')]
        else:
            errors = APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   status,
                   errors)
