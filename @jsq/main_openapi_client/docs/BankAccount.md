# BankAccount

A bank account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the bank account. | [readonly] 
**owner_name** | **str** | Name of the bank account owner. | [readonly] 
**account_number** | **str** | Bank account number. | [readonly] 
**routing_number** | **str** | Bank account routing number. | [readonly] 
**arena_id** | **int** | Arena ID this bank account belongs to. | [readonly] 
**ach_info** | [**BankAccountAchInfo**](BankAccountAchInfo.md) |  | [optional] 

## Example

```python
from main_openapi_client.models.bank_account import BankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccount from a JSON string
bank_account_instance = BankAccount.from_json(json)
# print the JSON string representation of the object
print(BankAccount.to_json())

# convert the object into a dict
bank_account_dict = bank_account_instance.to_dict()
# create an instance of BankAccount from a dict
bank_account_from_dict = BankAccount.from_dict(bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


