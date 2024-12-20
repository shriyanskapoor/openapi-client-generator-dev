# AccountContactAdd

Account contact add

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_details** | [**ContactDetails**](.md) |  | 
**communication_preferences** | [**AddContactCommunicationPrefs**](.md) |  | 

## Example

```python
from main_openapi_client.models.account_contact_add import AccountContactAdd

# TODO update the JSON string below
json = "{}"
# create an instance of AccountContactAdd from a JSON string
account_contact_add_instance = AccountContactAdd.from_json(json)
# print the JSON string representation of the object
print(AccountContactAdd.to_json())

# convert the object into a dict
account_contact_add_dict = account_contact_add_instance.to_dict()
# create an instance of AccountContactAdd from a dict
account_contact_add_from_dict = AccountContactAdd.from_dict(account_contact_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


