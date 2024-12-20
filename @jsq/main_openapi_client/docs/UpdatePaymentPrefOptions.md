# UpdatePaymentPrefOptions

An object provided when updating (patch) payment prefs. Note: presently only supports verification_status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_status** | **str** | Verification status for the payment preference: verified, unverified or error. | [optional] 

## Example

```python
from main_openapi_client.models.update_payment_pref_options import UpdatePaymentPrefOptions

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaymentPrefOptions from a JSON string
update_payment_pref_options_instance = UpdatePaymentPrefOptions.from_json(json)
# print the JSON string representation of the object
print(UpdatePaymentPrefOptions.to_json())

# convert the object into a dict
update_payment_pref_options_dict = update_payment_pref_options_instance.to_dict()
# create an instance of UpdatePaymentPrefOptions from a dict
update_payment_pref_options_from_dict = UpdatePaymentPrefOptions.from_dict(update_payment_pref_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


