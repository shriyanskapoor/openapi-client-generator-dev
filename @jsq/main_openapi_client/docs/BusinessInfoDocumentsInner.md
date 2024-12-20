# BusinessInfoDocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** | Document type | [optional] 
**s3_key** | **str** | S3 Keys for documents | [optional] 
**name** | **str** | Name of document | [optional] 
**content_type** | **str** | Content type of document | [optional] 

## Example

```python
from main_openapi_client.models.business_info_documents_inner import BusinessInfoDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessInfoDocumentsInner from a JSON string
business_info_documents_inner_instance = BusinessInfoDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(BusinessInfoDocumentsInner.to_json())

# convert the object into a dict
business_info_documents_inner_dict = business_info_documents_inner_instance.to_dict()
# create an instance of BusinessInfoDocumentsInner from a dict
business_info_documents_inner_from_dict = BusinessInfoDocumentsInner.from_dict(business_info_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


