# PositionContributionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**amount** | **float** |  | 

## Example

```python
from main_openapi_client.models.position_contributions_inner import PositionContributionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PositionContributionsInner from a JSON string
position_contributions_inner_instance = PositionContributionsInner.from_json(json)
# print the JSON string representation of the object
print(PositionContributionsInner.to_json())

# convert the object into a dict
position_contributions_inner_dict = position_contributions_inner_instance.to_dict()
# create an instance of PositionContributionsInner from a dict
position_contributions_inner_from_dict = PositionContributionsInner.from_dict(position_contributions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


