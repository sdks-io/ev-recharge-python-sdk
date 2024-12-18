# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellev.api_helper import APIHelper


class Coordinates(object):

    """Implementation of the 'Coordinates' model.

    Coordinates of the Shell Recharge Site Location

    Attributes:
        latitude (float): Latitude of the Coordinate
        longitude (float): Longitude of the Coordinate

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "latitude": 'latitude',
        "longitude": 'longitude'
    }

    _optionals = [
        'latitude',
        'longitude',
    ]

    def __init__(self,
                 latitude=APIHelper.SKIP,
                 longitude=APIHelper.SKIP):
        """Constructor for the Coordinates class"""

        # Initialize members of the class
        if latitude is not APIHelper.SKIP:
            self.latitude = latitude 
        if longitude is not APIHelper.SKIP:
            self.longitude = longitude 

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
        latitude = dictionary.get("latitude") if dictionary.get("latitude") else APIHelper.SKIP
        longitude = dictionary.get("longitude") if dictionary.get("longitude") else APIHelper.SKIP
        # Return an object of this model
        return cls(latitude,
                   longitude)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
