# main_openapi_client.EntitiesApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_distribution_batch_ids_for_entity_id**](EntitiesApi.md#get_distribution_batch_ids_for_entity_id) | **GET** /entities/{id}/distribution_batch_ids | Get list of distribution batch ids for an entity
[**get_entities_with_positions**](EntitiesApi.md#get_entities_with_positions) | **GET** /arenas/{arena_id}/entities | Get a list of investment entities with their positions in an arena
[**get_entity**](EntitiesApi.md#get_entity) | **GET** /entities/{id} | Get an entity (AccountModel)
[**get_entity_ids**](EntitiesApi.md#get_entity_ids) | **GET** /entity-ids | Get entity ids
[**get_entity_position_ids**](EntitiesApi.md#get_entity_position_ids) | **GET** /entities/{id}/position_ids | Get list of position ids in an investment entity.
[**get_entity_positions**](EntitiesApi.md#get_entity_positions) | **GET** /entities/{id}/positions | Get a list of positions in an investment entity.


# **get_distribution_batch_ids_for_entity_id**
> EntityDistributionBatchIds get_distribution_batch_ids_for_entity_id(id, start_date=start_date, end_date=end_date, include_deleted=include_deleted)

Get list of distribution batch ids for an entity

Get list of distribution batch ids for an entity.

### Example


```python
import main_openapi_client
from main_openapi_client.models.entity_distribution_batch_ids import EntityDistributionBatchIds
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
    api_instance = main_openapi_client.EntitiesApi(api_client)
    id = 56 # int | Id of the resource
    start_date = '2013-10-20T19:20:30+01:00' # datetime | A start date of a period. Format should be YYYY-MM-DD. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | An end date of a period. Format should be YYYY-MM-DD. (optional)
    include_deleted = True # bool | Whether to include deleted objects in the response. (optional)

    try:
        # Get list of distribution batch ids for an entity
        api_response = api_instance.get_distribution_batch_ids_for_entity_id(id, start_date=start_date, end_date=end_date, include_deleted=include_deleted)
        print("The response of EntitiesApi->get_distribution_batch_ids_for_entity_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_distribution_batch_ids_for_entity_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the resource | 
 **start_date** | **datetime**| A start date of a period. Format should be YYYY-MM-DD. | [optional] 
 **end_date** | **datetime**| An end date of a period. Format should be YYYY-MM-DD. | [optional] 
 **include_deleted** | **bool**| Whether to include deleted objects in the response. | [optional] 

### Return type

[**EntityDistributionBatchIds**](EntityDistributionBatchIds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The count of distribution batches for an entity |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entities_with_positions**
> List[DetailedEntity] get_entities_with_positions(arena_id, entity_ids=entity_ids)

Get a list of investment entities with their positions in an arena

Get an un-paginated list of investment entities with their positions.

### Example


```python
import main_openapi_client
from main_openapi_client.models.detailed_entity import DetailedEntity
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
    api_instance = main_openapi_client.EntitiesApi(api_client)
    arena_id = 56 # int | Id of the arena to operate within
    entity_ids = ['entity_ids_example'] # List[str] | Comma separated list of entity ids. (optional)

    try:
        # Get a list of investment entities with their positions in an arena
        api_response = api_instance.get_entities_with_positions(arena_id, entity_ids=entity_ids)
        print("The response of EntitiesApi->get_entities_with_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entities_with_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arena_id** | **int**| Id of the arena to operate within | 
 **entity_ids** | [**List[str]**](str.md)| Comma separated list of entity ids. | [optional] 

### Return type

[**List[DetailedEntity]**](DetailedEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of entities with detailed information |  -  |
**400** | Request/response validation failed |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity**
> Entity get_entity(id)

Get an entity (AccountModel)

Get the name of the provided entity_id

### Example


```python
import main_openapi_client
from main_openapi_client.models.entity import Entity
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
    api_instance = main_openapi_client.EntitiesApi(api_client)
    id = 56 # int | Id of the resource

    try:
        # Get an entity (AccountModel)
        api_response = api_instance.get_entity(id)
        print("The response of EntitiesApi->get_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the resource | 

### Return type

[**Entity**](Entity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An entity object (AccountModel) |  -  |
**400** | Request/response validation failed |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_ids**
> List[int] get_entity_ids(is_fund_admin=is_fund_admin)

Get entity ids

Get an un-paginated list of entity ids filtered by query params

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
    api_instance = main_openapi_client.EntitiesApi(api_client)
    is_fund_admin = True # bool | Flag to fetch FA only resource. (optional)

    try:
        # Get entity ids
        api_response = api_instance.get_entity_ids(is_fund_admin=is_fund_admin)
        print("The response of EntitiesApi->get_entity_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entity_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_fund_admin** | **bool**| Flag to fetch FA only resource. | [optional] 

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
**200** | An array of integers |  -  |
**400** | Request/response validation failed |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_position_ids**
> EntityPositionIds get_entity_position_ids(id, start_date=start_date, end_date=end_date, include_deleted=include_deleted, exclude_inactive=exclude_inactive)

Get list of position ids in an investment entity.

Get position ids in an investment entity for a date range with options of excluding inactive and including deleted positions.

### Example


```python
import main_openapi_client
from main_openapi_client.models.entity_position_ids import EntityPositionIds
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
    api_instance = main_openapi_client.EntitiesApi(api_client)
    id = 56 # int | Id of the resource
    start_date = '2013-10-20T19:20:30+01:00' # datetime | A start date of a period. Format should be YYYY-MM-DD. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | An end date of a period. Format should be YYYY-MM-DD. (optional)
    include_deleted = True # bool | Whether to include deleted objects in the response. (optional)
    exclude_inactive = True # bool | Whether to exclude inactive objects from the response. (optional)

    try:
        # Get list of position ids in an investment entity.
        api_response = api_instance.get_entity_position_ids(id, start_date=start_date, end_date=end_date, include_deleted=include_deleted, exclude_inactive=exclude_inactive)
        print("The response of EntitiesApi->get_entity_position_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entity_position_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the resource | 
 **start_date** | **datetime**| A start date of a period. Format should be YYYY-MM-DD. | [optional] 
 **end_date** | **datetime**| An end date of a period. Format should be YYYY-MM-DD. | [optional] 
 **include_deleted** | **bool**| Whether to include deleted objects in the response. | [optional] 
 **exclude_inactive** | **bool**| Whether to exclude inactive objects from the response. | [optional] 

### Return type

[**EntityPositionIds**](EntityPositionIds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The List of position IDs for an entity |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_positions**
> List[Position] get_entity_positions(id, cab_period_ends=cab_period_ends, transaction_dates=transaction_dates)

Get a list of positions in an investment entity.

Get an un-paginated list of positions in an investment entity.

### Example


```python
import main_openapi_client
from main_openapi_client.models.position import Position
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
    api_instance = main_openapi_client.EntitiesApi(api_client)
    id = 56 # int | Id of the resource
    cab_period_ends = ['cab_period_ends_example'] # List[str] | Comma separated list of dates for calculating cab. Date format should be YYYY-MM-DDThh:mm:ssZ. (optional)
    transaction_dates = ['transaction_dates_example'] # List[str] | Comma separated list of dates. Format should be YYYY-MM-DDThh:mm:ssZ. (optional)

    try:
        # Get a list of positions in an investment entity.
        api_response = api_instance.get_entity_positions(id, cab_period_ends=cab_period_ends, transaction_dates=transaction_dates)
        print("The response of EntitiesApi->get_entity_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entity_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the resource | 
 **cab_period_ends** | [**List[str]**](str.md)| Comma separated list of dates for calculating cab. Date format should be YYYY-MM-DDThh:mm:ssZ. | [optional] 
 **transaction_dates** | [**List[str]**](str.md)| Comma separated list of dates. Format should be YYYY-MM-DDThh:mm:ssZ. | [optional] 

### Return type

[**List[Position]**](Position.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of positions |  -  |
**400** | Request/response validation failed |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

