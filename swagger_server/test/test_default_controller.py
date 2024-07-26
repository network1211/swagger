# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2_xx import InlineResponse2XX  # noqa: E501
from swagger_server.models.inline_response2_xx1 import InlineResponse2XX1  # noqa: E501
from swagger_server.models.inline_response2_xx2 import InlineResponse2XX2  # noqa: E501
from swagger_server.models.inline_response2_xx3 import InlineResponse2XX3  # noqa: E501
from swagger_server.models.inline_response2_xx4 import InlineResponse2XX4  # noqa: E501
from swagger_server.models.referfriends_oidctoken_body import ReferfriendsOidctokenBody  # noqa: E501
from swagger_server.models.update_payment_info_by_id_dyn_body import UpdatePaymentInfoByIdDYNBody  # noqa: E501
from swagger_server.models.v2_move_order_body import V2MoveOrderBody  # noqa: E501
from swagger_server.models.v2_order_addresses_body import V2OrderAddressesBody  # noqa: E501
from swagger_server.models.v2_place_order_body import V2PlaceOrderBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_api_v1_auth_refer_friends_oidc_token_post(self):
        """Test case for api_v1_auth_refer_friends_oidc_token_post

        
        """
        body = ReferfriendsOidctokenBody()
        headers = [('accept_encoding', 'accept_encoding_example'),
                   ('postman_token', 'postman_token_example'),
                   ('x_volterra_truncated_hdr', 'x_volterra_truncated_hdr_example')]
        response = self.client.open(
            '/api/v1/auth/refer-friends/oidc-token',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v2_change_order_stop_limit_get(self):
        """Test case for api_v2_change_order_stop_limit_get

        
        """
        headers = [('accept_encoding', 'accept_encoding_example'),
                   ('postman_token', 'postman_token_example'),
                   ('x_volterra_truncated_hdr', 'x_volterra_truncated_hdr_example')]
        response = self.client.open(
            '/api/v2/changeOrderStopLimit',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v2_get_stock_get(self):
        """Test case for api_v2_get_stock_get

        
        """
        headers = [('accept_encoding', 'accept_encoding_example'),
                   ('postman_token', 'postman_token_example'),
                   ('x_volterra_truncated_hdr', 'x_volterra_truncated_hdr_example')]
        response = self.client.open(
            '/api/v2/getStock',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v2_move_order_get(self):
        """Test case for api_v2_move_order_get

        
        """
        headers = [('accept_encoding', 'accept_encoding_example'),
                   ('postman_token', 'postman_token_example'),
                   ('x_volterra_truncated_hdr', 'x_volterra_truncated_hdr_example')]
        response = self.client.open(
            '/api/v2/moveOrder',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v2_move_order_post(self):
        """Test case for api_v2_move_order_post

        
        """
        body = V2MoveOrderBody()
        headers = [('accept_encoding', 'accept_encoding_example'),
                   ('postman_token', 'postman_token_example'),
                   ('x_volterra_truncated_hdr', 'x_volterra_truncated_hdr_example')]
        response = self.client.open(
            '/api/v2/moveOrder',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v2_order_addresses_post(self):
        """Test case for api_v2_order_addresses_post

        
        """
        body = V2OrderAddressesBody()
        headers = [('accept_encoding', 'accept_encoding_example'),
                   ('postman_token', 'postman_token_example'),
                   ('x_volterra_truncated_hdr', 'x_volterra_truncated_hdr_example')]
        response = self.client.open(
            '/api/v2/orderAddresses',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v2_place_order_post(self):
        """Test case for api_v2_place_order_post

        
        """
        body = V2PlaceOrderBody()
        headers = [('accept_encoding', 'accept_encoding_example'),
                   ('postman_token', 'postman_token_example'),
                   ('x_volterra_truncated_hdr', 'x_volterra_truncated_hdr_example')]
        response = self.client.open(
            '/api/v2/placeOrder',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v2_update_payment_info_by_id_dynput(self):
        """Test case for api_v2_update_payment_info_by_id_dynput

        
        """
        body = UpdatePaymentInfoByIdDYNBody()
        headers = [('accept_encoding', 'accept_encoding_example'),
                   ('postman_token', 'postman_token_example'),
                   ('x_volterra_truncated_hdr', 'x_volterra_truncated_hdr_example')]
        response = self.client.open(
            '/api/v2/updatePaymentInfoById/{DYN}'.format(dyn='dyn_example'),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
