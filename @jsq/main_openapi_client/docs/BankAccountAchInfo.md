# BankAccountAchInfo

A bank account containing ach specific info. This will only have valid fields if the bank account is set to ach. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ach_instructions_account_owner_name** | **str** | Optional ach account owner name | [optional] 

## Example

```python
from main_openapi_client.models.bank_account_ach_info import BankAccountAchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountAchInfo from a JSON string
bank_account_ach_info_instance = BankAccountAchInfo.from_json(json)
# print the JSON string representation of the object
print(BankAccountAchInfo.to_json())

# convert the object into a dict
bank_account_ach_info_dict = bank_account_ach_info_instance.to_dict()
# create an instance of BankAccountAchInfo from a dict
bank_account_ach_info_from_dict = BankAccountAchInfo.from_dict(bank_account_ach_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


