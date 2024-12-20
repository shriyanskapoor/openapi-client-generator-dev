# BulkAccountContactUpdateRequestBody

Bulk account contact update array input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **MetaData[str, object]** |  | [optional] 
**request_payloads** | [**List[BulkAccountContactUpdate]**](BulkAccountContactUpdate.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.bulk_account_contact_update_request_body import BulkAccountContactUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAccountContactUpdateRequestBody from a JSON string
bulk_account_contact_update_request_body_instance = BulkAccountContactUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkAccountContactUpdateRequestBody.to_json())

# convert the object into a dict
bulk_account_contact_update_request_body_dict = bulk_account_contact_update_request_body_instance.to_dict()
# create an instance of BulkAccountContactUpdateRequestBody from a dict
bulk_account_contact_update_request_body_from_dict = BulkAccountContactUpdateRequestBody.from_dict(bulk_account_contact_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


