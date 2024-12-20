# ContactDetailsAttributesPhoneFaxInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the phone number | [optional] 
**phone_type** | **int** | Type of the phone number | [optional] 
**phone_number** | **str** | Phone number | [optional] 

## Example

```python
from main_openapi_client.models.contact_details_attributes_phone_fax_inner import ContactDetailsAttributesPhoneFaxInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailsAttributesPhoneFaxInner from a JSON string
contact_details_attributes_phone_fax_inner_instance = ContactDetailsAttributesPhoneFaxInner.from_json(json)
# print the JSON string representation of the object
print(ContactDetailsAttributesPhoneFaxInner.to_json())

# convert the object into a dict
contact_details_attributes_phone_fax_inner_dict = contact_details_attributes_phone_fax_inner_instance.to_dict()
# create an instance of ContactDetailsAttributesPhoneFaxInner from a dict
contact_details_attributes_phone_fax_inner_from_dict = ContactDetailsAttributesPhoneFaxInner.from_dict(contact_details_attributes_phone_fax_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


