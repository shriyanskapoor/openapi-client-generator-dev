# BulkAccountContactRemove

Bulk account contact removal object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** | Arena ID | 
**account_id** | **int** | Account ID | 
**contact_id** | **int** | Contact ID | 
**account_contact_id** | **int** | Account contact ID | 
**suspend_contact_portal_access** | **bool** | Suspend contact portal access | [optional] [default to False]
**delete_contact** | **bool** | Delete contact | [optional] [default to False]

## Example

```python
from main_openapi_client.models.bulk_account_contact_remove import BulkAccountContactRemove

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAccountContactRemove from a JSON string
bulk_account_contact_remove_instance = BulkAccountContactRemove.from_json(json)
# print the JSON string representation of the object
print(BulkAccountContactRemove.to_json())

# convert the object into a dict
bulk_account_contact_remove_dict = bulk_account_contact_remove_instance.to_dict()
# create an instance of BulkAccountContactRemove from a dict
bulk_account_contact_remove_from_dict = BulkAccountContactRemove.from_dict(bulk_account_contact_remove_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


