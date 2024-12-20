# main_openapi_client.ArenasApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_allocation_types**](ArenasApi.md#get_allocation_types) | **GET** /arenas/{arena_id}/allocation_types | Get a list of allocation types for the given arena
[**get_arena**](ArenasApi.md#get_arena) | **GET** /arenas/{id}/ | Get arena
[**get_arena_net_income_types**](ArenasApi.md#get_arena_net_income_types) | **GET** /arenas/{arena_id}/net_income_allocation_types | Get allocation types for a given arena by ID
[**get_arena_payment_settings**](ArenasApi.md#get_arena_payment_settings) | **GET** /arenas/{arena_id}/payment_settings | Get payment settings for a given arena
[**get_arenas**](ArenasApi.md#get_arenas) | **GET** /arenas/ | Get a list of Arenas
[**get_arenas_manage_account_contact_settings**](ArenasApi.md#get_arenas_manage_account_contact_settings) | **GET** /arenas/manage_account_contact_settings | Get manage account contact settings for a given arenas


# **get_allocation_types**
> List[AllocationType] get_allocation_types(arena_id)

Get a list of allocation types for the given arena

Get an un-paginated list of allocation types.

### Example


```python
import main_openapi_client
from main_openapi_client.models.allocation_type import AllocationType
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
    api_instance = main_openapi_client.ArenasApi(api_client)
    arena_id = 56 # int | Id of the arena to operate within

    try:
        # Get a list of allocation types for the given arena
        api_response = api_instance.get_allocation_types(arena_id)
        print("The response of ArenasApi->get_allocation_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArenasApi->get_allocation_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Id of the arena to operate within | 

### Return type

[**List[AllocationType]**](AllocationType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of allocation types |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_arena**
> Arena get_arena(id)

Get arena

Get an arena by ID.

### Example


```python
import main_openapi_client
from main_openapi_client.models.arena import Arena
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
    api_instance = main_openapi_client.ArenasApi(api_client)
    id = 56 # int | Id of the resource

    try:
        # Get arena
        api_response = api_instance.get_arena(id)
        print("The response of ArenasApi->get_arena:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArenasApi->get_arena: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the resource | 

### Return type

[**Arena**](Arena.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An arena |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_arena_net_income_types**
> List[ArenaNetIncomeType] get_arena_net_income_types(arena_id)

Get allocation types for a given arena by ID

Get allocationTypes for a given arena by ID

### Example


```python
import main_openapi_client
from main_openapi_client.models.arena_net_income_type import ArenaNetIncomeType
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
    api_instance = main_openapi_client.ArenasApi(api_client)
    arena_id = 56 # int | Id of the arena to operate within

    try:
        # Get allocation types for a given arena by ID
        api_response = api_instance.get_arena_net_income_types(arena_id)
        print("The response of ArenasApi->get_arena_net_income_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArenasApi->get_arena_net_income_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Id of the arena to operate within | 

### Return type

[**List[ArenaNetIncomeType]**](ArenaNetIncomeType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Allocation Types for a specific arena |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_arena_payment_settings**
> ArenaPaymentSettings get_arena_payment_settings(arena_id)

Get payment settings for a given arena

Get payment settings for a given arena by ID

### Example


```python
import main_openapi_client
from main_openapi_client.models.arena_payment_settings import ArenaPaymentSettings
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
    api_instance = main_openapi_client.ArenasApi(api_client)
    arena_id = 56 # int | Id of the arena to operate within

    try:
        # Get payment settings for a given arena
        api_response = api_instance.get_arena_payment_settings(arena_id)
        print("The response of ArenasApi->get_arena_payment_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArenasApi->get_arena_payment_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Id of the arena to operate within | 

### Return type

[**ArenaPaymentSettings**](ArenaPaymentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment settings for a specific arena |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_arenas**
> List[Arena] get_arenas(ids=ids)

Get a list of Arenas

Get an un-paginated list of all arenas, optionally filtered by a list of arena IDs.

### Example


```python
import main_openapi_client
from main_openapi_client.models.arena import Arena
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
    api_instance = main_openapi_client.ArenasApi(api_client)
    ids = [56] # List[int] | Optional comma separated list of ids to filter resources by. (optional)

    try:
        # Get a list of Arenas
        api_response = api_instance.get_arenas(ids=ids)
        print("The response of ArenasApi->get_arenas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArenasApi->get_arenas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| Optional comma separated list of ids to filter resources by. | [optional] 

### Return type

[**List[Arena]**](Arena.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of arenas |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_arenas_manage_account_contact_settings**
> List[ArenaManageAccountContactSettings] get_arenas_manage_account_contact_settings(arena_ids)

Get manage account contact settings for a given arenas

Get manage account contact settings for a given arenas

### Example


```python
import main_openapi_client
from main_openapi_client.models.arena_manage_account_contact_settings import ArenaManageAccountContactSettings
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
    api_instance = main_openapi_client.ArenasApi(api_client)
    arena_ids = [56] # List[int] | List of arena_ids

    try:
        # Get manage account contact settings for a given arenas
        api_response = api_instance.get_arenas_manage_account_contact_settings(arena_ids)
        print("The response of ArenasApi->get_arenas_manage_account_contact_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArenasApi->get_arenas_manage_account_contact_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_ids** | [**List[int]**](int.md)| List of arena_ids | 

### Return type

[**List[ArenaManageAccountContactSettings]**](ArenaManageAccountContactSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manage Account Contact Settings for a specific arena |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

