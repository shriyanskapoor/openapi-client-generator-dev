# Distribution

A Distribution that is part of a distribution batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**arena_id** | **int** | Arena ID this distribution batch belongs to. | [readonly] 
**position_id** | **int** | FK to position ID this distribution belongs to | 
**payment_pref_id** | **int** | FK to payment pref for this distribution&#39;s position&#39;s payment pref | 
**amount** | **float** | Amount to be distributed | 
**amount_payable** | **float** | Amount to be distributed netting any amount adjusted or reinvested | 
**manual_settlement_date** | **date** | The date the distribution was manually settled (if applicable) | 
**has_legacy_payment** | **bool** | Whether or not the distribution has a legacy payment associated with it (that has not been marked as canceled or failed or voided) | 

## Example

```python
from main_openapi_client.models.distribution import Distribution

# TODO update the JSON string below
json = "{}"
# create an instance of Distribution from a JSON string
distribution_instance = Distribution.from_json(json)
# print the JSON string representation of the object
print(Distribution.to_json())

# convert the object into a dict
distribution_dict = distribution_instance.to_dict()
# create an instance of Distribution from a dict
distribution_from_dict = Distribution.from_dict(distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


