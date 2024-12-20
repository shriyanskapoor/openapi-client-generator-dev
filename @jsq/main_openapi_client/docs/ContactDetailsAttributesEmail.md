# ContactDetailsAttributesEmail

Email of the contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the email | [optional] 
**email_type** | **int** | Type of the email | [optional] 
**email_address** | **str** | Email address | [optional] 

## Example

```python
from main_openapi_client.models.contact_details_attributes_email import ContactDetailsAttributesEmail

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailsAttributesEmail from a JSON string
contact_details_attributes_email_instance = ContactDetailsAttributesEmail.from_json(json)
# print the JSON string representation of the object
print(ContactDetailsAttributesEmail.to_json())

# convert the object into a dict
contact_details_attributes_email_dict = contact_details_attributes_email_instance.to_dict()
# create an instance of ContactDetailsAttributesEmail from a dict
contact_details_attributes_email_from_dict = ContactDetailsAttributesEmail.from_dict(contact_details_attributes_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


