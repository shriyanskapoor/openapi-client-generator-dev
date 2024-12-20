# Position

A position in an investment entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Name of the position. | 
**amount_committed** | **float** | Amount that this position has committed to invest. | 
**percent_ownership** | **float** | Percentage of ownership in the investment. | 
**investor_group_name** | **str** | Name of the position&#39;s investor group. | 
**cabs** | [**List[PositionCabsInner]**](PositionCabsInner.md) | Capital account balances of position | 
**contributions** | [**List[PositionContributionsInner]**](PositionContributionsInner.md) |  | [optional] 
**distributions** | [**List[PositionContributionsInner]**](PositionContributionsInner.md) |  | [optional] 
**net_income_sum_by_type** | [**List[PositionNetIncomeSumByTypeInner]**](PositionNetIncomeSumByTypeInner.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.position import Position

# TODO update the JSON string below
json = "{}"
# create an instance of Position from a JSON string
position_instance = Position.from_json(json)
# print the JSON string representation of the object
print(Position.to_json())

# convert the object into a dict
position_dict = position_instance.to_dict()
# create an instance of Position from a dict
position_from_dict = Position.from_dict(position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


