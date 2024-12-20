# main_openapi_client.DistributionBatchesApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_distribution_batch**](DistributionBatchesApi.md#get_distribution_batch) | **GET** /distribution_batches/{id}/ | Get distribution batch no authorization checks
[**get_distributions_for_distribution_batch**](DistributionBatchesApi.md#get_distributions_for_distribution_batch) | **GET** /distribution_batches/{id}/distributions | Get distributions for a distribution batch not authorization checks
[**get_unique_position_ids_for_distribution_batches**](DistributionBatchesApi.md#get_unique_position_ids_for_distribution_batches) | **POST** /distribution_batches/unique_position_ids | Get unique positions ids for distribution batches


# **get_distribution_batch**
> DistributionBatch get_distribution_batch(id)

Get distribution batch no authorization checks

Get a distribution batch by ID. This does not handle auth checks.

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
    api_instance = main_openapi_client.DistributionBatchesApi(api_client)
    id = 56 # int | Id of the resource

    try:
        # Get distribution batch no authorization checks
        api_response = api_instance.get_distribution_batch(id)
        print("The response of DistributionBatchesApi->get_distribution_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionBatchesApi->get_distribution_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the resource | 

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

# **get_distributions_for_distribution_batch**
> List[Distribution] get_distributions_for_distribution_batch(id)

Get distributions for a distribution batch not authorization checks

Get distributions for a distribution batch by distribution batch ID. This does not handle auth.

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
    api_instance = main_openapi_client.DistributionBatchesApi(api_client)
    id = 56 # int | Id of the resource

    try:
        # Get distributions for a distribution batch not authorization checks
        api_response = api_instance.get_distributions_for_distribution_batch(id)
        print("The response of DistributionBatchesApi->get_distributions_for_distribution_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionBatchesApi->get_distributions_for_distribution_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the resource | 

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

# **get_unique_position_ids_for_distribution_batches**
> DistributionBatchUniquePositionIds get_unique_position_ids_for_distribution_batches(distribution_batch_unique_position_ids_request_body)

Get unique positions ids for distribution batches

Retrieve the unique positions ids for the specified distribution batch IDs. No authorization checks are applied.

### Example


```python
import main_openapi_client
from main_openapi_client.models.distribution_batch_unique_position_ids import DistributionBatchUniquePositionIds
from main_openapi_client.models.distribution_batch_unique_position_ids_request_body import DistributionBatchUniquePositionIdsRequestBody
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
    api_instance = main_openapi_client.DistributionBatchesApi(api_client)
    distribution_batch_unique_position_ids_request_body = main_openapi_client.DistributionBatchUniquePositionIdsRequestBody() # DistributionBatchUniquePositionIdsRequestBody | A JSON list of unique position IDs

    try:
        # Get unique positions ids for distribution batches
        api_response = api_instance.get_unique_position_ids_for_distribution_batches(distribution_batch_unique_position_ids_request_body)
        print("The response of DistributionBatchesApi->get_unique_position_ids_for_distribution_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionBatchesApi->get_unique_position_ids_for_distribution_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_batch_unique_position_ids_request_body** | [**DistributionBatchUniquePositionIdsRequestBody**](DistributionBatchUniquePositionIdsRequestBody.md)| A JSON list of unique position IDs | 

### Return type

[**DistributionBatchUniquePositionIds**](DistributionBatchUniquePositionIds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of unique positions for distribution batch IDs. |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

