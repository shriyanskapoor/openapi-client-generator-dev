# main_openapi_client.TransactionsApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_rollup_status**](TransactionsApi.md#get_transaction_rollup_status) | **GET** /transaction-rollups/{sync_id} | Retrieve a single transaction rollup status by batch ID
[**get_transaction_rollup_statuses**](TransactionsApi.md#get_transaction_rollup_statuses) | **GET** /transaction-rollups | Retrieves the status of transaction rollups by batch IDs


# **get_transaction_rollup_status**
> TransactionRollupStatus get_transaction_rollup_status(sync_id)

Retrieve a single transaction rollup status by batch ID

Returns the transaction rollup status for a specified batch ID.

### Example


```python
import main_openapi_client
from main_openapi_client.models.transaction_rollup_status import TransactionRollupStatus
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
    api_instance = main_openapi_client.TransactionsApi(api_client)
    sync_id = 'sync_id_example' # str | The synchronization ID to fetch the transaction rollup status for.

    try:
        # Retrieve a single transaction rollup status by batch ID
        api_response = api_instance.get_transaction_rollup_status(sync_id)
        print("The response of TransactionsApi->get_transaction_rollup_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction_rollup_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_id** | **str**| The synchronization ID to fetch the transaction rollup status for. | 

### Return type

[**TransactionRollupStatus**](TransactionRollupStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction rollup status found |  -  |
**400** | Invalid UUID format |  -  |
**404** | Transaction rollup status not found for the specified ID |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_rollup_statuses**
> List[TransactionRollupStatus] get_transaction_rollup_statuses(sync_ids)

Retrieves the status of transaction rollups by batch IDs

Returns a list of transaction rollup statuses based on the provided batch IDs.

### Example


```python
import main_openapi_client
from main_openapi_client.models.transaction_rollup_status import TransactionRollupStatus
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
    api_instance = main_openapi_client.TransactionsApi(api_client)
    sync_ids = ['sync_ids_example'] # List[str] | A list of synchronization IDs (UUIDs) to fetch the transaction rollups statuses.

    try:
        # Retrieves the status of transaction rollups by batch IDs
        api_response = api_instance.get_transaction_rollup_statuses(sync_ids)
        print("The response of TransactionsApi->get_transaction_rollup_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction_rollup_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_ids** | [**List[str]**](str.md)| A list of synchronization IDs (UUIDs) to fetch the transaction rollups statuses. | 

### Return type

[**List[TransactionRollupStatus]**](TransactionRollupStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transaction rollup statuses |  -  |
**400** | Invalid input |  -  |
**404** | No matching records found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

