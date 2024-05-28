# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ChargesessionStartBody(object):

    """Implementation of the 'chargesession_start_body' model.

    TODO: type model description here.

    Attributes:
        ev_charge_number (str): The EV Charge Number which can be found on the
            back of the Shell EV Card
        evse_id (str): Standard EVSE (Electric Vehicle Supply Equipment) Id
            identifier (ISO-IEC-15118)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ev_charge_number": 'EvChargeNumber',
        "evse_id": 'EvseId'
    }

    def __init__(self,
                 ev_charge_number=None,
                 evse_id=None):
        """Constructor for the ChargesessionStartBody class"""

        # Initialize members of the class
        self.ev_charge_number = ev_charge_number 
        self.evse_id = evse_id 

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
        ev_charge_number = dictionary.get("EvChargeNumber") if dictionary.get("EvChargeNumber") else None
        evse_id = dictionary.get("EvseId") if dictionary.get("EvseId") else None
        # Return an object of this model
        return cls(ev_charge_number,
                   evse_id)