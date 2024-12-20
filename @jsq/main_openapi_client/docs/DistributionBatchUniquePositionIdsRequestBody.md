# DistributionBatchUniquePositionIdsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_deleted** | **bool** | Include deleted positions in the count. | [optional] 
**ids** | **List[int]** | An array of distribution batch IDs. Each ID must be a positive integer. | [optional] 

## Example

```python
from main_openapi_client.models.distribution_batch_unique_position_ids_request_body import DistributionBatchUniquePositionIdsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of DistributionBatchUniquePositionIdsRequestBody from a JSON string
distribution_batch_unique_position_ids_request_body_instance = DistributionBatchUniquePositionIdsRequestBody.from_json(json)
# print the JSON string representation of the object
print(DistributionBatchUniquePositionIdsRequestBody.to_json())

# convert the object into a dict
distribution_batch_unique_position_ids_request_body_dict = distribution_batch_unique_position_ids_request_body_instance.to_dict()
# create an instance of DistributionBatchUniquePositionIdsRequestBody from a dict
distribution_batch_unique_position_ids_request_body_from_dict = DistributionBatchUniquePositionIdsRequestBody.from_dict(distribution_batch_unique_position_ids_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


