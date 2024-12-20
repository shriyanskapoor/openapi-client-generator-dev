# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.contact_details_attributes_employments_inner_employer import ContactDetailsAttributesEmploymentsInnerEmployer

class TestContactDetailsAttributesEmploymentsInnerEmployer(unittest.TestCase):
    """ContactDetailsAttributesEmploymentsInnerEmployer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactDetailsAttributesEmploymentsInnerEmployer:
        """Test ContactDetailsAttributesEmploymentsInnerEmployer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactDetailsAttributesEmploymentsInnerEmployer`
        """
        model = ContactDetailsAttributesEmploymentsInnerEmployer()
        if include_optional:
            return ContactDetailsAttributesEmploymentsInnerEmployer(
                lazy_create = False,
                object_id = 56,
                object_name = 'TestCompany',
                object_type = 3
            )
        else:
            return ContactDetailsAttributesEmploymentsInnerEmployer(
        )
        """

    def testContactDetailsAttributesEmploymentsInnerEmployer(self):
        """Test ContactDetailsAttributesEmploymentsInnerEmployer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
