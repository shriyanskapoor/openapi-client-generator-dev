# ArenaRoles

Roles for an arena.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** | FK to the arena. | [readonly] 
**role_ids** | **List[int]** | FK to the role. | [readonly] 
**role_enums** | **List[str]** | Enum key for the role. Orders sorted by role name alphabetical order. | [readonly] 

## Example

```python
from main_openapi_client.models.arena_roles import ArenaRoles

# TODO update the JSON string below
json = "{}"
# create an instance of ArenaRoles from a JSON string
arena_roles_instance = ArenaRoles.from_json(json)
# print the JSON string representation of the object
print(ArenaRoles.to_json())

# convert the object into a dict
arena_roles_dict = arena_roles_instance.to_dict()
# create an instance of ArenaRoles from a dict
arena_roles_from_dict = ArenaRoles.from_dict(arena_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


