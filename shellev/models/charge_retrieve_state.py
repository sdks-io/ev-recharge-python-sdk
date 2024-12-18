# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellev.api_helper import APIHelper
from shellev.models.charge_error import ChargeError


class ChargeRetrieveState(object):

    """Implementation of the 'ChargeRetrieveState' model.

    TODO: type model description here.

    Attributes:
        status (str): Describes the session state   started, stopped,
            start-requested, stop-requested, failed-to-start, failed-to-stop
        error (ChargeError): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'status',
        "error": 'error'
    }

    _optionals = [
        'status',
        'error',
    ]

    def __init__(self,
                 status=APIHelper.SKIP,
                 error=APIHelper.SKIP):
        """Constructor for the ChargeRetrieveState class"""

        # Initialize members of the class
        if status is not APIHelper.SKIP:
            self.status = status 
        if error is not APIHelper.SKIP:
            self.error = error 

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
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        error = ChargeError.from_dictionary(dictionary.get('error')) if 'error' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(status,
                   error)
