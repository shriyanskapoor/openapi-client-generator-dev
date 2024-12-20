# BulkAccountContactRemoveRequestBody

Bulk account contact removal array input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **MetaData[str, object]** |  | [optional] 
**request_payloads** | [**List[BulkAccountContactRemove]**](BulkAccountContactRemove.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.bulk_account_contact_remove_request_body import BulkAccountContactRemoveRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAccountContactRemoveRequestBody from a JSON string
bulk_account_contact_remove_request_body_instance = BulkAccountContactRemoveRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkAccountContactRemoveRequestBody.to_json())

# convert the object into a dict
bulk_account_contact_remove_request_body_dict = bulk_account_contact_remove_request_body_instance.to_dict()
# create an instance of BulkAccountContactRemoveRequestBody from a dict
bulk_account_contact_remove_request_body_from_dict = BulkAccountContactRemoveRequestBody.from_dict(bulk_account_contact_remove_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


