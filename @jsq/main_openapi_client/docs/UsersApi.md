# main_openapi_client.UsersApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_edit_access**](UsersApi.md#get_accounts_edit_access) | **GET** /users/{user_id}/account-contact/edit-access | Get accounts with edit access
[**get_accounts_view_access**](UsersApi.md#get_accounts_view_access) | **GET** /users/{user_id}/account-contact/view-access | Get accounts with view access
[**get_user_arena_roles**](UsersApi.md#get_user_arena_roles) | **GET** /users/{user_id}/arena_roles | Get roles for each arena
[**get_user_distribution_batch**](UsersApi.md#get_user_distribution_batch) | **GET** /users/{user_id}/distribution_batch/{distribution_batch_id} | Get distribution batch with authorization checks
[**get_user_distribution_batch_distributions**](UsersApi.md#get_user_distribution_batch_distributions) | **GET** /users/{user_id}/distribution_batch/{distribution_batch_id}/distributions | Get distribution batch distributions for a user_id with authorization checks
[**get_users**](UsersApi.md#get_users) | **GET** /users | Get users


# **get_accounts_edit_access**
> List[int] get_accounts_edit_access(user_id, account_ids=account_ids)

Get accounts with edit access

Returns account IDs that the user has edit access to.

### Example


```python
import main_openapi_client
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
    api_instance = main_openapi_client.UsersApi(api_client)
    user_id = 56 # int | User ID of the resource
    account_ids = [56] # List[int] | Comma separated list of account ids. (optional)

    try:
        # Get accounts with edit access
        api_response = api_instance.get_accounts_edit_access(user_id, account_ids=account_ids)
        print("The response of UsersApi->get_accounts_edit_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_accounts_edit_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the resource | 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids. | [optional] 

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of account IDs with edit access |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_view_access**
> List[int] get_accounts_view_access(user_id, account_ids=account_ids)

Get accounts with view access

Returns account IDs that the user has view access to.

### Example


```python
import main_openapi_client
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
    api_instance = main_openapi_client.UsersApi(api_client)
    user_id = 56 # int | User ID of the resource
    account_ids = [56] # List[int] | Comma separated list of account ids. (optional)

    try:
        # Get accounts with view access
        api_response = api_instance.get_accounts_view_access(user_id, account_ids=account_ids)
        print("The response of UsersApi->get_accounts_view_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_accounts_view_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the resource | 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids. | [optional] 

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of account IDs with view access |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_arena_roles**
> List[ArenaRoles] get_user_arena_roles(user_id)

Get roles for each arena

Get roles for each areana

### Example


```python
import main_openapi_client
from main_openapi_client.models.arena_roles import ArenaRoles
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
    api_instance = main_openapi_client.UsersApi(api_client)
    user_id = 56 # int | User ID of the resource

    try:
        # Get roles for each arena
        api_response = api_instance.get_user_arena_roles(user_id)
        print("The response of UsersApi->get_user_arena_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_arena_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the resource | 

### Return type

[**List[ArenaRoles]**](ArenaRoles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of ArenaRoles |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_distribution_batch**
> DistributionBatch get_user_distribution_batch(user_id, distribution_batch_id)

Get distribution batch with authorization checks

Get a distribution batch by ID. This does handle auth checks (object and role based permissions)

### Example


```python
import main_openapi_client
from main_openapi_client.models.distribution_batch import DistributionBatch
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
    api_instance = main_openapi_client.UsersApi(api_client)
    user_id = 56 # int | User ID of the resource
    distribution_batch_id = 56 # int | Id of the distribution_batch

    try:
        # Get distribution batch with authorization checks
        api_response = api_instance.get_user_distribution_batch(user_id, distribution_batch_id)
        print("The response of UsersApi->get_user_distribution_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_distribution_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the resource | 
 **distribution_batch_id** | **int**| Id of the distribution_batch | 

### Return type

[**DistributionBatch**](DistributionBatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A distribution batch |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_distribution_batch_distributions**
> List[Distribution] get_user_distribution_batch_distributions(user_id, distribution_batch_id)

Get distribution batch distributions for a user_id with authorization checks

Get an un-paginated list of distributions that a user_id is authorized to view taking into account both role-based and object-level permissioning.

### Example


```python
import main_openapi_client
from main_openapi_client.models.distribution import Distribution
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
    api_instance = main_openapi_client.UsersApi(api_client)
    user_id = 56 # int | User ID of the resource
    distribution_batch_id = 56 # int | Id of the distribution_batch

    try:
        # Get distribution batch distributions for a user_id with authorization checks
        api_response = api_instance.get_user_distribution_batch_distributions(user_id, distribution_batch_id)
        print("The response of UsersApi->get_user_distribution_batch_distributions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_distribution_batch_distributions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the resource | 
 **distribution_batch_id** | **int**| Id of the distribution_batch | 

### Return type

[**List[Distribution]**](Distribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of distributions |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> List[User] get_users(global_ids=global_ids, ids=ids)

Get users

Get an un-paginated list of users filtered by a required list of either DB or global user IDs.

### Example


```python
import main_openapi_client
from main_openapi_client.models.user import User
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
    api_instance = main_openapi_client.UsersApi(api_client)
    global_ids = ['global_ids_example'] # List[str] | Optional comma separated list of global ids to filter resources by. (optional)
    ids = [56] # List[int] | Optional comma separated list of ids to filter resources by. (optional)

    try:
        # Get users
        api_response = api_instance.get_users(global_ids=global_ids, ids=ids)
        print("The response of UsersApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_ids** | [**List[str]**](str.md)| Optional comma separated list of global ids to filter resources by. | [optional] 
 **ids** | [**List[int]**](int.md)| Optional comma separated list of ids to filter resources by. | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of users |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

