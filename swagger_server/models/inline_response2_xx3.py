# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2XX3(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, created_at: str=None, id: str=None, name: str=None, order_id: int=None, price: str=None, qty: int=None, stock_id: int=None, updated_at: str=None):  # noqa: E501
        """InlineResponse2XX3 - a model defined in Swagger

        :param created_at: The created_at of this InlineResponse2XX3.  # noqa: E501
        :type created_at: str
        :param id: The id of this InlineResponse2XX3.  # noqa: E501
        :type id: str
        :param name: The name of this InlineResponse2XX3.  # noqa: E501
        :type name: str
        :param order_id: The order_id of this InlineResponse2XX3.  # noqa: E501
        :type order_id: int
        :param price: The price of this InlineResponse2XX3.  # noqa: E501
        :type price: str
        :param qty: The qty of this InlineResponse2XX3.  # noqa: E501
        :type qty: int
        :param stock_id: The stock_id of this InlineResponse2XX3.  # noqa: E501
        :type stock_id: int
        :param updated_at: The updated_at of this InlineResponse2XX3.  # noqa: E501
        :type updated_at: str
        """
        self.swagger_types = {
            'created_at': str,
            'id': str,
            'name': str,
            'order_id': int,
            'price': str,
            'qty': int,
            'stock_id': int,
            'updated_at': str
        }

        self.attribute_map = {
            'created_at': 'created_at',
            'id': 'id',
            'name': 'name',
            'order_id': 'order_id',
            'price': 'price',
            'qty': 'qty',
            'stock_id': 'stock_id',
            'updated_at': 'updated_at'
        }
        self._created_at = created_at
        self._id = id
        self._name = name
        self._order_id = order_id
        self._price = price
        self._qty = qty
        self._stock_id = stock_id
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2XX3':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_2XX_3 of this InlineResponse2XX3.  # noqa: E501
        :rtype: InlineResponse2XX3
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_at(self) -> str:
        """Gets the created_at of this InlineResponse2XX3.


        :return: The created_at of this InlineResponse2XX3.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this InlineResponse2XX3.


        :param created_at: The created_at of this InlineResponse2XX3.
        :type created_at: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self) -> str:
        """Gets the id of this InlineResponse2XX3.


        :return: The id of this InlineResponse2XX3.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this InlineResponse2XX3.


        :param id: The id of this InlineResponse2XX3.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this InlineResponse2XX3.


        :return: The name of this InlineResponse2XX3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InlineResponse2XX3.


        :param name: The name of this InlineResponse2XX3.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def order_id(self) -> int:
        """Gets the order_id of this InlineResponse2XX3.


        :return: The order_id of this InlineResponse2XX3.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id: int):
        """Sets the order_id of this InlineResponse2XX3.


        :param order_id: The order_id of this InlineResponse2XX3.
        :type order_id: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def price(self) -> str:
        """Gets the price of this InlineResponse2XX3.


        :return: The price of this InlineResponse2XX3.
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price: str):
        """Sets the price of this InlineResponse2XX3.


        :param price: The price of this InlineResponse2XX3.
        :type price: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def qty(self) -> int:
        """Gets the qty of this InlineResponse2XX3.


        :return: The qty of this InlineResponse2XX3.
        :rtype: int
        """
        return self._qty

    @qty.setter
    def qty(self, qty: int):
        """Sets the qty of this InlineResponse2XX3.


        :param qty: The qty of this InlineResponse2XX3.
        :type qty: int
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")  # noqa: E501

        self._qty = qty

    @property
    def stock_id(self) -> int:
        """Gets the stock_id of this InlineResponse2XX3.


        :return: The stock_id of this InlineResponse2XX3.
        :rtype: int
        """
        return self._stock_id

    @stock_id.setter
    def stock_id(self, stock_id: int):
        """Sets the stock_id of this InlineResponse2XX3.


        :param stock_id: The stock_id of this InlineResponse2XX3.
        :type stock_id: int
        """
        if stock_id is None:
            raise ValueError("Invalid value for `stock_id`, must not be `None`")  # noqa: E501

        self._stock_id = stock_id

    @property
    def updated_at(self) -> str:
        """Gets the updated_at of this InlineResponse2XX3.


        :return: The updated_at of this InlineResponse2XX3.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: str):
        """Sets the updated_at of this InlineResponse2XX3.


        :param updated_at: The updated_at of this InlineResponse2XX3.
        :type updated_at: str
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at
