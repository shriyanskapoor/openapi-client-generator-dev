# BulkAccountContactChangeNotify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** |  | [optional] 
**request_payloads** | [**List[BulkAccountContactChangeNotifyRequestPayloadsInner]**](BulkAccountContactChangeNotifyRequestPayloadsInner.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.bulk_account_contact_change_notify import BulkAccountContactChangeNotify

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAccountContactChangeNotify from a JSON string
bulk_account_contact_change_notify_instance = BulkAccountContactChangeNotify.from_json(json)
# print the JSON string representation of the object
print(BulkAccountContactChangeNotify.to_json())

# convert the object into a dict
bulk_account_contact_change_notify_dict = bulk_account_contact_change_notify_instance.to_dict()
# create an instance of BulkAccountContactChangeNotify from a dict
bulk_account_contact_change_notify_from_dict = BulkAccountContactChangeNotify.from_dict(bulk_account_contact_change_notify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


