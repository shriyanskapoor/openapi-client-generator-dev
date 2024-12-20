# FeatureFlag

Feature flags used to control application or arena wide availability of features. Note: presently only supports boolean (enabled/disabled) feature flags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | The name of the feature flag. | [readonly] 
**label** | **str** | A meaningful label for the feature flag. | [readonly] 
**description** | **str** | A description of the purpose of the feature flag. | [optional] [readonly] 
**is_enabled** | **bool** | Whether the feature flag is enabled or disabled. | 
**has_side_effects** | **bool** | Whether the feature flag has side-effect operations that must be performed when the feature flag is enabled or disabled. | [optional] [readonly] 

## Example

```python
from main_openapi_client.models.feature_flag import FeatureFlag

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlag from a JSON string
feature_flag_instance = FeatureFlag.from_json(json)
# print the JSON string representation of the object
print(FeatureFlag.to_json())

# convert the object into a dict
feature_flag_dict = feature_flag_instance.to_dict()
# create an instance of FeatureFlag from a dict
feature_flag_from_dict = FeatureFlag.from_dict(feature_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


