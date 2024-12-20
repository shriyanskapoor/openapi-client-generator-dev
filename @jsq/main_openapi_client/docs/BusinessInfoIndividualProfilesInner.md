# BusinessInfoIndividualProfilesInner


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
from main_openapi_client.models.business_info_individual_profiles_inner import BusinessInfoIndividualProfilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessInfoIndividualProfilesInner from a JSON string
business_info_individual_profiles_inner_instance = BusinessInfoIndividualProfilesInner.from_json(json)
# print the JSON string representation of the object
print(BusinessInfoIndividualProfilesInner.to_json())

# convert the object into a dict
business_info_individual_profiles_inner_dict = business_info_individual_profiles_inner_instance.to_dict()
# create an instance of BusinessInfoIndividualProfilesInner from a dict
business_info_individual_profiles_inner_from_dict = BusinessInfoIndividualProfilesInner.from_dict(business_info_individual_profiles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


