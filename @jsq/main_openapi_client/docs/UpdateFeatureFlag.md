# UpdateFeatureFlag

Feature flags used to control application or arena wide availability of features. Note: presently only supports boolean (enabled/disabled) feature flags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether the feature flag is enabled or disabled. | 

## Example

```python
from main_openapi_client.models.update_feature_flag import UpdateFeatureFlag

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeatureFlag from a JSON string
update_feature_flag_instance = UpdateFeatureFlag.from_json(json)
# print the JSON string representation of the object
print(UpdateFeatureFlag.to_json())

# convert the object into a dict
update_feature_flag_dict = update_feature_flag_instance.to_dict()
# create an instance of UpdateFeatureFlag from a dict
update_feature_flag_from_dict = UpdateFeatureFlag.from_dict(update_feature_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


