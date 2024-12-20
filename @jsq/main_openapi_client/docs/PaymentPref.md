# PaymentPref

A payment preference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**payment_method** | **str** | Payment method for the payment preference: ACH, Wire or Check. | 
**verification_status** | **str** | Verification status for the payment preference: verified, unverified or error. | 
**wire_has_intermediary** | **bool** | For wire payment method only, whether the wire payment pref has an intermediary bank that wires transfer through.  | [optional] 
**wire_has_international_beneficiary_address** | **bool** | For wire payment method only, whether the wire payment pref has an international beneficiary address | [optional] 
**payment_pref_wire** | [**PaymentPrefPaymentPrefWire**](PaymentPrefPaymentPrefWire.md) |  | [optional] 
**payment_pref_ach** | [**PaymentPrefPaymentPrefAch**](PaymentPrefPaymentPrefAch.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.payment_pref import PaymentPref

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPref from a JSON string
payment_pref_instance = PaymentPref.from_json(json)
# print the JSON string representation of the object
print(PaymentPref.to_json())

# convert the object into a dict
payment_pref_dict = payment_pref_instance.to_dict()
# create an instance of PaymentPref from a dict
payment_pref_from_dict = PaymentPref.from_dict(payment_pref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


