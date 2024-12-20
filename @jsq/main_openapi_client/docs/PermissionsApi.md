# main_openapi_client.PermissionsApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_granular_permissions**](PermissionsApi.md#get_granular_permissions) | **GET** /arenas/{arena_id}/users/{user_id}/granular_permissions | Returns a list of granular permissions given user has.
[**get_object_class_level_permissions**](PermissionsApi.md#get_object_class_level_permissions) | **GET** /object_class_level_permission | Determines if a user has object class level authorization provided as input an objectAuthorizationClass, [Permissions]. For staff users, permissions checks are only valid in an arena with ArenaFeatureFlags.advanced_permissions enabled.
[**get_object_level_permissions**](PermissionsApi.md#get_object_level_permissions) | **GET** /object_level_permission | Determines if a user has object level authorization provided as input an objectType, [IDs], and [Permissions]. For staff users, permissions checks are only valid in an arena with ArenaFeatureFlags.advanced_permissions enabled. For portal users, only read permissions checks are allowed.


# **get_granular_permissions**
> List[GranularPermission] get_granular_permissions(arena_id, user_id)

Returns a list of granular permissions given user has.

Returns a list of granular permissions given user has.

### Example


```python
import main_openapi_client
from main_openapi_client.models.granular_permission import GranularPermission
from main_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /internal/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = main_openapi_client.Configuration(
    host = "/internal/api/v1"
)


# Enter a context with an instance of the API client
with main_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = main_openapi_client.PermissionsApi(api_client)
    arena_id = 56 # int | Id of the arena to operate within
    user_id = 56 # int | User ID of the resource

    try:
        # Returns a list of granular permissions given user has.
        api_response = api_instance.get_granular_permissions(arena_id, user_id)
        print("The response of PermissionsApi->get_granular_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_granular_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Id of the arena to operate within | 
 **user_id** | **int**| User ID of the resource | 

### Return type

[**List[GranularPermission]**](GranularPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of granular permissions |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_class_level_permissions**
> ObjectLevelPermission get_object_class_level_permissions(user_id, object_authorized_class, permissions)

Determines if a user has object class level authorization provided as input an objectAuthorizationClass, [Permissions]. For staff users, permissions checks are only valid in an arena with ArenaFeatureFlags.advanced_permissions enabled.

Determines if a user has object class level authorization provided as input an objectAuthorizationClass, [Permissions]. For staff users, permissions checks are only valid in an arena with ArenaFeatureFlags.advanced_permissions enabled.

### Example


```python
import main_openapi_client
from main_openapi_client.models.object_authorized_class import ObjectAuthorizedClass
from main_openapi_client.models.object_level_permission import ObjectLevelPermission
from main_openapi_client.models.permission import Permission
from main_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /internal/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = main_openapi_client.Configuration(
    host = "/internal/api/v1"
)


# Enter a context with an instance of the API client
with main_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = main_openapi_client.PermissionsApi(api_client)
    user_id = 56 # int | Required user_id to filter by.
    object_authorized_class = main_openapi_client.ObjectAuthorizedClass() # ObjectAuthorizedClass | Required object_authorized_class to filter by. Should match an AuthorizedClass enum.
    permissions = [main_openapi_client.Permission()] # List[Permission] | List of object level permissions to filter by

    try:
        # Determines if a user has object class level authorization provided as input an objectAuthorizationClass, [Permissions]. For staff users, permissions checks are only valid in an arena with ArenaFeatureFlags.advanced_permissions enabled.
        api_response = api_instance.get_object_class_level_permissions(user_id, object_authorized_class, permissions)
        print("The response of PermissionsApi->get_object_class_level_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_object_class_level_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Required user_id to filter by. | 
 **object_authorized_class** | [**ObjectAuthorizedClass**](.md)| Required object_authorized_class to filter by. Should match an AuthorizedClass enum. | 
 **permissions** | [**List[Permission]**](Permission.md)| List of object level permissions to filter by | 

### Return type

[**ObjectLevelPermission**](ObjectLevelPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the permissioning object for the queried user and object type combination. |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_level_permissions**
> ObjectLevelPermission get_object_level_permissions(user_id, object_type, object_ids, permissions)

Determines if a user has object level authorization provided as input an objectType, [IDs], and [Permissions]. For staff users, permissions checks are only valid in an arena with ArenaFeatureFlags.advanced_permissions enabled. For portal users, only read permissions checks are allowed.

Determines if a user has object level authorization provided as input an objectType, [IDs], and [Permissions]. For staff users, permissions checks are only valid in an arena with ArenaFeatureFlags.advanced_permissions enabled. For portal users, only read permissions checks are allowed.

### Example


```python
import main_openapi_client
from main_openapi_client.models.object_level_permission import ObjectLevelPermission
from main_openapi_client.models.object_type import ObjectType
from main_openapi_client.models.permission import Permission
from main_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /internal/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = main_openapi_client.Configuration(
    host = "/internal/api/v1"
)


# Enter a context with an instance of the API client
with main_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = main_openapi_client.PermissionsApi(api_client)
    user_id = 56 # int | Required user_id to filter by.
    object_type = main_openapi_client.ObjectType() # ObjectType | Required object_type to filter by. Should match an ObjectType enum.
    object_ids = [56] # List[int] | List of objects_ids of the corresponding ObjectType
    permissions = [main_openapi_client.Permission()] # List[Permission] | List of object level permissions to filter by

    try:
        # Determines if a user has object level authorization provided as input an objectType, [IDs], and [Permissions]. For staff users, permissions checks are only valid in an arena with ArenaFeatureFlags.advanced_permissions enabled. For portal users, only read permissions checks are allowed.
        api_response = api_instance.get_object_level_permissions(user_id, object_type, object_ids, permissions)
        print("The response of PermissionsApi->get_object_level_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_object_level_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Required user_id to filter by. | 
 **object_type** | [**ObjectType**](.md)| Required object_type to filter by. Should match an ObjectType enum. | 
 **object_ids** | [**List[int]**](int.md)| List of objects_ids of the corresponding ObjectType | 
 **permissions** | [**List[Permission]**](Permission.md)| List of object level permissions to filter by | 

### Return type

[**ObjectLevelPermission**](ObjectLevelPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the permissioning object for the queried user and object type combination. |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

