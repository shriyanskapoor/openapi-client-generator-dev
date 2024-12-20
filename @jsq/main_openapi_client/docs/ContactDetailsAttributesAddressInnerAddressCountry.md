# ContactDetailsAttributesAddressInnerAddressCountry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int** | ID of the country | [optional] 
**object_name** | **str** | Name of the country | [optional] 
**object_type** | **str** | Type of the country object | [optional] 

## Example

```python
from main_openapi_client.models.contact_details_attributes_address_inner_address_country import ContactDetailsAttributesAddressInnerAddressCountry

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailsAttributesAddressInnerAddressCountry from a JSON string
contact_details_attributes_address_inner_address_country_instance = ContactDetailsAttributesAddressInnerAddressCountry.from_json(json)
# print the JSON string representation of the object
print(ContactDetailsAttributesAddressInnerAddressCountry.to_json())

# convert the object into a dict
contact_details_attributes_address_inner_address_country_dict = contact_details_attributes_address_inner_address_country_instance.to_dict()
# create an instance of ContactDetailsAttributesAddressInnerAddressCountry from a dict
contact_details_attributes_address_inner_address_country_from_dict = ContactDetailsAttributesAddressInnerAddressCountry.from_dict(contact_details_attributes_address_inner_address_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


