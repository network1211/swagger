# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class ReferfriendsOidctokenBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, qty: int=None, stock_id: int=None):  # noqa: E501
        """ReferfriendsOidctokenBody - a model defined in Swagger

        :param name: The name of this ReferfriendsOidctokenBody.  # noqa: E501
        :type name: str
        :param qty: The qty of this ReferfriendsOidctokenBody.  # noqa: E501
        :type qty: int
        :param stock_id: The stock_id of this ReferfriendsOidctokenBody.  # noqa: E501
        :type stock_id: int
        """
        self.swagger_types = {
            'name': str,
            'qty': int,
            'stock_id': int
        }

        self.attribute_map = {
            'name': 'name',
            'qty': 'qty',
            'stock_id': 'stock_id'
        }
        self._name = name
        self._qty = qty
        self._stock_id = stock_id

    @classmethod
    def from_dict(cls, dikt) -> 'ReferfriendsOidctokenBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The referfriends_oidctoken_body of this ReferfriendsOidctokenBody.  # noqa: E501
        :rtype: ReferfriendsOidctokenBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ReferfriendsOidctokenBody.

        Word  # noqa: E501

        :return: The name of this ReferfriendsOidctokenBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ReferfriendsOidctokenBody.

        Word  # noqa: E501

        :param name: The name of this ReferfriendsOidctokenBody.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def qty(self) -> int:
        """Gets the qty of this ReferfriendsOidctokenBody.


        :return: The qty of this ReferfriendsOidctokenBody.
        :rtype: int
        """
        return self._qty

    @qty.setter
    def qty(self, qty: int):
        """Sets the qty of this ReferfriendsOidctokenBody.


        :param qty: The qty of this ReferfriendsOidctokenBody.
        :type qty: int
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")  # noqa: E501

        self._qty = qty

    @property
    def stock_id(self) -> int:
        """Gets the stock_id of this ReferfriendsOidctokenBody.


        :return: The stock_id of this ReferfriendsOidctokenBody.
        :rtype: int
        """
        return self._stock_id

    @stock_id.setter
    def stock_id(self, stock_id: int):
        """Sets the stock_id of this ReferfriendsOidctokenBody.


        :param stock_id: The stock_id of this ReferfriendsOidctokenBody.
        :type stock_id: int
        """
        if stock_id is None:
            raise ValueError("Invalid value for `stock_id`, must not be `None`")  # noqa: E501

        self._stock_id = stock_id
