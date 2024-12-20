# BulkAccountContactChangeNotifyRequestPayloadsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** |  | 
**account_id** | **int** |  | 
**contact_id** | **int** |  | 
**comment** | **str** |  | 

## Example

```python
from main_openapi_client.models.bulk_account_contact_change_notify_request_payloads_inner import BulkAccountContactChangeNotifyRequestPayloadsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAccountContactChangeNotifyRequestPayloadsInner from a JSON string
bulk_account_contact_change_notify_request_payloads_inner_instance = BulkAccountContactChangeNotifyRequestPayloadsInner.from_json(json)
# print the JSON string representation of the object
print(BulkAccountContactChangeNotifyRequestPayloadsInner.to_json())

# convert the object into a dict
bulk_account_contact_change_notify_request_payloads_inner_dict = bulk_account_contact_change_notify_request_payloads_inner_instance.to_dict()
# create an instance of BulkAccountContactChangeNotifyRequestPayloadsInner from a dict
bulk_account_contact_change_notify_request_payloads_inner_from_dict = BulkAccountContactChangeNotifyRequestPayloadsInner.from_dict(bulk_account_contact_change_notify_request_payloads_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


