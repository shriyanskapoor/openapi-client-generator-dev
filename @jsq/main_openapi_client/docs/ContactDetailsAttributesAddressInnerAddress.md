# ContactDetailsAttributesAddressInnerAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City of the address | [optional] 
**country** | [**ContactDetailsAttributesAddressInnerAddressCountry**](ContactDetailsAttributesAddressInnerAddressCountry.md) |  | [optional] 
**postal_code** | **str** | Postal code of the address | [optional] 
**state** | [**ContactDetailsAttributesAddressInnerAddressState**](ContactDetailsAttributesAddressInnerAddressState.md) |  | [optional] 
**street** | **str** | Street address | [optional] 
**street2** | **str** | Additional street address | [optional] 
**street3** | **str** | Additional street address | [optional] 

## Example

```python
from main_openapi_client.models.contact_details_attributes_address_inner_address import ContactDetailsAttributesAddressInnerAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailsAttributesAddressInnerAddress from a JSON string
contact_details_attributes_address_inner_address_instance = ContactDetailsAttributesAddressInnerAddress.from_json(json)
# print the JSON string representation of the object
print(ContactDetailsAttributesAddressInnerAddress.to_json())

# convert the object into a dict
contact_details_attributes_address_inner_address_dict = contact_details_attributes_address_inner_address_instance.to_dict()
# create an instance of ContactDetailsAttributesAddressInnerAddress from a dict
contact_details_attributes_address_inner_address_from_dict = ContactDetailsAttributesAddressInnerAddress.from_dict(contact_details_attributes_address_inner_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


