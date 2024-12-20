# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.bulk_account_contact_update import BulkAccountContactUpdate

class TestBulkAccountContactUpdate(unittest.TestCase):
    """BulkAccountContactUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkAccountContactUpdate:
        """Test BulkAccountContactUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkAccountContactUpdate`
        """
        model = BulkAccountContactUpdate()
        if include_optional:
            return BulkAccountContactUpdate(
                arena_id = 6,
                account_id = 7,
                account_contact_id = 7,
                label = 'label',
                is_main_contact = True,
                is_admin_contact = True,
                distribution_list = [1,2,3]
            )
        else:
            return BulkAccountContactUpdate(
                arena_id = 6,
                account_id = 7,
                account_contact_id = 7,
        )
        """

    def testBulkAccountContactUpdate(self):
        """Test BulkAccountContactUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
