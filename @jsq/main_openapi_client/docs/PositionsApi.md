# main_openapi_client.PositionsApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_external_position**](PositionsApi.md#get_external_position) | **GET** /arenas/{arena_id}/external_positions/{external_position_id} | Gets position of a specific arena and source
[**get_opco_positions**](PositionsApi.md#get_opco_positions) | **GET** /arenas/{arena_id}/entities/{entity_id}/opco_positions | Get a list of the entity&#39;s positions in its directly-owned operating companies.
[**get_positions**](PositionsApi.md#get_positions) | **GET** /positions | Gets positions by ids with account, investor group, and investment entity ids.


# **get_external_position**
> ExternalPosition get_external_position(arena_id, external_position_id)

Gets position of a specific arena and source

Gets position of a specific arena and source

### Example


```python
import main_openapi_client
from main_openapi_client.models.external_position import ExternalPosition
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
    api_instance = main_openapi_client.PositionsApi(api_client)
    arena_id = 56 # int | Id of the arena to operate within
    external_position_id = 'external_position_id_example' # str | Url safe base64 encoded version of url encoded version of source_name:url encoded version of source_object_id.

    try:
        # Gets position of a specific arena and source
        api_response = api_instance.get_external_position(arena_id, external_position_id)
        print("The response of PositionsApi->get_external_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->get_external_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Id of the arena to operate within | 
 **external_position_id** | **str**| Url safe base64 encoded version of url encoded version of source_name:url encoded version of source_object_id. | 

### Return type

[**ExternalPosition**](ExternalPosition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A position for a specific arena, source name, and source object id. |  -  |
**400** | Request/response validation failed |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_opco_positions**
> List[Opco] get_opco_positions(arena_id, entity_id, exclude_inactive=exclude_inactive, as_of_date=as_of_date)

Get a list of the entity's positions in its directly-owned operating companies.

Get an un-paginated list of the entity's positions in its directly-owned operating companies.

### Example


```python
import main_openapi_client
from main_openapi_client.models.opco import Opco
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
    api_instance = main_openapi_client.PositionsApi(api_client)
    arena_id = 56 # int | Id of the arena to operate within
    entity_id = 56 # int | Id of the entity
    exclude_inactive = True # bool | Whether to exclude inactive objects from the response. (optional)
    as_of_date = 'as_of_date_example' # str | An end date of a period. Format should be YYYY-MM-DD. (optional)

    try:
        # Get a list of the entity's positions in its directly-owned operating companies.
        api_response = api_instance.get_opco_positions(arena_id, entity_id, exclude_inactive=exclude_inactive, as_of_date=as_of_date)
        print("The response of PositionsApi->get_opco_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->get_opco_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Id of the arena to operate within | 
 **entity_id** | **int**| Id of the entity | 
 **exclude_inactive** | **bool**| Whether to exclude inactive objects from the response. | [optional] 
 **as_of_date** | **str**| An end date of a period. Format should be YYYY-MM-DD. | [optional] 

### Return type

[**List[Opco]**](Opco.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of given entity&#39;s directly owned operating companies and its positions |  -  |
**404** | An expected resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_positions**
> List[PositionAttribute] get_positions(arena_id, position_ids=position_ids)

Gets positions by ids with account, investor group, and investment entity ids.

Gets positions by ids with account, investor group, and investment entity ids.

### Example


```python
import main_openapi_client
from main_openapi_client.models.position_attribute import PositionAttribute
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
    api_instance = main_openapi_client.PositionsApi(api_client)
    arena_id = 56 # int | Required arena_id to filter by.
    position_ids = ['position_ids_example'] # List[str] | Comma separated list of position ids. (optional)

    try:
        # Gets positions by ids with account, investor group, and investment entity ids.
        api_response = api_instance.get_positions(arena_id, position_ids=position_ids)
        print("The response of PositionsApi->get_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->get_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Required arena_id to filter by. | 
 **position_ids** | [**List[str]**](str.md)| Comma separated list of position ids. | [optional] 

### Return type

[**List[PositionAttribute]**](PositionAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of positions with account, investor group, and investment entity ids. |  -  |
**400** | Request/response validation failed |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

