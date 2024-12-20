# main_openapi_client.FeatureFlagsApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_arena_feature_flags**](FeatureFlagsApi.md#bulk_update_arena_feature_flags) | **POST** /feature-flags/arena-feature-flags/{arena_id}/ | Bulk Update Arena Feature Flags
[**bulk_update_developer_feature_flags**](FeatureFlagsApi.md#bulk_update_developer_feature_flags) | **POST** /feature-flags/developer-feature-flags/ | Bulk Update Developer Feature Flags
[**get_arena_feature_flag**](FeatureFlagsApi.md#get_arena_feature_flag) | **GET** /feature-flags/arena-feature-flags/{arena_id}/{feature_flag_name}/ | Arena Feature Flag
[**get_arena_feature_flags**](FeatureFlagsApi.md#get_arena_feature_flags) | **GET** /feature-flags/arena-feature-flags/{arena_id}/ | Feature Flags for Arena
[**get_developer_feature_flag**](FeatureFlagsApi.md#get_developer_feature_flag) | **GET** /feature-flags/developer-feature-flags/{feature_flag_name}/ | Developer Feature Flag
[**get_developer_feature_flags**](FeatureFlagsApi.md#get_developer_feature_flags) | **GET** /feature-flags/developer-feature-flags/ | Developer Feature Flags
[**update_arena_feature_flag**](FeatureFlagsApi.md#update_arena_feature_flag) | **PATCH** /feature-flags/arena-feature-flags/{arena_id}/{feature_flag_name}/ | Update Arena Feature Flag
[**update_developer_feature_flag**](FeatureFlagsApi.md#update_developer_feature_flag) | **PATCH** /feature-flags/developer-feature-flags/{feature_flag_name}/ | Update Developer Feature Flag


# **bulk_update_arena_feature_flags**
> bulk_update_arena_feature_flags(arena_id, bulk_update_feature_flags=bulk_update_feature_flags)

Bulk Update Arena Feature Flags

Bulk update the state of arena feature flags.

### Example

* Api Key Authentication (csrf-token):

```python
import main_openapi_client
from main_openapi_client.models.bulk_update_feature_flags import BulkUpdateFeatureFlags
from main_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /internal/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = main_openapi_client.Configuration(
    host = "/internal/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf-token
configuration.api_key['csrf-token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf-token'] = 'Bearer'

# Enter a context with an instance of the API client
with main_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = main_openapi_client.FeatureFlagsApi(api_client)
    arena_id = 56 # int | Id of the arena to operate within
    bulk_update_feature_flags = main_openapi_client.BulkUpdateFeatureFlags() # BulkUpdateFeatureFlags | Fields used to update arena feature flags in bulk. (optional)

    try:
        # Bulk Update Arena Feature Flags
        api_instance.bulk_update_arena_feature_flags(arena_id, bulk_update_feature_flags=bulk_update_feature_flags)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->bulk_update_arena_feature_flags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Id of the arena to operate within | 
 **bulk_update_feature_flags** | [**BulkUpdateFeatureFlags**](BulkUpdateFeatureFlags.md)| Fields used to update arena feature flags in bulk. | [optional] 

### Return type

void (empty response body)

### Authorization

[csrf-token](../README.md#csrf-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Bulk updates were succesfully completed. |  -  |
**400** | Request/response validation failed |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_developer_feature_flags**
> bulk_update_developer_feature_flags(bulk_update_feature_flags=bulk_update_feature_flags)

Bulk Update Developer Feature Flags

Bulk update the state of developer feature flags.

### Example

* Api Key Authentication (csrf-token):

```python
import main_openapi_client
from main_openapi_client.models.bulk_update_feature_flags import BulkUpdateFeatureFlags
from main_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /internal/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = main_openapi_client.Configuration(
    host = "/internal/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf-token
configuration.api_key['csrf-token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf-token'] = 'Bearer'

# Enter a context with an instance of the API client
with main_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = main_openapi_client.FeatureFlagsApi(api_client)
    bulk_update_feature_flags = main_openapi_client.BulkUpdateFeatureFlags() # BulkUpdateFeatureFlags | Fields used to update developer feature flags in bulk. (optional)

    try:
        # Bulk Update Developer Feature Flags
        api_instance.bulk_update_developer_feature_flags(bulk_update_feature_flags=bulk_update_feature_flags)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->bulk_update_developer_feature_flags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_update_feature_flags** | [**BulkUpdateFeatureFlags**](BulkUpdateFeatureFlags.md)| Fields used to update developer feature flags in bulk. | [optional] 

### Return type

void (empty response body)

### Authorization

[csrf-token](../README.md#csrf-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Bulk updates were succesfully completed. |  -  |
**400** | Request/response validation failed |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_arena_feature_flag**
> FeatureFlag get_arena_feature_flag(arena_id, feature_flag_name)

Arena Feature Flag

Retrieves an arena feature flag by feature flag name and arena domain

### Example


```python
import main_openapi_client
from main_openapi_client.models.feature_flag import FeatureFlag
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
    api_instance = main_openapi_client.FeatureFlagsApi(api_client)
    arena_id = 56 # int | Id of the arena to operate within
    feature_flag_name = 'feature_flag_name_example' # str | Name of the feature flag to retrieve

    try:
        # Arena Feature Flag
        api_response = api_instance.get_arena_feature_flag(arena_id, feature_flag_name)
        print("The response of FeatureFlagsApi->get_arena_feature_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->get_arena_feature_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Id of the arena to operate within | 
 **feature_flag_name** | **str**| Name of the feature flag to retrieve | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A feature flag |  -  |
**400** | Request/response validation failed |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_arena_feature_flags**
> List[FeatureFlag] get_arena_feature_flags(arena_id)

Feature Flags for Arena

Retrieves all arena-level feature flags for an arena.

### Example


```python
import main_openapi_client
from main_openapi_client.models.feature_flag import FeatureFlag
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
    api_instance = main_openapi_client.FeatureFlagsApi(api_client)
    arena_id = 56 # int | Id of the arena to operate within

    try:
        # Feature Flags for Arena
        api_response = api_instance.get_arena_feature_flags(arena_id)
        print("The response of FeatureFlagsApi->get_arena_feature_flags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->get_arena_feature_flags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Id of the arena to operate within | 

### Return type

[**List[FeatureFlag]**](FeatureFlag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of feature flags |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_developer_feature_flag**
> FeatureFlag get_developer_feature_flag(feature_flag_name)

Developer Feature Flag

Retrieves a developer feature flag by name.

### Example


```python
import main_openapi_client
from main_openapi_client.models.feature_flag import FeatureFlag
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
    api_instance = main_openapi_client.FeatureFlagsApi(api_client)
    feature_flag_name = 'feature_flag_name_example' # str | Name of the feature flag to retrieve

    try:
        # Developer Feature Flag
        api_response = api_instance.get_developer_feature_flag(feature_flag_name)
        print("The response of FeatureFlagsApi->get_developer_feature_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->get_developer_feature_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_flag_name** | **str**| Name of the feature flag to retrieve | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A feature flag |  -  |
**400** | Request/response validation failed |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_developer_feature_flags**
> List[FeatureFlag] get_developer_feature_flags()

Developer Feature Flags

Retrieves all developer feature flags.

### Example


```python
import main_openapi_client
from main_openapi_client.models.feature_flag import FeatureFlag
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
    api_instance = main_openapi_client.FeatureFlagsApi(api_client)

    try:
        # Developer Feature Flags
        api_response = api_instance.get_developer_feature_flags()
        print("The response of FeatureFlagsApi->get_developer_feature_flags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->get_developer_feature_flags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FeatureFlag]**](FeatureFlag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of feature flags |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_arena_feature_flag**
> FeatureFlag update_arena_feature_flag(arena_id, feature_flag_name, update_feature_flag=update_feature_flag)

Update Arena Feature Flag

Update a developer feature flag

### Example


```python
import main_openapi_client
from main_openapi_client.models.feature_flag import FeatureFlag
from main_openapi_client.models.update_feature_flag import UpdateFeatureFlag
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
    api_instance = main_openapi_client.FeatureFlagsApi(api_client)
    arena_id = 56 # int | Id of the arena to operate within
    feature_flag_name = 'feature_flag_name_example' # str | Name of the feature flag to retrieve
    update_feature_flag = main_openapi_client.UpdateFeatureFlag() # UpdateFeatureFlag | Fields used to update (patch) an arena feature flag (optional)

    try:
        # Update Arena Feature Flag
        api_response = api_instance.update_arena_feature_flag(arena_id, feature_flag_name, update_feature_flag=update_feature_flag)
        print("The response of FeatureFlagsApi->update_arena_feature_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->update_arena_feature_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Id of the arena to operate within | 
 **feature_flag_name** | **str**| Name of the feature flag to retrieve | 
 **update_feature_flag** | [**UpdateFeatureFlag**](UpdateFeatureFlag.md)| Fields used to update (patch) an arena feature flag | [optional] 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A feature flag |  -  |
**400** | Request/response validation failed |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_developer_feature_flag**
> FeatureFlag update_developer_feature_flag(feature_flag_name, update_feature_flag=update_feature_flag)

Update Developer Feature Flag

Update a developer feature flag

### Example


```python
import main_openapi_client
from main_openapi_client.models.feature_flag import FeatureFlag
from main_openapi_client.models.update_feature_flag import UpdateFeatureFlag
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
    api_instance = main_openapi_client.FeatureFlagsApi(api_client)
    feature_flag_name = 'feature_flag_name_example' # str | Name of the feature flag to retrieve
    update_feature_flag = main_openapi_client.UpdateFeatureFlag() # UpdateFeatureFlag | Fields used to update (patch) a developer feature flag (optional)

    try:
        # Update Developer Feature Flag
        api_response = api_instance.update_developer_feature_flag(feature_flag_name, update_feature_flag=update_feature_flag)
        print("The response of FeatureFlagsApi->update_developer_feature_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->update_developer_feature_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_flag_name** | **str**| Name of the feature flag to retrieve | 
 **update_feature_flag** | [**UpdateFeatureFlag**](UpdateFeatureFlag.md)| Fields used to update (patch) a developer feature flag | [optional] 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A feature flag |  -  |
**400** | Request/response validation failed |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

