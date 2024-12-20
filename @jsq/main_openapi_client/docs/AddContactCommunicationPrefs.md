# AddContactCommunicationPrefs

Account contact add communication pref

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** | Arena ID | 
**account_id** | **int** | Account ID | 
**label** | **str** | Relationship label for account contact | [optional] 
**is_main_contact** | **bool** | True if the account contact is To contact, False for CC contact | [optional] 
**is_admin_contact** | **bool** | True if the account contact is an admin contact | [optional] 
**distribution_list** | **List[int]** | List of distribution IDs | [optional] 

## Example

```python
from main_openapi_client.models.add_contact_communication_prefs import AddContactCommunicationPrefs

# TODO update the JSON string below
json = "{}"
# create an instance of AddContactCommunicationPrefs from a JSON string
add_contact_communication_prefs_instance = AddContactCommunicationPrefs.from_json(json)
# print the JSON string representation of the object
print(AddContactCommunicationPrefs.to_json())

# convert the object into a dict
add_contact_communication_prefs_dict = add_contact_communication_prefs_instance.to_dict()
# create an instance of AddContactCommunicationPrefs from a dict
add_contact_communication_prefs_from_dict = AddContactCommunicationPrefs.from_dict(add_contact_communication_prefs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


