# main_openapi_client.AccountsApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_contact_add**](AccountsApi.md#account_contact_add) | **PATCH** /account-contact/add | API for account contact to add new or existing contact to account
[**account_contact_bulk_remove**](AccountsApi.md#account_contact_bulk_remove) | **DELETE** /account-contact/bulk-remove | API for account contact bulk removal
[**account_contact_bulk_update**](AccountsApi.md#account_contact_bulk_update) | **PATCH** /account-contact/bulk-update | API for account contact bulk update
[**account_contact_change_notify**](AccountsApi.md#account_contact_change_notify) | **POST** /users/{user_id}/account-contact/bulk-notify | API for account contact change notification
[**account_contact_change_notify_by_status**](AccountsApi.md#account_contact_change_notify_by_status) | **POST** /users/{user_id}/account-contact/bulk-notify-by-status | API for account contact change notification by status


# **account_contact_add**
> AccountContactAddSuccessResponse account_contact_add(account_contact_add_request_body=account_contact_add_request_body)

API for account contact to add new or existing contact to account

API for account contact to add new or existing contact to account

### Example


```python
import main_openapi_client
from main_openapi_client.models.account_contact_add_request_body import AccountContactAddRequestBody
from main_openapi_client.models.account_contact_add_success_response import AccountContactAddSuccessResponse
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
    api_instance = main_openapi_client.AccountsApi(api_client)
    account_contact_add_request_body = main_openapi_client.AccountContactAddRequestBody() # AccountContactAddRequestBody |  (optional)

    try:
        # API for account contact to add new or existing contact to account
        api_response = api_instance.account_contact_add(account_contact_add_request_body=account_contact_add_request_body)
        print("The response of AccountsApi->account_contact_add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->account_contact_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_contact_add_request_body** | [**AccountContactAddRequestBody**](AccountContactAddRequestBody.md)|  | [optional] 

### Return type

[**AccountContactAddSuccessResponse**](AccountContactAddSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account Contact Add Success |  -  |
**400** | Request/response validation failed |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_contact_bulk_remove**
> List[AccountContactBulkSuccessResponse] account_contact_bulk_remove(bulk_account_contact_remove_request_body=bulk_account_contact_remove_request_body)

API for account contact bulk removal

API for account contact bulk removal

### Example


```python
import main_openapi_client
from main_openapi_client.models.account_contact_bulk_success_response import AccountContactBulkSuccessResponse
from main_openapi_client.models.bulk_account_contact_remove_request_body import BulkAccountContactRemoveRequestBody
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
    api_instance = main_openapi_client.AccountsApi(api_client)
    bulk_account_contact_remove_request_body = main_openapi_client.BulkAccountContactRemoveRequestBody() # BulkAccountContactRemoveRequestBody |  (optional)

    try:
        # API for account contact bulk removal
        api_response = api_instance.account_contact_bulk_remove(bulk_account_contact_remove_request_body=bulk_account_contact_remove_request_body)
        print("The response of AccountsApi->account_contact_bulk_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->account_contact_bulk_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_account_contact_remove_request_body** | [**BulkAccountContactRemoveRequestBody**](BulkAccountContactRemoveRequestBody.md)|  | [optional] 

### Return type

[**List[AccountContactBulkSuccessResponse]**](AccountContactBulkSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account Contact Bulk Success Response Array |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_contact_bulk_update**
> List[AccountContactBulkSuccessResponse] account_contact_bulk_update(bulk_account_contact_update_request_body=bulk_account_contact_update_request_body)

API for account contact bulk update

API for account contact bulk update

### Example


```python
import main_openapi_client
from main_openapi_client.models.account_contact_bulk_success_response import AccountContactBulkSuccessResponse
from main_openapi_client.models.bulk_account_contact_update_request_body import BulkAccountContactUpdateRequestBody
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
    api_instance = main_openapi_client.AccountsApi(api_client)
    bulk_account_contact_update_request_body = main_openapi_client.BulkAccountContactUpdateRequestBody() # BulkAccountContactUpdateRequestBody |  (optional)

    try:
        # API for account contact bulk update
        api_response = api_instance.account_contact_bulk_update(bulk_account_contact_update_request_body=bulk_account_contact_update_request_body)
        print("The response of AccountsApi->account_contact_bulk_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->account_contact_bulk_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_account_contact_update_request_body** | [**BulkAccountContactUpdateRequestBody**](BulkAccountContactUpdateRequestBody.md)|  | [optional] 

### Return type

[**List[AccountContactBulkSuccessResponse]**](AccountContactBulkSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account Contact Bulk Success Response Array |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_contact_change_notify**
> account_contact_change_notify(user_id, bulk_account_contact_change_notify=bulk_account_contact_change_notify)

API for account contact change notification

API for account contact change notification

### Example


```python
import main_openapi_client
from main_openapi_client.models.bulk_account_contact_change_notify import BulkAccountContactChangeNotify
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
    api_instance = main_openapi_client.AccountsApi(api_client)
    user_id = 56 # int | User ID of the resource
    bulk_account_contact_change_notify = main_openapi_client.BulkAccountContactChangeNotify() # BulkAccountContactChangeNotify |  (optional)

    try:
        # API for account contact change notification
        api_instance.account_contact_change_notify(user_id, bulk_account_contact_change_notify=bulk_account_contact_change_notify)
    except Exception as e:
        print("Exception when calling AccountsApi->account_contact_change_notify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the resource | 
 **bulk_account_contact_change_notify** | [**BulkAccountContactChangeNotify**](BulkAccountContactChangeNotify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Bulk updates were successfully completed. |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_contact_change_notify_by_status**
> account_contact_change_notify_by_status(user_id, bulk_account_contact_change_notify_by_status=bulk_account_contact_change_notify_by_status)

API for account contact change notification by status

API for account contact change notification by status

### Example


```python
import main_openapi_client
from main_openapi_client.models.bulk_account_contact_change_notify_by_status import BulkAccountContactChangeNotifyByStatus
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
    api_instance = main_openapi_client.AccountsApi(api_client)
    user_id = 56 # int | User ID of the resource
    bulk_account_contact_change_notify_by_status = main_openapi_client.BulkAccountContactChangeNotifyByStatus() # BulkAccountContactChangeNotifyByStatus |  (optional)

    try:
        # API for account contact change notification by status
        api_instance.account_contact_change_notify_by_status(user_id, bulk_account_contact_change_notify_by_status=bulk_account_contact_change_notify_by_status)
    except Exception as e:
        print("Exception when calling AccountsApi->account_contact_change_notify_by_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the resource | 
 **bulk_account_contact_change_notify_by_status** | [**BulkAccountContactChangeNotifyByStatus**](BulkAccountContactChangeNotifyByStatus.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Bulk updates were successfully completed. |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

