# main_openapi_client.BankAccountApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bank_account**](BankAccountApi.md#get_bank_account) | **GET** /bank_account/{id} | Get a bank account (BankAccountModel)


# **get_bank_account**
> BankAccount get_bank_account(id)

Get a bank account (BankAccountModel)

Get the name of the provided bank_account_id

### Example


```python
import main_openapi_client
from main_openapi_client.models.bank_account import BankAccount
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
    api_instance = main_openapi_client.BankAccountApi(api_client)
    id = 56 # int | Id of the resource

    try:
        # Get a bank account (BankAccountModel)
        api_response = api_instance.get_bank_account(id)
        print("The response of BankAccountApi->get_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountApi->get_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the resource | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A bank account object (BankAccountModel) |  -  |
**400** | Request/response validation failed |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

