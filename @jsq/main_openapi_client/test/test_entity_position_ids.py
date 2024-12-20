# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.entity_position_ids import EntityPositionIds

class TestEntityPositionIds(unittest.TestCase):
    """EntityPositionIds unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntityPositionIds:
        """Test EntityPositionIds
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntityPositionIds`
        """
        model = EntityPositionIds()
        if include_optional:
            return EntityPositionIds(
                entity_id = 56,
                position_ids = [
                    56
                    ]
            )
        else:
            return EntityPositionIds(
                entity_id = 56,
                position_ids = [
                    56
                    ],
        )
        """

    def testEntityPositionIds(self):
        """Test EntityPositionIds"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()