# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from shellev.api_helper import APIHelper
from shellev.models.chargesession_start_body import ChargesessionStartBody


class ChargingControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(ChargingControllerTests, cls).setUpClass()
        cls.controller = cls.client.charging
        cls.response_catcher = cls.controller.http_call_back

    # This endpoint start the charging session for the user.
    def test_start(self):
        # Parameters for the API call
        request_id = '123e4567-e89b-12d3-a456-426614174000'
        body = None

        # Perform the API call through the SDK function
        result = self.controller.start(request_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"requestId":"9d2dee33-7803-485a-a2b1-2c7538e597ee","status":"SUCC'
            'ESS","data":[{"sessionId":"c3e332f0-1bb2-4f50-a96b-e075bbb71e68"}]'
            '}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Accepts a request to stop an active session when a valid session id is provided.
    def test_stop(self):
        # Parameters for the API call
        request_id = '123e4567-e89b-12d3-a456-426614174000'
        session_id = 'c3e332f0-1bb2-4f50-a96b-e075bbb71e68'

        # Perform the API call through the SDK function
        result = self.controller.stop(request_id, session_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"requestId":"9d2dee33-7803-485a-a2b1-2c7538e597ee","status":"SUCC'
            'ESS"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # This endpoint returns the details of the session if the session is found.
    def test_get_charge_session_retrieve(self):
        # Parameters for the API call
        request_id = '123e4567-e89b-12d3-a456-426614174000'
        session_id = 'c3e332f0-1bb2-4f50-a96b-e075bbb71e68'

        # Perform the API call through the SDK function
        result = self.controller.get_charge_session_retrieve(request_id, session_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"requestId":"9d2dee33-7803-485a-a2b1-2c7538e597ee","status":"SUCC'
            'ESS","data":[{"id":"78b5d7a3-bdba-43d7-9851-1c84fcddb782","userId"'
            ':"281482b6-2c9a-4fd1-b3ea-1928edb40ef9","emaId":"NL-TNM-C00122045-'
            'K","evseId":"NL*TNM*E02003451*0","lastUpdated":"2024-06-19T07:36:5'
            '7.985998Z","startedAt":"2024-06-19T11:20:27Z","stoppedAt":"2014-06'
            '-19T12:20:27Z","sessionState":{"status":"Started"}}]}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Fetrches the active sessions for user.
    def test_active(self):
        # Parameters for the API call
        request_id = '123e4567-e89b-12d3-a456-426614174000'
        ema_id = 'NL-TNM-C0216599X-A'

        # Perform the API call through the SDK function
        result = self.controller.active(request_id, ema_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"requestId":"9d2dee33-7803-485a-a2b1-2c7538e597ee","status":"SUCC'
            'ESS","data":[{"id":"78b5d7a3-bdba-43d7-9851-1c84fcddb782","userId"'
            ':"281482b6-2c9a-4fd1-b3ea-1928edb40ef9","emaId":"NL-TNM-C00122045-'
            'K","evseId":"NL*TNM*E02003451*0","startedAt":"2015-08-19T11:20:27Z'
            '","stoppedAt":"2015-08-19T11:20:27Z","SessionState":{"status":"Sta'
            'rted"},"lastUpdated":"2024-07-17T07:36:57.985998Z"}]}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

