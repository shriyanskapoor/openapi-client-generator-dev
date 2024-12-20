# Arena

Arena resources representing a GP workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | The name of the arena. | 
**unified_portal_url** | **str** | The environment specific arena&#39;s hostname and path prefix for the Unified Portal (Portal 2.0) | 
**is_active** | **bool** | Whether the arena is active. | 
**domain** | **str** | The domain of the arena. | 

## Example

```python
from main_openapi_client.models.arena import Arena

# TODO update the JSON string below
json = "{}"
# create an instance of Arena from a JSON string
arena_instance = Arena.from_json(json)
# print the JSON string representation of the object
print(Arena.to_json())

# convert the object into a dict
arena_dict = arena_instance.to_dict()
# create an instance of Arena from a dict
arena_from_dict = Arena.from_dict(arena_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


