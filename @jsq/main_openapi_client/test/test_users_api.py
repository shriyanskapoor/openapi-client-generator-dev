# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.api.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()

    def tearDown(self) -> None:
        pass

    def test_get_accounts_edit_access(self) -> None:
        """Test case for get_accounts_edit_access

        Get accounts with edit access
        """
        pass

    def test_get_user_arena_roles(self) -> None:
        """Test case for get_user_arena_roles

        Get roles for each arena
        """
        pass

    def test_get_user_distribution_batch(self) -> None:
        """Test case for get_user_distribution_batch

        Get distribution batch with authorization checks
        """
        pass

    def test_get_user_distribution_batch_distributions(self) -> None:
        """Test case for get_user_distribution_batch_distributions

        Get distribution batch distributions for a user_id with authorization checks
        """
        pass

    def test_get_users(self) -> None:
        """Test case for get_users

        Get users
        """
        pass


if __name__ == '__main__':
    unittest.main()