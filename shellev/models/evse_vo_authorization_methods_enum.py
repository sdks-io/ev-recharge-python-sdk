# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class EvseVOAuthorizationMethodsEnum(object):

    """Implementation of the 'EvseVOAuthorizationMethods' enum.

    Methods that can be used to Authorize sessions on this EVSE

    Attributes:
        NEWMOTIONAPP: TODO: type description here.
        RFIDTOKEN: TODO: type description here.
        PNC: TODO: type description here.

    """
    _all_values = ['NewMotionApp', 'RFIDToken', 'PnC']
    NEWMOTIONAPP = 'NewMotionApp'

    RFIDTOKEN = 'RFIDToken'

    PNC = 'PnC'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   