# Document

Documents for business

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** | Document type | [optional] 
**s3_key** | **str** | S3 Keys for documents | [optional] 
**name** | **str** | Name of document | [optional] 
**content_type** | **str** | Content type of document | [optional] 

## Example

```python
from main_openapi_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


