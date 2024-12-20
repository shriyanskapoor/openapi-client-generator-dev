# main_openapi_client.DistributionApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_distribution**](DistributionApi.md#get_distribution) | **GET** /distributions/{id} | Get distribution


# **get_distribution**
> Distribution get_distribution(id)

Get distribution

Get a distribution by the given distribution id. This does not handle auth.

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
    api_instance = main_openapi_client.DistributionApi(api_client)
    id = 56 # int | Id of the resource

    try:
        # Get distribution
        api_response = api_instance.get_distribution(id)
        print("The response of DistributionApi->get_distribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionApi->get_distribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the resource | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A distribution |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

