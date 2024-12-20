# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from main_openapi_client.models.bulk_account_contact_change_notify_request_payloads_inner import BulkAccountContactChangeNotifyRequestPayloadsInner
from typing import Optional, Set
from typing_extensions import Self

class BulkAccountContactChangeNotify(BaseModel):
    """
    BulkAccountContactChangeNotify
    """ # noqa: E501
    request_type: Optional[StrictStr] = None
    request_payloads: Optional[List[BulkAccountContactChangeNotifyRequestPayloadsInner]] = None
    __properties: ClassVar[List[str]] = ["request_type", "request_payloads"]

    @field_validator('request_type')
    def request_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ADD_CONTACT', 'UPDATE_CONTACT', 'REMOVE_CONTACT']):
            raise ValueError("must be one of enum values ('ADD_CONTACT', 'UPDATE_CONTACT', 'REMOVE_CONTACT')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BulkAccountContactChangeNotify from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in request_payloads (list)
        _items = []
        if self.request_payloads:
            for _item_request_payloads in self.request_payloads:
                if _item_request_payloads:
                    _items.append(_item_request_payloads.to_dict())
            _dict['request_payloads'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BulkAccountContactChangeNotify from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "request_type": obj.get("request_type"),
            "request_payloads": [BulkAccountContactChangeNotifyRequestPayloadsInner.from_dict(_item) for _item in obj["request_payloads"]] if obj.get("request_payloads") is not None else None
        })
        return _obj


