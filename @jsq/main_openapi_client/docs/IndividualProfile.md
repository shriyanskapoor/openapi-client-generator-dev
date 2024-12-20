# IndividualProfile

Individual profile for diligence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_profile_id** | **int** | Profile ID for diligence | 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**date_of_birth** | **str** | Date of birth | 
**tax_id** | **str** | SSN | 
**address** | [**IndividualProfileAddress**](IndividualProfileAddress.md) |  | 
**documents** | [**List[BusinessInfoDocumentsInner]**](BusinessInfoDocumentsInner.md) | Documents for individual | 
**is_beneficial_owner** | **bool** | Whether the individual is a beneficial owner | [optional] 
**is_controller** | **bool** | Whether the individual is a controller | [optional] 
**is_signatory** | **bool** | Whether the individual is a signatory | [optional] 
**business_ownership_percent** | **int** | Potential percentage of the business the individual owns | [optional] 

## Example

```python
from main_openapi_client.models.individual_profile import IndividualProfile

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualProfile from a JSON string
individual_profile_instance = IndividualProfile.from_json(json)
# print the JSON string representation of the object
print(IndividualProfile.to_json())

# convert the object into a dict
individual_profile_dict = individual_profile_instance.to_dict()
# create an instance of IndividualProfile from a dict
individual_profile_from_dict = IndividualProfile.from_dict(individual_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


