# PaymentPrefPaymentPrefAchAchDomicileAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street1** | **str** |  | [optional] 
**street2** | **str** |  | [optional] 
**street3** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from main_openapi_client.models.payment_pref_payment_pref_ach_ach_domicile_address import PaymentPrefPaymentPrefAchAchDomicileAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPrefPaymentPrefAchAchDomicileAddress from a JSON string
payment_pref_payment_pref_ach_ach_domicile_address_instance = PaymentPrefPaymentPrefAchAchDomicileAddress.from_json(json)
# print the JSON string representation of the object
print(PaymentPrefPaymentPrefAchAchDomicileAddress.to_json())

# convert the object into a dict
payment_pref_payment_pref_ach_ach_domicile_address_dict = payment_pref_payment_pref_ach_ach_domicile_address_instance.to_dict()
# create an instance of PaymentPrefPaymentPrefAchAchDomicileAddress from a dict
payment_pref_payment_pref_ach_ach_domicile_address_from_dict = PaymentPrefPaymentPrefAchAchDomicileAddress.from_dict(payment_pref_payment_pref_ach_ach_domicile_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


