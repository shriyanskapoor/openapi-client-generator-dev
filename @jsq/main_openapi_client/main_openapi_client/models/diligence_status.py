# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DiligenceStatus(str, Enum):
    """
    Status of the diligence in the submission workflow
    """

    """
    allowed enum values
    """
    STARTED = 'started'
    PENDING_REVIEW = 'pending_review'
    REQUESTED_LP_FOR_INFO = 'requested_lp_for_info'
    IN_REVIEW = 'in_review'
    PENDING_PEER_REVIEW = 'pending_peer_review'
    IN_PEER_REVIEW = 'in_peer_review'
    CONFIRMED = 'confirmed'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DiligenceStatus from a JSON string"""
        return cls(json.loads(json_str))


