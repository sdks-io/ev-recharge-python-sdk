# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from shellev.configuration import Configuration
from shellev.controllers.base_controller import BaseController
from shellev.configuration import Environment
from shellev.http.auth.o_auth_2 import OAuth2
from shellev.controllers.locations_controller import LocationsController
from shellev.controllers.charging_controller import ChargingController
from shellev.controllers.o_auth_authorization_controller\
    import OAuthAuthorizationController


class ShellevClient(object):
    @LazyProperty
    def locations(self):
        return LocationsController(self.global_configuration)

    @LazyProperty
    def charging(self):
        return ChargingController(self.global_configuration)

    @LazyProperty
    def o_auth_authorization(self):
        return OAuthAuthorizationController(self.global_configuration)

    @property
    def bearer_auth(self):
        return self.auth_managers['BearerAuth']

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.PRODUCTION, o_auth_client_id=None,
                 o_auth_client_secret=None, o_auth_token=None,
                 client_credentials_auth_credentials=None, config=None):
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, o_auth_client_id=o_auth_client_id,
            o_auth_client_secret=o_auth_client_secret,
            o_auth_token=o_auth_token,
            client_credentials_auth_credentials=client_credentials_auth_credentials)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())

        self.auth_managers = {key: None for key in ['BearerAuth']}
        self.auth_managers['BearerAuth'] = OAuth2(
            self.config.client_credentials_auth_credentials,
            self.global_configuration)
        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)

