# ArenaPaymentSettings

Payment Settings for an arena.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **int** | FK to the the arena these payment settings belong to. | [readonly] 
**required_approval_count** | **int** | The number of approvers required on a payment batch. | 
**require_different_approver** | **bool** | Whether or not the payment batch creator can also approve the payment batch. | 

## Example

```python
from main_openapi_client.models.arena_payment_settings import ArenaPaymentSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ArenaPaymentSettings from a JSON string
arena_payment_settings_instance = ArenaPaymentSettings.from_json(json)
# print the JSON string representation of the object
print(ArenaPaymentSettings.to_json())

# convert the object into a dict
arena_payment_settings_dict = arena_payment_settings_instance.to_dict()
# create an instance of ArenaPaymentSettings from a dict
arena_payment_settings_from_dict = ArenaPaymentSettings.from_dict(arena_payment_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


