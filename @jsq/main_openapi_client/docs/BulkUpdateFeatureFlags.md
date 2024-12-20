# BulkUpdateFeatureFlags

Bulk operation to update feature flag states in bulk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from main_openapi_client.models.bulk_update_feature_flags import BulkUpdateFeatureFlags

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateFeatureFlags from a JSON string
bulk_update_feature_flags_instance = BulkUpdateFeatureFlags.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateFeatureFlags.to_json())

# convert the object into a dict
bulk_update_feature_flags_dict = bulk_update_feature_flags_instance.to_dict()
# create an instance of BulkUpdateFeatureFlags from a dict
bulk_update_feature_flags_from_dict = BulkUpdateFeatureFlags.from_dict(bulk_update_feature_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


