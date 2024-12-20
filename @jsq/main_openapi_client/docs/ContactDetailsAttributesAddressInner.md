# ContactDetailsAttributesAddressInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**ContactDetailsAttributesAddressInnerAddress**](ContactDetailsAttributesAddressInnerAddress.md) |  | [optional] 
**address_type** | **int** | Type of the address | [optional] 
**id** | **int** | ID of the address | [optional] 

## Example

```python
from main_openapi_client.models.contact_details_attributes_address_inner import ContactDetailsAttributesAddressInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailsAttributesAddressInner from a JSON string
contact_details_attributes_address_inner_instance = ContactDetailsAttributesAddressInner.from_json(json)
# print the JSON string representation of the object
print(ContactDetailsAttributesAddressInner.to_json())

# convert the object into a dict
contact_details_attributes_address_inner_dict = contact_details_attributes_address_inner_instance.to_dict()
# create an instance of ContactDetailsAttributesAddressInner from a dict
contact_details_attributes_address_inner_from_dict = ContactDetailsAttributesAddressInner.from_dict(contact_details_attributes_address_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


