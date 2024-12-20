# EntityPositionIds

Positions IDs for a specific entity ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** | The unique identifier of the entity | 
**position_ids** | **List[int]** | Position IDs associated with the given entity ID | 

## Example

```python
from main_openapi_client.models.entity_position_ids import EntityPositionIds

# TODO update the JSON string below
json = "{}"
# create an instance of EntityPositionIds from a JSON string
entity_position_ids_instance = EntityPositionIds.from_json(json)
# print the JSON string representation of the object
print(EntityPositionIds.to_json())

# convert the object into a dict
entity_position_ids_dict = entity_position_ids_instance.to_dict()
# create an instance of EntityPositionIds from a dict
entity_position_ids_from_dict = EntityPositionIds.from_dict(entity_position_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


