# ArenaNetIncomeType

Allocation Type for an arena.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** | FK to the the arena these payment settings belong to. | [readonly] 
**id** | **int** | ID of the allocation type. | 
**sort_order** | **int** | The sort order of the object. | [optional] 
**name** | **str** | Name of the allocation type. | 

## Example

```python
from main_openapi_client.models.arena_net_income_type import ArenaNetIncomeType

# TODO update the JSON string below
json = "{}"
# create an instance of ArenaNetIncomeType from a JSON string
arena_net_income_type_instance = ArenaNetIncomeType.from_json(json)
# print the JSON string representation of the object
print(ArenaNetIncomeType.to_json())

# convert the object into a dict
arena_net_income_type_dict = arena_net_income_type_instance.to_dict()
# create an instance of ArenaNetIncomeType from a dict
arena_net_income_type_from_dict = ArenaNetIncomeType.from_dict(arena_net_income_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


