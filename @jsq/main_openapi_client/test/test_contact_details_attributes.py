# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.contact_details_attributes import ContactDetailsAttributes

class TestContactDetailsAttributes(unittest.TestCase):
    """ContactDetailsAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactDetailsAttributes:
        """Test ContactDetailsAttributes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactDetailsAttributes`
        """
        model = ContactDetailsAttributes()
        if include_optional:
            return ContactDetailsAttributes(
                first_name = 'Test6',
                full_name = 'Test6 Person2 5',
                last_name = '6',
                middle_name = 'Person6',
                salutation_name = 'Mr.',
                email = main_openapi_client.models.contact_details_attributes_email.ContactDetails_attributes_email(
                    id = 56, 
                    email_type = 1, 
                    email_address = 'test@test.com', ),
                employments = [
                    main_openapi_client.models.contact_details_attributes_employments_inner.ContactDetails_attributes_employments_inner(
                        employer = main_openapi_client.models.contact_details_attributes_employments_inner_employer.ContactDetails_attributes_employments_inner_employer(
                            lazy_create = False, 
                            object_id = 56, 
                            object_name = 'TestCompany', 
                            object_type = 3, ), 
                        is_current = True, 
                        job_title = 'Director', 
                        sort_order = 1, )
                    ],
                phone_fax = [
                    main_openapi_client.models.contact_details_attributes_phone_fax_inner.ContactDetails_attributes_phone_fax_inner(
                        id = 56, 
                        phone_type = 2, 
                        phone_number = '+1 (211) 111-1111', )
                    ],
                address = [
                    main_openapi_client.models.contact_details_attributes_address_inner.ContactDetails_attributes_address_inner(
                        address_type = 1, 
                        id = 56, )
                    ]
            )
        else:
            return ContactDetailsAttributes(
        )
        """

    def testContactDetailsAttributes(self):
        """Test ContactDetailsAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
