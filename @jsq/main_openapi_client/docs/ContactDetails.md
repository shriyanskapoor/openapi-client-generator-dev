# ContactDetails

Details of the contact to be added or updated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **int** | ID of the contact | [optional] 
**arena_id** | **int** | ID of the arena | [optional] 
**is_update** | **bool** | Indicates if the contact is being updated | [optional] 
**attributes** | [**ContactDetailsAttributes**](ContactDetailsAttributes.md) |  | [optional] 
**access_group_ids** | **List[int]** | List of access group IDs | [optional] 
**invite_to_portal** | **bool** | Indicates if the contact should be invited to the portal | [optional] [default to False]

## Example

```python
from main_openapi_client.models.contact_details import ContactDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetails from a JSON string
contact_details_instance = ContactDetails.from_json(json)
# print the JSON string representation of the object
print(ContactDetails.to_json())

# convert the object into a dict
contact_details_dict = contact_details_instance.to_dict()
# create an instance of ContactDetails from a dict
contact_details_from_dict = ContactDetails.from_dict(contact_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


