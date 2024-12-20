# BusinessInfo

Business information for diligence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_profile_id** | **int** | Profile ID for diligence | [optional] 
**legal_entity_name** | **str** | Legal entity name | [optional] 
**date_of_organization** | **str** | Date of formation for business | [optional] 
**tax_id** | **str** | Tax ID for business | [optional] 
**documents** | [**List[BusinessInfoDocumentsInner]**](BusinessInfoDocumentsInner.md) | Documents for business | [optional] 
**address** | [**BusinessInfoAddress**](BusinessInfoAddress.md) |  | [optional] 
**individual_profiles** | [**List[BusinessInfoIndividualProfilesInner]**](BusinessInfoIndividualProfilesInner.md) | Individual profiles used for legacy diligences. This is deprecated. For KYC, a KycDetail will be created. For watchlist, a watchlist screening will be triggered. | [optional] 
**institution_profiles** | [**List[BusinessInfoInstitutionProfilesInner]**](BusinessInfoInstitutionProfilesInner.md) | Institution profiles used for legacy diligences. This is deprecated. For KYC, a KycDetail will be created. For watchlist, a watchlist screening will be triggered. | [optional] 

## Example

```python
from main_openapi_client.models.business_info import BusinessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessInfo from a JSON string
business_info_instance = BusinessInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessInfo.to_json())

# convert the object into a dict
business_info_dict = business_info_instance.to_dict()
# create an instance of BusinessInfo from a dict
business_info_from_dict = BusinessInfo.from_dict(business_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


