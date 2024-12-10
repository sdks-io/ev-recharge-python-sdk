# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellev.api_helper import APIHelper


class InternalErrorObject(object):

    """Implementation of the 'InternalErrorObject' model.

    TODO: type model description here.

    Attributes:
        code (str): Error code
        message (str): Error description in English
        description (str): Technical details of the error message, the example
            which is given in the sample payload is one of the scenario.
            actual response will vary based on the technical nature

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "message": 'message',
        "description": 'description'
    }

    _optionals = [
        'code',
        'message',
        'description',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 message=APIHelper.SKIP,
                 description=APIHelper.SKIP):
        """Constructor for the InternalErrorObject class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if message is not APIHelper.SKIP:
            self.message = message 
        if description is not APIHelper.SKIP:
            self.description = description 

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   message,
                   description)
