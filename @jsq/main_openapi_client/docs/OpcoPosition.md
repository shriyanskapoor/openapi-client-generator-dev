# OpcoPosition

An entity's position on its operating company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**investor_group_name** | **str** |  | 
**status** | **str** |  | 
**ownership_percent** | **str** |  | 

## Example

```python
from main_openapi_client.models.opco_position import OpcoPosition

# TODO update the JSON string below
json = "{}"
# create an instance of OpcoPosition from a JSON string
opco_position_instance = OpcoPosition.from_json(json)
# print the JSON string representation of the object
print(OpcoPosition.to_json())

# convert the object into a dict
opco_position_dict = opco_position_instance.to_dict()
# create an instance of OpcoPosition from a dict
opco_position_from_dict = OpcoPosition.from_dict(opco_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


