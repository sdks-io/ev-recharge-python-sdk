# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellev.api_helper import APIHelper


class OpeningHoursObject(object):

    """Implementation of the 'OpeningHoursObject' model.

    TODO: type model description here.

    Attributes:
        week_day (OpeningHoursObjectWeekDayEnum): 3 letter day of the week
        start_time (str): Hour in 24h local time when the location opens.
        end_time (str): Hour in 24h local time when the location closes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "week_day": 'weekDay',
        "start_time": 'startTime',
        "end_time": 'endTime'
    }

    _optionals = [
        'week_day',
        'start_time',
        'end_time',
    ]

    def __init__(self,
                 week_day=APIHelper.SKIP,
                 start_time=APIHelper.SKIP,
                 end_time=APIHelper.SKIP):
        """Constructor for the OpeningHoursObject class"""

        # Initialize members of the class
        if week_day is not APIHelper.SKIP:
            self.week_day = week_day 
        if start_time is not APIHelper.SKIP:
            self.start_time = start_time 
        if end_time is not APIHelper.SKIP:
            self.end_time = end_time 

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
        week_day = dictionary.get("weekDay") if dictionary.get("weekDay") else APIHelper.SKIP
        start_time = dictionary.get("startTime") if dictionary.get("startTime") else APIHelper.SKIP
        end_time = dictionary.get("endTime") if dictionary.get("endTime") else APIHelper.SKIP
        # Return an object of this model
        return cls(week_day,
                   start_time,
                   end_time)