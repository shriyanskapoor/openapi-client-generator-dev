# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.api.positions_api import PositionsApi


class TestPositionsApi(unittest.TestCase):
    """PositionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PositionsApi()

    def tearDown(self) -> None:
        pass

    def test_get_external_position(self) -> None:
        """Test case for get_external_position

        Gets position of a specific arena and source
        """
        pass

    def test_get_opco_positions(self) -> None:
        """Test case for get_opco_positions

        Get a list of the entity's positions in its directly-owned operating companies.
        """
        pass

    def test_get_positions_attributes(self) -> None:
        """Test case for get_positions_attributes

        Gets positions by ids with account, investor group, and investment entity ids.
        """
        pass


if __name__ == '__main__':
    unittest.main()
