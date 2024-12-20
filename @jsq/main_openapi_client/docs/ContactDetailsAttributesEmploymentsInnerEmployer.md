# ContactDetailsAttributesEmploymentsInnerEmployer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lazy_create** | **bool** | Indicates if the employer should be lazily created | [optional] 
**object_id** | **int** | ID of the employer | [optional] 
**object_name** | **str** | Name of the employer | [optional] 
**object_type** | **int** | Type of the employer object | [optional] 

## Example

```python
from main_openapi_client.models.contact_details_attributes_employments_inner_employer import ContactDetailsAttributesEmploymentsInnerEmployer

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailsAttributesEmploymentsInnerEmployer from a JSON string
contact_details_attributes_employments_inner_employer_instance = ContactDetailsAttributesEmploymentsInnerEmployer.from_json(json)
# print the JSON string representation of the object
print(ContactDetailsAttributesEmploymentsInnerEmployer.to_json())

# convert the object into a dict
contact_details_attributes_employments_inner_employer_dict = contact_details_attributes_employments_inner_employer_instance.to_dict()
# create an instance of ContactDetailsAttributesEmploymentsInnerEmployer from a dict
contact_details_attributes_employments_inner_employer_from_dict = ContactDetailsAttributesEmploymentsInnerEmployer.from_dict(contact_details_attributes_employments_inner_employer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


