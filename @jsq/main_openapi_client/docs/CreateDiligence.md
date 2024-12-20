# CreateDiligence

Deprecated create diligence object and underlying KYC/watchlists

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** | Arena ID the diligence is located in | [optional] 
**user_id** | **int** | User ID of the user creating the diligence | [optional] 
**external_object_type** | [**CreateDiligenceExternalObjectType**](CreateDiligenceExternalObjectType.md) |  | [optional] 
**external_object_id** | **int** | Number representing the id of the external object type in the external object type table. | [optional] 
**diligence_type** | [**CreateDiligenceDiligenceType**](CreateDiligenceDiligenceType.md) |  | [optional] 
**diligence_category** | [**CreateDiligenceDiligenceCategory**](CreateDiligenceDiligenceCategory.md) |  | [optional] 
**business_info** | [**CreateDiligenceBusinessInfo**](CreateDiligenceBusinessInfo.md) |  | [optional] 
**reference_external_object_type** | [**CreateDiligenceReferenceExternalObjectType**](CreateDiligenceReferenceExternalObjectType.md) |  | [optional] 
**reference_external_object_id** | **int** | Reference external object ID. Useful when needing to check the relationship between two objects. | [optional] 
**other_info** | **Dict[str, object]** | Other key values info for the diligence | [optional] 

## Example

```python
from main_openapi_client.models.create_diligence import CreateDiligence

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDiligence from a JSON string
create_diligence_instance = CreateDiligence.from_json(json)
# print the JSON string representation of the object
print(CreateDiligence.to_json())

# convert the object into a dict
create_diligence_dict = create_diligence_instance.to_dict()
# create an instance of CreateDiligence from a dict
create_diligence_from_dict = CreateDiligence.from_dict(create_diligence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


