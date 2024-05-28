# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SuccessResponse(object):

    """Implementation of the 'Success Response' model.

    TODO: type model description here.

    Attributes:
        request_id (str): A unique request id in GUID format. The value is
            written to the Shell API Platform audit log for end to end
            traceability of a request.
        status (ResponseBaseStatusEnum): Indicates overall status of the
            request

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "status": 'Status'
    }

    def __init__(self,
                 request_id=None,
                 status=None):
        """Constructor for the SuccessResponse class"""

        # Initialize members of the class
        self.request_id = request_id 
        self.status = status 

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
        # Return an object of this model
        return cls(request_id,
                   status)