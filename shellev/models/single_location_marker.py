# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellev.api_helper import APIHelper
from shellev.models.coordinates import Coordinates


class SingleLocationMarker(object):

    """Implementation of the 'SingleLocationMarker' model.

    A Marker is a place on the map that represent a single Location

    Attributes:
        marker_type (str): Identifies the marker type. If it’s a
            `SingleLocationMarker`, then the value is `SingleLocation`
        unique_key (str): Uniquely identifies the marker object
        status (SingleLocationMarkerStatusEnum): TODO: type description here.
        coordinates (Coordinates): Coordinates of the Shell Recharge Site
            Location
        evse_count (float): Total number of Evse units in Locations that this
            Marker represents
        max_power (float): Maximum power in kW across all locations grouped in
            this marker (disregarding availability)
        geo_hash (str): GeoHash of marker coordinates
        location_uid (float): Unique ID of the Location this Marker represents
        authorization_methods
            (List[SingleLocationMarkerAuthorizationMethodsItemsEnum]): Methods
            that can be used to Authorize sessions on this EVSE
        operator_id (str): Unique Id of the operator

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "marker_type": 'markerType',
        "unique_key": 'uniqueKey',
        "status": 'status',
        "coordinates": 'coordinates',
        "evse_count": 'evseCount',
        "max_power": 'maxPower',
        "geo_hash": 'geoHash',
        "location_uid": 'locationUid',
        "authorization_methods": 'authorizationMethods',
        "operator_id": 'operatorId'
    }

    _optionals = [
        'unique_key',
        'status',
        'coordinates',
        'evse_count',
        'max_power',
        'geo_hash',
        'location_uid',
        'authorization_methods',
        'operator_id',
    ]

    def __init__(self,
                 marker_type=None,
                 unique_key=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 coordinates=APIHelper.SKIP,
                 evse_count=APIHelper.SKIP,
                 max_power=APIHelper.SKIP,
                 geo_hash=APIHelper.SKIP,
                 location_uid=APIHelper.SKIP,
                 authorization_methods=APIHelper.SKIP,
                 operator_id=APIHelper.SKIP):
        """Constructor for the SingleLocationMarker class"""

        # Initialize members of the class
        self.marker_type = marker_type 
        if unique_key is not APIHelper.SKIP:
            self.unique_key = unique_key 
        if status is not APIHelper.SKIP:
            self.status = status 
        if coordinates is not APIHelper.SKIP:
            self.coordinates = coordinates 
        if evse_count is not APIHelper.SKIP:
            self.evse_count = evse_count 
        if max_power is not APIHelper.SKIP:
            self.max_power = max_power 
        if geo_hash is not APIHelper.SKIP:
            self.geo_hash = geo_hash 
        if location_uid is not APIHelper.SKIP:
            self.location_uid = location_uid 
        if authorization_methods is not APIHelper.SKIP:
            self.authorization_methods = authorization_methods 
        if operator_id is not APIHelper.SKIP:
            self.operator_id = operator_id 

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
        marker_type = dictionary.get("markerType") if dictionary.get("markerType") else None
        unique_key = dictionary.get("uniqueKey") if dictionary.get("uniqueKey") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        coordinates = Coordinates.from_dictionary(dictionary.get('coordinates')) if 'coordinates' in dictionary.keys() else APIHelper.SKIP
        evse_count = dictionary.get("evseCount") if dictionary.get("evseCount") else APIHelper.SKIP
        max_power = dictionary.get("maxPower") if dictionary.get("maxPower") else APIHelper.SKIP
        geo_hash = dictionary.get("geoHash") if dictionary.get("geoHash") else APIHelper.SKIP
        location_uid = dictionary.get("locationUid") if dictionary.get("locationUid") else APIHelper.SKIP
        authorization_methods = dictionary.get("authorizationMethods") if dictionary.get("authorizationMethods") else APIHelper.SKIP
        operator_id = dictionary.get("operatorId") if dictionary.get("operatorId") else APIHelper.SKIP
        # Return an object of this model
        return cls(marker_type,
                   unique_key,
                   status,
                   coordinates,
                   evse_count,
                   max_power,
                   geo_hash,
                   location_uid,
                   authorization_methods,
                   operator_id)

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
            return APIHelper.is_valid_type(value=dictionary.marker_type,
                                           type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('markerType'),
                                       type_callable=lambda value: isinstance(value, str))
