# BulkAccountContactChangeNotifyByStatusRequestPayloadsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** |  | 
**account_id** | **int** |  | 
**contact_id** | **int** |  | [optional] 
**new_contact_name** | **str** |  | [optional] 
**comment** | **str** |  | 

## Example

```python
from main_openapi_client.models.bulk_account_contact_change_notify_by_status_request_payloads_inner import BulkAccountContactChangeNotifyByStatusRequestPayloadsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAccountContactChangeNotifyByStatusRequestPayloadsInner from a JSON string
bulk_account_contact_change_notify_by_status_request_payloads_inner_instance = BulkAccountContactChangeNotifyByStatusRequestPayloadsInner.from_json(json)
# print the JSON string representation of the object
print(BulkAccountContactChangeNotifyByStatusRequestPayloadsInner.to_json())

# convert the object into a dict
bulk_account_contact_change_notify_by_status_request_payloads_inner_dict = bulk_account_contact_change_notify_by_status_request_payloads_inner_instance.to_dict()
# create an instance of BulkAccountContactChangeNotifyByStatusRequestPayloadsInner from a dict
bulk_account_contact_change_notify_by_status_request_payloads_inner_from_dict = BulkAccountContactChangeNotifyByStatusRequestPayloadsInner.from_dict(bulk_account_contact_change_notify_by_status_request_payloads_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


