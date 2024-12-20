# DistributionBatch

A Distribution Batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**total_amount** | **float** | Total amount distributed | 
**arena_id** | **int** | Arena ID this distribution batch belongs to. | [readonly] 
**entity_id** | **int** | Entity ID this distribution batch belongs to. | [readonly] 
**description** | **str** | Description of the distribution batch. | [readonly] 

## Example

```python
from main_openapi_client.models.distribution_batch import DistributionBatch

# TODO update the JSON string below
json = "{}"
# create an instance of DistributionBatch from a JSON string
distribution_batch_instance = DistributionBatch.from_json(json)
# print the JSON string representation of the object
print(DistributionBatch.to_json())

# convert the object into a dict
distribution_batch_dict = distribution_batch_instance.to_dict()
# create an instance of DistributionBatch from a dict
distribution_batch_from_dict = DistributionBatch.from_dict(distribution_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


