# BusinessInfoInstitutionProfilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_profile_id** | **int** | Profile ID for institution | 
**legal_entity_name** | **str** | Name of institution | 
**tax_id** | **str** | Tax ID for institution | 
**date_of_organization** | **str** | Date of formation for business | 
**is_beneficial_owner** | **bool** | Whether the individual is a beneficial owner | [optional] 
**address** | [**InstitutionProfileAddress**](InstitutionProfileAddress.md) |  | 
**documents** | [**List[BusinessInfoDocumentsInner]**](BusinessInfoDocumentsInner.md) | Documents for individual | 
**business_ownership_percent** | **int** | Potential percentage of the business the individual owns | [optional] 

## Example

```python
from main_openapi_client.models.business_info_institution_profiles_inner import BusinessInfoInstitutionProfilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessInfoInstitutionProfilesInner from a JSON string
business_info_institution_profiles_inner_instance = BusinessInfoInstitutionProfilesInner.from_json(json)
# print the JSON string representation of the object
print(BusinessInfoInstitutionProfilesInner.to_json())

# convert the object into a dict
business_info_institution_profiles_inner_dict = business_info_institution_profiles_inner_instance.to_dict()
# create an instance of BusinessInfoInstitutionProfilesInner from a dict
business_info_institution_profiles_inner_from_dict = BusinessInfoInstitutionProfilesInner.from_dict(business_info_institution_profiles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


