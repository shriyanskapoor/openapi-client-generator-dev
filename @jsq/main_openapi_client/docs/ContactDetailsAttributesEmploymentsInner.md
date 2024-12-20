# ContactDetailsAttributesEmploymentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employer** | [**ContactDetailsAttributesEmploymentsInnerEmployer**](ContactDetailsAttributesEmploymentsInnerEmployer.md) |  | [optional] 
**is_current** | **bool** | Indicates if the employment is current | [optional] 
**job_title** | **str** | Job title of the contact | [optional] 
**sort_order** | **int** | Sort order of the employment | [optional] 

## Example

```python
from main_openapi_client.models.contact_details_attributes_employments_inner import ContactDetailsAttributesEmploymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailsAttributesEmploymentsInner from a JSON string
contact_details_attributes_employments_inner_instance = ContactDetailsAttributesEmploymentsInner.from_json(json)
# print the JSON string representation of the object
print(ContactDetailsAttributesEmploymentsInner.to_json())

# convert the object into a dict
contact_details_attributes_employments_inner_dict = contact_details_attributes_employments_inner_instance.to_dict()
# create an instance of ContactDetailsAttributesEmploymentsInner from a dict
contact_details_attributes_employments_inner_from_dict = ContactDetailsAttributesEmploymentsInner.from_dict(contact_details_attributes_employments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


