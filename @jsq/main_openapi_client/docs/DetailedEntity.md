# DetailedEntity

An entity with it's positions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** | Name of the entity. | [optional] 
**arena_id** | **int** |  | [optional] [readonly] 
**bank_account_id** | **int** |  | [optional] 
**automated_payments_enabled** | **bool** |  | [optional] 
**positions** | [**List[Position]**](Position.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.detailed_entity import DetailedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedEntity from a JSON string
detailed_entity_instance = DetailedEntity.from_json(json)
# print the JSON string representation of the object
print(DetailedEntity.to_json())

# convert the object into a dict
detailed_entity_dict = detailed_entity_instance.to_dict()
# create an instance of DetailedEntity from a dict
detailed_entity_from_dict = DetailedEntity.from_dict(detailed_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


