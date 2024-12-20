# ObjectLevelPermission

Returns the permissioning object for the queried user and object type combination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_permission** | **bool** | Boolean if the user has permission based on the specified filters | [readonly] 

## Example

```python
from main_openapi_client.models.object_level_permission import ObjectLevelPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectLevelPermission from a JSON string
object_level_permission_instance = ObjectLevelPermission.from_json(json)
# print the JSON string representation of the object
print(ObjectLevelPermission.to_json())

# convert the object into a dict
object_level_permission_dict = object_level_permission_instance.to_dict()
# create an instance of ObjectLevelPermission from a dict
object_level_permission_from_dict = ObjectLevelPermission.from_dict(object_level_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


