import connexion
import six

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
from swagger_server import util


def api_v1_auth_refer_friends_oidc_token_post(body=None, accept_encoding=None, postman_token=None, x_volterra_truncated_hdr=None):  # noqa: E501
    """api_v1_auth_refer_friends_oidc_token_post

    Swagger auto-generated from learnt schema # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param accept_encoding: 
    :type accept_encoding: str
    :param postman_token: Word
    :type postman_token: str
    :param x_volterra_truncated_hdr: Word
    :type x_volterra_truncated_hdr: str

    :rtype: InlineResponse2XX
    """
    if connexion.request.is_json:
        body = ReferfriendsOidctokenBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_v2_change_order_stop_limit_get(accept_encoding=None, postman_token=None, x_volterra_truncated_hdr=None):  # noqa: E501
    """api_v2_change_order_stop_limit_get

    Swagger auto-generated from learnt schema # noqa: E501

    :param accept_encoding: 
    :type accept_encoding: str
    :param postman_token: Word
    :type postman_token: str
    :param x_volterra_truncated_hdr: Word
    :type x_volterra_truncated_hdr: str

    :rtype: None
    """
    return 'do some magic!'

def api_v2_get_stock_get(accept_encoding=None, postman_token=None, x_volterra_truncated_hdr=None):  # noqa: E501
    """api_v2_get_stock_get

    Swagger auto-generated from learnt schema # noqa: E501

    :param accept_encoding: 
    :type accept_encoding: str
    :param postman_token: Word
    :type postman_token: str
    :param x_volterra_truncated_hdr: Word
    :type x_volterra_truncated_hdr: str

    :rtype: List[Object]
    """
    # Example data to return. You should replace this with actual logic.
    example_data = [
        {
            "productID": 1,
            "name": "Example Product 1",
            "description": "Description for product 1",
            "price": 100
        },
        {
            "productID": 2,
            "name": "Example Product 2",
            "description": "Description for product 2",
            "price": 200
        }
    ]
    
    return example_data

def api_v2_move_order_get(accept_encoding=None, postman_token=None, x_volterra_truncated_hdr=None):  # noqa: E501
    """api_v2_move_order_get

    Swagger auto-generated from learnt schema # noqa: E501

    :param accept_encoding: 
    :type accept_encoding: str
    :param postman_token: Word
    :type postman_token: str
    :param x_volterra_truncated_hdr: Word
    :type x_volterra_truncated_hdr: str

    :rtype: List[Object]
    """
    return 'do some magic!'


def api_v2_move_order_post(body=None, accept_encoding=None, postman_token=None, x_volterra_truncated_hdr=None):  # noqa: E501
    """api_v2_move_order_post

    Swagger auto-generated from learnt schema # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param accept_encoding: 
    :type accept_encoding: str
    :param postman_token: Word
    :type postman_token: str
    :param x_volterra_truncated_hdr: Word
    :type x_volterra_truncated_hdr: str

    :rtype: List[InlineResponse2XX1]
    """
    if connexion.request.is_json:
        body = V2MoveOrderBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_v2_order_addresses_post(body=None, accept_encoding=None, postman_token=None, x_volterra_truncated_hdr=None):  # noqa: E501
    """api_v2_order_addresses_post

    Swagger auto-generated from learnt schema # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param accept_encoding: 
    :type accept_encoding: str
    :param postman_token: Word
    :type postman_token: str
    :param x_volterra_truncated_hdr: Word
    :type x_volterra_truncated_hdr: str

    :rtype: InlineResponse2XX2
    """
    if connexion.request.is_json:
        body = V2OrderAddressesBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_v2_place_order_post(body=None, accept_encoding=None, postman_token=None, x_volterra_truncated_hdr=None):  # noqa: E501
    """api_v2_place_order_post

    Swagger auto-generated from learnt schema # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param accept_encoding: 
    :type accept_encoding: str
    :param postman_token: Word
    :type postman_token: str
    :param x_volterra_truncated_hdr: Word
    :type x_volterra_truncated_hdr: str

    :rtype: InlineResponse2XX3
    """
    if connexion.request.is_json:
        body = V2PlaceOrderBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_v2_update_payment_info_by_id_dynput(dyn, body=None, accept_encoding=None, postman_token=None, x_volterra_truncated_hdr=None):  # noqa: E501
    """api_v2_update_payment_info_by_id_dynput

    Swagger auto-generated from learnt schema # noqa: E501

    :param dyn: 
    :type dyn: str
    :param body: 
    :type body: dict | bytes
    :param accept_encoding: 
    :type accept_encoding: str
    :param postman_token: Word
    :type postman_token: str
    :param x_volterra_truncated_hdr: Word
    :type x_volterra_truncated_hdr: str

    :rtype: InlineResponse2XX4
    """
    if connexion.request.is_json:
        body = UpdatePaymentInfoByIdDYNBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
