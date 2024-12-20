# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.api.accounts_api import AccountsApi


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccountsApi()

    def tearDown(self) -> None:
        pass

    def test_account_contact_bulk_remove(self) -> None:
        """Test case for account_contact_bulk_remove

        API for account contact bulk removal
        """
        pass

    def test_account_contact_bulk_update(self) -> None:
        """Test case for account_contact_bulk_update

        API for account contact bulk update
        """
        pass

    def test_account_contact_change_notify(self) -> None:
        """Test case for account_contact_change_notify

        API for account contact change notification
        """
        pass


if __name__ == '__main__':
    unittest.main()