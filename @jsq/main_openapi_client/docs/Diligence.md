# Diligence

Diligence used as a model for keeping track of investor diligence actions on a variety of items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the diligence object in the DB. | 
**external_object_type** | [**DiligenceExternalObjectType**](DiligenceExternalObjectType.md) |  | 
**external_object_id** | **int** | Number representing the id of the external object type in the external object type table. | 
**diligence_type** | [**DiligenceType**](DiligenceType.md) |  | 
**status** | [**DiligenceStatus**](DiligenceStatus.md) |  | 
**reviewer_user_id** | **int** | ID of user who reviewed the diligence | 
**review_start_date** | **datetime** | Date-time the diligence was moved into review status | 
**review_end_date** | **datetime** | Date-time the diligence was moved out of review status | 
**peer_reviewer_user_id** | **int** | ID of user who peer-reviewed the diligence | 
**peer_review_start_date** | **datetime** | Date-time the diligence was moved into peer-review status | 
**peer_review_end_date** | **datetime** | Date-time the diligence was moved out of peer-review status | 
**arena_id** | **int** | Arena ID the diligence is located in | 
**modified_at** | **datetime** | Date-time the diligence was last modified | 
**created_at** | **datetime** | Date-time the diligence was created | 
**created_by** | **int** | FK to the user id who created the diligence | 
**current_investor_diligence_risk_log_id** | **int** | FK to the Investor Diligence Risk Log | 
**category** | [**DiligenceCategory**](DiligenceCategory.md) |  | 
**external_reference_key** | **str** | String of external reference | 
**name** | **str** | Name of the diligence | 
**perform_recurring_check** | **bool** | Only used for watchlist diligences. Used to determine if recurring checks is enabled | 
**other_info** | **Dict[str, object]** | Other key values info for the diligence | [optional] 

## Example

```python
from main_openapi_client.models.diligence import Diligence

# TODO update the JSON string below
json = "{}"
# create an instance of Diligence from a JSON string
diligence_instance = Diligence.from_json(json)
# print the JSON string representation of the object
print(Diligence.to_json())

# convert the object into a dict
diligence_dict = diligence_instance.to_dict()
# create an instance of Diligence from a dict
diligence_from_dict = Diligence.from_dict(diligence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


