# BulkAccountContactUpdate

Bulk account contact update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** | Arena ID | 
**account_id** | **int** | User ID | 
**account_contact_id** | **int** | Account contact ID | 
**label** | **str** | Relationship label for account contact | [optional] 
**is_main_contact** | **bool** | True if the account contact is To contact, False for CC contact | [optional] 
**is_admin_contact** | **bool** | True if the account contact is an admin contact | [optional] 
**distribution_list** | **List[int]** | List of distribution IDs | [optional] 

## Example

```python
from main_openapi_client.models.bulk_account_contact_update import BulkAccountContactUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAccountContactUpdate from a JSON string
bulk_account_contact_update_instance = BulkAccountContactUpdate.from_json(json)
# print the JSON string representation of the object
print(BulkAccountContactUpdate.to_json())

# convert the object into a dict
bulk_account_contact_update_dict = bulk_account_contact_update_instance.to_dict()
# create an instance of BulkAccountContactUpdate from a dict
bulk_account_contact_update_from_dict = BulkAccountContactUpdate.from_dict(bulk_account_contact_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


