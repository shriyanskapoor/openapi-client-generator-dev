# AccountContactBulkSuccessResponse

Account contact bulk success response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** | Arena ID | [optional] 
**account_id** | **int** | User ID | [optional] 
**account_contact_id** | **int** | Account contact ID | [optional] 
**status** | [**ResponseStatus**](ResponseStatus.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.account_contact_bulk_success_response import AccountContactBulkSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountContactBulkSuccessResponse from a JSON string
account_contact_bulk_success_response_instance = AccountContactBulkSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(AccountContactBulkSuccessResponse.to_json())

# convert the object into a dict
account_contact_bulk_success_response_dict = account_contact_bulk_success_response_instance.to_dict()
# create an instance of AccountContactBulkSuccessResponse from a dict
account_contact_bulk_success_response_from_dict = AccountContactBulkSuccessResponse.from_dict(account_contact_bulk_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


