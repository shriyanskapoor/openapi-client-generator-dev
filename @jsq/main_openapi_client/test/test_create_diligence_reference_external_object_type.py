# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.create_diligence_reference_external_object_type import CreateDiligenceReferenceExternalObjectType

class TestCreateDiligenceReferenceExternalObjectType(unittest.TestCase):
    """CreateDiligenceReferenceExternalObjectType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateDiligenceReferenceExternalObjectType:
        """Test CreateDiligenceReferenceExternalObjectType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateDiligenceReferenceExternalObjectType`
        """
        model = CreateDiligenceReferenceExternalObjectType()
        if include_optional:
            return CreateDiligenceReferenceExternalObjectType(
            )
        else:
            return CreateDiligenceReferenceExternalObjectType(
        )
        """

    def testCreateDiligenceReferenceExternalObjectType(self):
        """Test CreateDiligenceReferenceExternalObjectType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
