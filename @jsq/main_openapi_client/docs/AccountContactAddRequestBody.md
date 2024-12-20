# AccountContactAddRequestBody

account contact add input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **MetaData[str, object]** |  | [optional] 
**request_payload** | [**AccountContactAdd**](.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.account_contact_add_request_body import AccountContactAddRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AccountContactAddRequestBody from a JSON string
account_contact_add_request_body_instance = AccountContactAddRequestBody.from_json(json)
# print the JSON string representation of the object
print(AccountContactAddRequestBody.to_json())

# convert the object into a dict
account_contact_add_request_body_dict = account_contact_add_request_body_instance.to_dict()
# create an instance of AccountContactAddRequestBody from a dict
account_contact_add_request_body_from_dict = AccountContactAddRequestBody.from_dict(account_contact_add_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


