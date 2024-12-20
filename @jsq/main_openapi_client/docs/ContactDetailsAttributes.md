# ContactDetailsAttributes

Attributes of the contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the contact | [optional] 
**full_name** | **str** | Full name of the contact | [optional] 
**last_name** | **str** | Last name of the contact | [optional] 
**middle_name** | **str** | Middle name of the contact | [optional] 
**salutation_name** | **str** | Salutation name of the contact | [optional] 
**email** | [**ContactDetailsAttributesEmail**](ContactDetailsAttributesEmail.md) |  | [optional] 
**employments** | [**List[ContactDetailsAttributesEmploymentsInner]**](ContactDetailsAttributesEmploymentsInner.md) | List of employments | [optional] 
**phone_fax** | [**List[ContactDetailsAttributesPhoneFaxInner]**](ContactDetailsAttributesPhoneFaxInner.md) | List of phone numbers | [optional] 
**address** | [**List[ContactDetailsAttributesAddressInner]**](ContactDetailsAttributesAddressInner.md) | List of addresses | [optional] 

## Example

```python
from main_openapi_client.models.contact_details_attributes import ContactDetailsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailsAttributes from a JSON string
contact_details_attributes_instance = ContactDetailsAttributes.from_json(json)
# print the JSON string representation of the object
print(ContactDetailsAttributes.to_json())

# convert the object into a dict
contact_details_attributes_dict = contact_details_attributes_instance.to_dict()
# create an instance of ContactDetailsAttributes from a dict
contact_details_attributes_from_dict = ContactDetailsAttributes.from_dict(contact_details_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


