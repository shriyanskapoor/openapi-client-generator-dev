# PaymentPrefPaymentPrefAch

A payment preference containing ach specific info. This will only have valid fields if payment pref method is ach. Otherwise, it will contain an empty object 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ach_account_name** | **str** | Optional ach account name | [optional] 
**ach_bank_name** | **str** | Ach bank name | 
**ach_account_number** | **str** | ach account number | 
**ach_routing_number** | **str** | ach routing number | 
**ach_account_type** | **str** | ach account type | 
**ach_account_ownership** | **str** | ach account ownership | [optional] 
**ach_additional_instructions** | **str** | ach account ownership | [optional] 
**ach_domicile_address** | [**PaymentPrefPaymentPrefAchAchDomicileAddress**](PaymentPrefPaymentPrefAchAchDomicileAddress.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.payment_pref_payment_pref_ach import PaymentPrefPaymentPrefAch

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPrefPaymentPrefAch from a JSON string
payment_pref_payment_pref_ach_instance = PaymentPrefPaymentPrefAch.from_json(json)
# print the JSON string representation of the object
print(PaymentPrefPaymentPrefAch.to_json())

# convert the object into a dict
payment_pref_payment_pref_ach_dict = payment_pref_payment_pref_ach_instance.to_dict()
# create an instance of PaymentPrefPaymentPrefAch from a dict
payment_pref_payment_pref_ach_from_dict = PaymentPrefPaymentPrefAch.from_dict(payment_pref_payment_pref_ach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


