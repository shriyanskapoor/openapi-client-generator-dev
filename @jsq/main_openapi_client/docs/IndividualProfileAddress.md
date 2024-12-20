# IndividualProfileAddress

Address for individual

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | Street address | [optional] 
**line2** | **str** | Street address line 2 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**postal_code** | **str** | Postal code | [optional] 
**country** | **str** | Country (ISO 3166-1 alpha-2) | [optional] 

## Example

```python
from main_openapi_client.models.individual_profile_address import IndividualProfileAddress

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualProfileAddress from a JSON string
individual_profile_address_instance = IndividualProfileAddress.from_json(json)
# print the JSON string representation of the object
print(IndividualProfileAddress.to_json())

# convert the object into a dict
individual_profile_address_dict = individual_profile_address_instance.to_dict()
# create an instance of IndividualProfileAddress from a dict
individual_profile_address_from_dict = IndividualProfileAddress.from_dict(individual_profile_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


