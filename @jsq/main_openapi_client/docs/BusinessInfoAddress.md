# BusinessInfoAddress

Address for business

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
from main_openapi_client.models.business_info_address import BusinessInfoAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessInfoAddress from a JSON string
business_info_address_instance = BusinessInfoAddress.from_json(json)
# print the JSON string representation of the object
print(BusinessInfoAddress.to_json())

# convert the object into a dict
business_info_address_dict = business_info_address_instance.to_dict()
# create an instance of BusinessInfoAddress from a dict
business_info_address_from_dict = BusinessInfoAddress.from_dict(business_info_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


