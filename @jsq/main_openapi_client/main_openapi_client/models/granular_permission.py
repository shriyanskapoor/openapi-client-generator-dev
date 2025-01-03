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


class GranularPermission(str, Enum):
    """
    Granular permission enum
    """

    """
    allowed enum values
    """
    CAN_MANAGE_PORTAL_SETTINGS = 'CAN_MANAGE_PORTAL_SETTINGS'
    CAN_MANAGE_GENERAL_SUBSCRIPTION_SETTINGS = 'CAN_MANAGE_GENERAL_SUBSCRIPTION_SETTINGS'
    CAN_MANAGE_STAFF_ACCESS = 'CAN_MANAGE_STAFF_ACCESS'
    CAN_MANAGE_SELF = 'CAN_MANAGE_SELF'
    CAN_MANAGE_USER_ROLES = 'CAN_MANAGE_USER_ROLES'
    CAN_ASSIGN_ADMINISTRATOR_PERMISSIONS_TO_STAFF_USERS = 'CAN_ASSIGN_ADMINISTRATOR_PERMISSIONS_TO_STAFF_USERS'
    CAN_MANAGE_AUTHENTICATION = 'CAN_MANAGE_AUTHENTICATION'
    CAN_MANAGE_AGREEMENTS = 'CAN_MANAGE_AGREEMENTS'
    CAN_MANAGE_DATA_FIELDS = 'CAN_MANAGE_DATA_FIELDS'
    CAN_ACCESS_AUDIT_LOG = 'CAN_ACCESS_AUDIT_LOG'
    CAN_CONFIG_DOCUMENT_CATEGORIES = 'CAN_CONFIG_DOCUMENT_CATEGORIES'
    CAN_CONFIG_EMAIL_DISTRIBUTION_LISTS = 'CAN_CONFIG_EMAIL_DISTRIBUTION_LISTS'
    CAN_CONFIG_CRM_NOTIFICATION_LISTS = 'CAN_CONFIG_CRM_NOTIFICATION_LISTS'
    CAN_CONFIG_OWNERSHIP_UNITS_AND_PERCENTAGES = 'CAN_CONFIG_OWNERSHIP_UNITS_AND_PERCENTAGES'
    CAN_CONFIG_DISTRIBUTIONS_AND_CAPITAL_TRANSACTIONS = 'CAN_CONFIG_DISTRIBUTIONS_AND_CAPITAL_TRANSACTIONS'
    CAN_CONFIG_NET_INCOME_AND_NAV_COMPONENTS = 'CAN_CONFIG_NET_INCOME_AND_NAV_COMPONENTS'
    CAN_CONFIG_ENTITY_SUBTYPES = 'CAN_CONFIG_ENTITY_SUBTYPES'
    CAN_CONFIG_METRICS_SETTINGS = 'CAN_CONFIG_METRICS_SETTINGS'
    CAN_CONFIG_WATERMARK_TEMPLATES = 'CAN_CONFIG_WATERMARK_TEMPLATES'
    CAN_CONFIG_MANAGEMENT_FEES = 'CAN_CONFIG_MANAGEMENT_FEES'
    CAN_CONFIG_ORGANIZATION_SETTINGS = 'CAN_CONFIG_ORGANIZATION_SETTINGS'
    CAN_CONFIG_E_SIGNATURES = 'CAN_CONFIG_E_SIGNATURES'
    CAN_CONFIG_STATEMENT_NOTICES = 'CAN_CONFIG_STATEMENT_NOTICES'
    CAN_CONFIG_STATIONERY_LIBRARY = 'CAN_CONFIG_STATIONERY_LIBRARY'
    CAN_CONFIG_REPORTING_TEMPLATE = 'CAN_CONFIG_REPORTING_TEMPLATE'
    CAN_CONFIG_INTEGRATIONS = 'CAN_CONFIG_INTEGRATIONS'
    CAN_CONFIG_MAPPINGS = 'CAN_CONFIG_MAPPINGS'
    CAN_ACCESS_PROSPECT_SUBSCRIPTION = 'CAN_ACCESS_PROSPECT_SUBSCRIPTION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GranularPermission from a JSON string"""
        return cls(json.loads(json_str))


