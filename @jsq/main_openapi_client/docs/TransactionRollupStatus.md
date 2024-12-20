# TransactionRollupStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_id** | **str** | The batch ID associated with the transaction rollup | [optional] 
**updated_at** | **datetime** | The date and time the status was last updated | [optional] 
**status** | **str** | The current status of the transaction rollup | [optional] 

## Example

```python
from main_openapi_client.models.transaction_rollup_status import TransactionRollupStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRollupStatus from a JSON string
transaction_rollup_status_instance = TransactionRollupStatus.from_json(json)
# print the JSON string representation of the object
print(TransactionRollupStatus.to_json())

# convert the object into a dict
transaction_rollup_status_dict = transaction_rollup_status_instance.to_dict()
# create an instance of TransactionRollupStatus from a dict
transaction_rollup_status_from_dict = TransactionRollupStatus.from_dict(transaction_rollup_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


