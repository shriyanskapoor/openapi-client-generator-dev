# InstitutionProfile

Institution profile for diligence

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
from main_openapi_client.models.institution_profile import InstitutionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionProfile from a JSON string
institution_profile_instance = InstitutionProfile.from_json(json)
# print the JSON string representation of the object
print(InstitutionProfile.to_json())

# convert the object into a dict
institution_profile_dict = institution_profile_instance.to_dict()
# create an instance of InstitutionProfile from a dict
institution_profile_from_dict = InstitutionProfile.from_dict(institution_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


