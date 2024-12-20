# PaymentPrefPaymentPrefWire

A payment preference containing wire specific info. This will only have valid fields if payment pref method is wire. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wire_beneficiary_name** | **str** | Optional wire beneficiary name | [optional] 
**wire_beneficiary_account_number** | **str** | Wire beneficiary account number | 
**wire_bank_name** | **str** | Wire bank name | 
**wire_aba_number** | **str** | Wire aba number (usually routing number) | 
**wire_has_intermediary** | **bool** | For wire payment method only, whether the wire payment pref has an intermediary bank that wires transfer through.  | 
**wire_has_international_beneficiary_address** | **bool** | Boolean to determine whether a wire has an international beneficiary address. Can be None if not applicable.  | [optional] 
**wire_reference_to_beneficiary** | **str** | Wire reference to beneficiary | [optional] 
**wire_obi** | **Dict[str, object]** |  | [optional] 
**wire_bbi** | **Dict[str, object]** |  | [optional] 
**wire_beneficiary_address** | [**PaymentPrefPaymentPrefWireWireBeneficiaryAddress**](PaymentPrefPaymentPrefWireWireBeneficiaryAddress.md) |  | 

## Example

```python
from main_openapi_client.models.payment_pref_payment_pref_wire import PaymentPrefPaymentPrefWire

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPrefPaymentPrefWire from a JSON string
payment_pref_payment_pref_wire_instance = PaymentPrefPaymentPrefWire.from_json(json)
# print the JSON string representation of the object
print(PaymentPrefPaymentPrefWire.to_json())

# convert the object into a dict
payment_pref_payment_pref_wire_dict = payment_pref_payment_pref_wire_instance.to_dict()
# create an instance of PaymentPrefPaymentPrefWire from a dict
payment_pref_payment_pref_wire_from_dict = PaymentPrefPaymentPrefWire.from_dict(payment_pref_payment_pref_wire_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


