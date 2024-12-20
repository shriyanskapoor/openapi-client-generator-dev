# PaymentPrefPaymentPrefWireWireBeneficiaryAddress


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
from main_openapi_client.models.payment_pref_payment_pref_wire_wire_beneficiary_address import PaymentPrefPaymentPrefWireWireBeneficiaryAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPrefPaymentPrefWireWireBeneficiaryAddress from a JSON string
payment_pref_payment_pref_wire_wire_beneficiary_address_instance = PaymentPrefPaymentPrefWireWireBeneficiaryAddress.from_json(json)
# print the JSON string representation of the object
print(PaymentPrefPaymentPrefWireWireBeneficiaryAddress.to_json())

# convert the object into a dict
payment_pref_payment_pref_wire_wire_beneficiary_address_dict = payment_pref_payment_pref_wire_wire_beneficiary_address_instance.to_dict()
# create an instance of PaymentPrefPaymentPrefWireWireBeneficiaryAddress from a dict
payment_pref_payment_pref_wire_wire_beneficiary_address_from_dict = PaymentPrefPaymentPrefWireWireBeneficiaryAddress.from_dict(payment_pref_payment_pref_wire_wire_beneficiary_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


