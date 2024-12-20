# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.api.arenas_api import ArenasApi


class TestArenasApi(unittest.TestCase):
    """ArenasApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ArenasApi()

    def tearDown(self) -> None:
        pass

    def test_get_allocation_types(self) -> None:
        """Test case for get_allocation_types

        Get a list of allocation types for the given arena
        """
        pass

    def test_get_arena(self) -> None:
        """Test case for get_arena

        Get arena
        """
        pass

    def test_get_arena_net_income_types(self) -> None:
        """Test case for get_arena_net_income_types

        Get allocation types for a given arena by ID
        """
        pass

    def test_get_arena_payment_settings(self) -> None:
        """Test case for get_arena_payment_settings

        Get payment settings for a given arena
        """
        pass

    def test_get_arenas(self) -> None:
        """Test case for get_arenas

        Get a list of Arenas
        """
        pass


if __name__ == '__main__':
    unittest.main()
