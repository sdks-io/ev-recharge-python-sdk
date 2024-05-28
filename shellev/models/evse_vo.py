# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellev.api_helper import APIHelper
from shellev.models.connector_vo import ConnectorVO


class EvseVO(object):

    """Implementation of the 'EvseVO' model.

    Each Location will contain one or more EVSEs (Electric Vehicle Supply
    Equipment). Each EVSE is capable of charging one car at a time.

    Attributes:
        uid (int): Internal identifier used to refer to single individual 
            EVSE unit.
        external_id (str): Identifier of the Evse as given by the Operator,
            unique for that Operator
        evse_id (str): Standard EVSEId identifier (ISO-IEC-15118)
        status (EvseVOStatusEnum): The current status of the EVSE units
            availability
        connectors (List[ConnectorVO]): List of all connectors available on
            this EVSE unit.
        authorization_methods (EvseVOAuthorizationMethodsEnum): Methods that
            can be used to Authorize sessions on this EVSE
        updated (str): ISO8601-compliant UTC datetime of the last update of
            the EVSE
        deleted (str): optional  ISO8601-compliant UTC deletion timestamp of
            the Evse
        physical_reference (str): An optional number/string printed on the
            outside of the EVSE for visual identification

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "external_id": 'externalId',
        "evse_id": 'evseId',
        "status": 'status',
        "connectors": 'connectors',
        "authorization_methods": 'authorizationMethods',
        "updated": 'updated',
        "deleted": 'deleted',
        "physical_reference": 'physicalReference'
    }

    _optionals = [
        'uid',
        'external_id',
        'evse_id',
        'status',
        'connectors',
        'authorization_methods',
        'updated',
        'deleted',
        'physical_reference',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 external_id=APIHelper.SKIP,
                 evse_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 connectors=APIHelper.SKIP,
                 authorization_methods=APIHelper.SKIP,
                 updated=APIHelper.SKIP,
                 deleted=APIHelper.SKIP,
                 physical_reference=APIHelper.SKIP):
        """Constructor for the EvseVO class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if external_id is not APIHelper.SKIP:
            self.external_id = external_id 
        if evse_id is not APIHelper.SKIP:
            self.evse_id = evse_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if connectors is not APIHelper.SKIP:
            self.connectors = connectors 
        if authorization_methods is not APIHelper.SKIP:
            self.authorization_methods = authorization_methods 
        if updated is not APIHelper.SKIP:
            self.updated = updated 
        if deleted is not APIHelper.SKIP:
            self.deleted = deleted 
        if physical_reference is not APIHelper.SKIP:
            self.physical_reference = physical_reference 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        external_id = dictionary.get("externalId") if dictionary.get("externalId") else APIHelper.SKIP
        evse_id = dictionary.get("evseId") if dictionary.get("evseId") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        connectors = None
        if dictionary.get('connectors') is not None:
            connectors = [ConnectorVO.from_dictionary(x) for x in dictionary.get('connectors')]
        else:
            connectors = APIHelper.SKIP
        authorization_methods = dictionary.get("authorizationMethods") if dictionary.get("authorizationMethods") else APIHelper.SKIP
        updated = dictionary.get("updated") if dictionary.get("updated") else APIHelper.SKIP
        deleted = dictionary.get("deleted") if dictionary.get("deleted") else APIHelper.SKIP
        physical_reference = dictionary.get("physicalReference") if dictionary.get("physicalReference") else APIHelper.SKIP
        # Return an object of this model
        return cls(uid,
                   external_id,
                   evse_id,
                   status,
                   connectors,
                   authorization_methods,
                   updated,
                   deleted,
                   physical_reference)