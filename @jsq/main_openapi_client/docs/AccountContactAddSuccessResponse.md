# AccountContactAddSuccessResponse

Account contact add success response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** | Arena ID | [optional] 
**account_id** | **int** | Account ID | [optional] 
**contact_id** | **int** | Contact ID | [optional] 
**account_contact_id** | **int** | Account contact ID | [optional] 
**status** | [**ResponseStatus**](ResponseStatus.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.account_contact_add_success_response import AccountContactAddSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountContactAddSuccessResponse from a JSON string
account_contact_add_success_response_instance = AccountContactAddSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(AccountContactAddSuccessResponse.to_json())

# convert the object into a dict
account_contact_add_success_response_dict = account_contact_add_success_response_instance.to_dict()
# create an instance of AccountContactAddSuccessResponse from a dict
account_contact_add_success_response_from_dict = AccountContactAddSuccessResponse.from_dict(account_contact_add_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


