# InstitutionProfileAddress

Address for institution

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
from main_openapi_client.models.institution_profile_address import InstitutionProfileAddress

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionProfileAddress from a JSON string
institution_profile_address_instance = InstitutionProfileAddress.from_json(json)
# print the JSON string representation of the object
print(InstitutionProfileAddress.to_json())

# convert the object into a dict
institution_profile_address_dict = institution_profile_address_instance.to_dict()
# create an instance of InstitutionProfileAddress from a dict
institution_profile_address_from_dict = InstitutionProfileAddress.from_dict(institution_profile_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


