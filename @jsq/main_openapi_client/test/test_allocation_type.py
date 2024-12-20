# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.allocation_type import AllocationType

class TestAllocationType(unittest.TestCase):
    """AllocationType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AllocationType:
        """Test AllocationType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AllocationType`
        """
        model = AllocationType()
        if include_optional:
            return AllocationType(
                name = '',
                category = 'Capital Call',
                is_recallable = True
            )
        else:
            return AllocationType(
                name = '',
                category = 'Capital Call',
                is_recallable = True,
        )
        """

    def testAllocationType(self):
        """Test AllocationType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
