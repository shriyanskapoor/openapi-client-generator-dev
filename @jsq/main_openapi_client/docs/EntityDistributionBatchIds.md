# EntityDistributionBatchIds

The distribution batch IDs associated with an entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** |  | 
**distribution_batch_ids** | **List[int]** |  | 

## Example

```python
from main_openapi_client.models.entity_distribution_batch_ids import EntityDistributionBatchIds

# TODO update the JSON string below
json = "{}"
# create an instance of EntityDistributionBatchIds from a JSON string
entity_distribution_batch_ids_instance = EntityDistributionBatchIds.from_json(json)
# print the JSON string representation of the object
print(EntityDistributionBatchIds.to_json())

# convert the object into a dict
entity_distribution_batch_ids_dict = entity_distribution_batch_ids_instance.to_dict()
# create an instance of EntityDistributionBatchIds from a dict
entity_distribution_batch_ids_from_dict = EntityDistributionBatchIds.from_dict(entity_distribution_batch_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


