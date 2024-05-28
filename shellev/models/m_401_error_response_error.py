# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellev.api_helper import APIHelper


class M401ErrorResponseError(object):

    """Implementation of the '401ErrorResponse_Error' model.

    TODO: type model description here.

    Attributes:
        code (str): Error code that logically best represents the error
            encountered
        title (str): Description of the error type
        detail (str): Details of the error that can help under the cause of
            the error
        additional_info (Dict[str, str]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'Code',
        "title": 'Title',
        "detail": 'Detail',
        "additional_info": 'AdditionalInfo'
    }

    _optionals = [
        'additional_info',
    ]

    _nullables = [
        'additional_info',
    ]

    def __init__(self,
                 code=None,
                 title=None,
                 detail=None,
                 additional_info=APIHelper.SKIP):
        """Constructor for the M401ErrorResponseError class"""

        # Initialize members of the class
        self.code = code 
        self.title = title 
        self.detail = detail 
        if additional_info is not APIHelper.SKIP:
            self.additional_info = additional_info 

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
        code = dictionary.get("Code") if dictionary.get("Code") else None
        title = dictionary.get("Title") if dictionary.get("Title") else None
        detail = dictionary.get("Detail") if dictionary.get("Detail") else None
        additional_info = dictionary.get("AdditionalInfo") if "AdditionalInfo" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   title,
                   detail,
                   additional_info)