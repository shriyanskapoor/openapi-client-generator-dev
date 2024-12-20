# ArenaManageAccountContactSettings

Manage Account Contact for an arena.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** | FK to the the arena these account contact settings belong to. | [readonly] 
**allow_admin_manage_account_contacts** | **bool** | Whether or not the admin can manage account contacts. | 
**contact_update_require_mgr_approval** | **str** | Account contact requires manager approval. | 

## Example

```python
from main_openapi_client.models.arena_manage_account_contact_settings import ArenaManageAccountContactSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ArenaManageAccountContactSettings from a JSON string
arena_manage_account_contact_settings_instance = ArenaManageAccountContactSettings.from_json(json)
# print the JSON string representation of the object
print(ArenaManageAccountContactSettings.to_json())

# convert the object into a dict
arena_manage_account_contact_settings_dict = arena_manage_account_contact_settings_instance.to_dict()
# create an instance of ArenaManageAccountContactSettings from a dict
arena_manage_account_contact_settings_from_dict = ArenaManageAccountContactSettings.from_dict(arena_manage_account_contact_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


