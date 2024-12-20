# UpdatePositionsPaymentPrefSuccessResponse

Update Positions Success Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_ids** | **List[int]** | List of position IDs | [optional] 

## Example

```python
from main_openapi_client.models.update_positions_payment_pref_success_response import UpdatePositionsPaymentPrefSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePositionsPaymentPrefSuccessResponse from a JSON string
update_positions_payment_pref_success_response_instance = UpdatePositionsPaymentPrefSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(UpdatePositionsPaymentPrefSuccessResponse.to_json())

# convert the object into a dict
update_positions_payment_pref_success_response_dict = update_positions_payment_pref_success_response_instance.to_dict()
# create an instance of UpdatePositionsPaymentPrefSuccessResponse from a dict
update_positions_payment_pref_success_response_from_dict = UpdatePositionsPaymentPrefSuccessResponse.from_dict(update_positions_payment_pref_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


