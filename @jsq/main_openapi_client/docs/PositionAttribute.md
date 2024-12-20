# PositionAttribute

A position with account, investor group, and investment entity ids.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**account_id** | **int** |  | 
**investment_entity_id** | **int** |  | 
**investor_group_id** | **int** |  | 

## Example

```python
from main_openapi_client.models.position_attribute import PositionAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of PositionAttribute from a JSON string
position_attribute_instance = PositionAttribute.from_json(json)
# print the JSON string representation of the object
print(PositionAttribute.to_json())

# convert the object into a dict
position_attribute_dict = position_attribute_instance.to_dict()
# create an instance of PositionAttribute from a dict
position_attribute_from_dict = PositionAttribute.from_dict(position_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


