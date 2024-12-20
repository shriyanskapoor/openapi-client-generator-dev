# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.bulk_account_contact_update_request_body import BulkAccountContactUpdateRequestBody

class TestBulkAccountContactUpdateRequestBody(unittest.TestCase):
    """BulkAccountContactUpdateRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkAccountContactUpdateRequestBody:
        """Test BulkAccountContactUpdateRequestBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkAccountContactUpdateRequestBody`
        """
        model = BulkAccountContactUpdateRequestBody()
        if include_optional:
            return BulkAccountContactUpdateRequestBody(
                metadata = main_openapi_client.models.bulk_account_contact_update_and_remove_metadata.Bulk account contact update and remove metadata(
                    requester_user_id = 6, 
                    comment = 'note from account admin', ),
                request_payloads = [
                    main_openapi_client.models.bulk_account_contact_update.Bulk account contact update(
                        arena_id = 6, 
                        account_id = 7, 
                        account_contact_id = 7, 
                        label = 'label', 
                        is_main_contact = True, 
                        is_admin_contact = True, 
                        distribution_list = [1,2,3], )
                    ]
            )
        else:
            return BulkAccountContactUpdateRequestBody(
        )
        """

    def testBulkAccountContactUpdateRequestBody(self):
        """Test BulkAccountContactUpdateRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()