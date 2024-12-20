# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.bulk_account_contact_change_notify import BulkAccountContactChangeNotify

class TestBulkAccountContactChangeNotify(unittest.TestCase):
    """BulkAccountContactChangeNotify unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkAccountContactChangeNotify:
        """Test BulkAccountContactChangeNotify
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkAccountContactChangeNotify`
        """
        model = BulkAccountContactChangeNotify()
        if include_optional:
            return BulkAccountContactChangeNotify(
                request_type = 'UPDATE_CONTACT',
                request_payloads = [
                    main_openapi_client.models.bulk_account_contact_change_notify_request_payloads_inner.BulkAccountContactChangeNotify_request_payloads_inner(
                        arena_id = 1, 
                        account_id = 2, 
                        contact_id = 3, 
                        comment = 'comment', )
                    ]
            )
        else:
            return BulkAccountContactChangeNotify(
        )
        """

    def testBulkAccountContactChangeNotify(self):
        """Test BulkAccountContactChangeNotify"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
