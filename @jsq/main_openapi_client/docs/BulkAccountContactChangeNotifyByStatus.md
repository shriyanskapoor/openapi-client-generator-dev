# BulkAccountContactChangeNotifyByStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**request_payloads** | [**List[BulkAccountContactChangeNotifyByStatusRequestPayloadsInner]**](BulkAccountContactChangeNotifyByStatusRequestPayloadsInner.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.bulk_account_contact_change_notify_by_status import BulkAccountContactChangeNotifyByStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAccountContactChangeNotifyByStatus from a JSON string
bulk_account_contact_change_notify_by_status_instance = BulkAccountContactChangeNotifyByStatus.from_json(json)
# print the JSON string representation of the object
print(BulkAccountContactChangeNotifyByStatus.to_json())

# convert the object into a dict
bulk_account_contact_change_notify_by_status_dict = bulk_account_contact_change_notify_by_status_instance.to_dict()
# create an instance of BulkAccountContactChangeNotifyByStatus from a dict
bulk_account_contact_change_notify_by_status_from_dict = BulkAccountContactChangeNotifyByStatus.from_dict(bulk_account_contact_change_notify_by_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


