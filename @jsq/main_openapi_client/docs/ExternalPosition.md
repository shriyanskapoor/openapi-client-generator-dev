# ExternalPosition

A position for a specific arena, source name, and source object id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 

## Example

```python
from main_openapi_client.models.external_position import ExternalPosition

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalPosition from a JSON string
external_position_instance = ExternalPosition.from_json(json)
# print the JSON string representation of the object
print(ExternalPosition.to_json())

# convert the object into a dict
external_position_dict = external_position_instance.to_dict()
# create an instance of ExternalPosition from a dict
external_position_from_dict = ExternalPosition.from_dict(external_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


