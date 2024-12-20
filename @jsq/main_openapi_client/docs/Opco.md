# Opco

An entity's operating company information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opco_id** | **int** | The Account ID of the operating company | 
**opco_name** | **str** | The name of the operating company | 
**opco_currency** | **str** | The currency of the operating company | 
**positions** | [**List[OpcoPosition]**](OpcoPosition.md) | The positions associated with the operating company | 

## Example

```python
from main_openapi_client.models.opco import Opco

# TODO update the JSON string below
json = "{}"
# create an instance of Opco from a JSON string
opco_instance = Opco.from_json(json)
# print the JSON string representation of the object
print(Opco.to_json())

# convert the object into a dict
opco_dict = opco_instance.to_dict()
# create an instance of Opco from a dict
opco_from_dict = Opco.from_dict(opco_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


