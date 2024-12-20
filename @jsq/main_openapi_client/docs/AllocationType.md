# AllocationType

Allocation Types for an arena

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the allocation type. | 
**category** | **str** | Category of the allocation type. | 
**is_recallable** | **bool** | Flag to indicate whether the allocation type is recallable. | 

## Example

```python
from main_openapi_client.models.allocation_type import AllocationType

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationType from a JSON string
allocation_type_instance = AllocationType.from_json(json)
# print the JSON string representation of the object
print(AllocationType.to_json())

# convert the object into a dict
allocation_type_dict = allocation_type_instance.to_dict()
# create an instance of AllocationType from a dict
allocation_type_from_dict = AllocationType.from_dict(allocation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


