# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.api.distribution_api import DistributionApi


class TestDistributionApi(unittest.TestCase):
    """DistributionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DistributionApi()

    def tearDown(self) -> None:
        pass

    def test_get_distribution(self) -> None:
        """Test case for get_distribution

        Get distribution
        """
        pass


if __name__ == '__main__':
    unittest.main()
