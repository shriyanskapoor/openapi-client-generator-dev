# main_openapi_client.PaymentPrefsApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate_payment_pref_with_positions**](PaymentPrefsApi.md#associate_payment_pref_with_positions) | **PATCH** /users/{user_id}/associate_payment_pref/positions | Associate payment pref with positions
[**associate_payment_pref_with_positions_of_accounts**](PaymentPrefsApi.md#associate_payment_pref_with_positions_of_accounts) | **PATCH** /users/{user_id}/associate_payment_pref/accounts | Associate payment pref with positions of account
[**associate_payment_pref_with_positions_of_source_payment_pref**](PaymentPrefsApi.md#associate_payment_pref_with_positions_of_source_payment_pref) | **PATCH** /users/{user_id}/associate_payment_pref/source_payment_pref | Associate payment pref with positions of source payment pref
[**associate_payment_pref_with_positions_without_payment_pref**](PaymentPrefsApi.md#associate_payment_pref_with_positions_without_payment_pref) | **PATCH** /users/{user_id}/associate_payment_pref/no_payment_pref | Associate payment pref with positions with no payment pref
[**get_payment_prefs**](PaymentPrefsApi.md#get_payment_prefs) | **GET** /payment_prefs | Get a list of payment prefs
[**update_payment_pref**](PaymentPrefsApi.md#update_payment_pref) | **PATCH** /payment_prefs/{id} | Update payment pref


# **associate_payment_pref_with_positions**
> UpdatePositionsPaymentPrefSuccessResponse associate_payment_pref_with_positions(user_id, target_payment_pref_id, position_ids, arena_id, should_update_account_mailing_address=should_update_account_mailing_address)

Associate payment pref with positions

Changes the payment pref tied to a position to the specified payment pref.

### Example


```python
import main_openapi_client
from main_openapi_client.models.update_positions_payment_pref_success_response import UpdatePositionsPaymentPrefSuccessResponse
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
    api_instance = main_openapi_client.PaymentPrefsApi(api_client)
    user_id = 56 # int | User ID of the resource
    target_payment_pref_id = 56 # int | Target Payment Pref ID.
    position_ids = [56] # List[int] | List of position ids.
    arena_id = 56 # int | Required arena_id to filter by.
    should_update_account_mailing_address = True # bool | If the Account mailing address should be updated. (optional)

    try:
        # Associate payment pref with positions
        api_response = api_instance.associate_payment_pref_with_positions(user_id, target_payment_pref_id, position_ids, arena_id, should_update_account_mailing_address=should_update_account_mailing_address)
        print("The response of PaymentPrefsApi->associate_payment_pref_with_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentPrefsApi->associate_payment_pref_with_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the resource | 
 **target_payment_pref_id** | **int**| Target Payment Pref ID. | 
 **position_ids** | [**List[int]**](int.md)| List of position ids. | 
 **arena_id** | **int**| Required arena_id to filter by. | 
 **should_update_account_mailing_address** | **bool**| If the Account mailing address should be updated. | [optional] 

### Return type

[**UpdatePositionsPaymentPrefSuccessResponse**](UpdatePositionsPaymentPrefSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of position ids |  -  |
**400** | Request/response validation failed |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **associate_payment_pref_with_positions_of_accounts**
> UpdatePositionsPaymentPrefSuccessResponse associate_payment_pref_with_positions_of_accounts(user_id, target_payment_pref_id, account_ids, check_same_mailing_address=check_same_mailing_address, should_update_account_mailing_address=should_update_account_mailing_address, bypass_check_for_accepted_payment_methods=bypass_check_for_accepted_payment_methods)

Associate payment pref with positions of account

Searches for all positions within an account and alters their payment prefs to the specified payment pref.

### Example


```python
import main_openapi_client
from main_openapi_client.models.update_positions_payment_pref_success_response import UpdatePositionsPaymentPrefSuccessResponse
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
    api_instance = main_openapi_client.PaymentPrefsApi(api_client)
    user_id = 56 # int | User ID of the resource
    target_payment_pref_id = 56 # int | Target Payment Pref ID.
    account_ids = [56] # List[int] | List of account ids.
    check_same_mailing_address = True # bool | Specifies if check address is the same as mailing address. (optional)
    should_update_account_mailing_address = True # bool | If the Account mailing address should be updated. (optional)
    bypass_check_for_accepted_payment_methods = True # bool | If the checks for accepted payment methods should be bypassed. (optional)

    try:
        # Associate payment pref with positions of account
        api_response = api_instance.associate_payment_pref_with_positions_of_accounts(user_id, target_payment_pref_id, account_ids, check_same_mailing_address=check_same_mailing_address, should_update_account_mailing_address=should_update_account_mailing_address, bypass_check_for_accepted_payment_methods=bypass_check_for_accepted_payment_methods)
        print("The response of PaymentPrefsApi->associate_payment_pref_with_positions_of_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentPrefsApi->associate_payment_pref_with_positions_of_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the resource | 
 **target_payment_pref_id** | **int**| Target Payment Pref ID. | 
 **account_ids** | [**List[int]**](int.md)| List of account ids. | 
 **check_same_mailing_address** | **bool**| Specifies if check address is the same as mailing address. | [optional] 
 **should_update_account_mailing_address** | **bool**| If the Account mailing address should be updated. | [optional] 
 **bypass_check_for_accepted_payment_methods** | **bool**| If the checks for accepted payment methods should be bypassed. | [optional] 

### Return type

[**UpdatePositionsPaymentPrefSuccessResponse**](UpdatePositionsPaymentPrefSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of position ids |  -  |
**400** | Request/response validation failed |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **associate_payment_pref_with_positions_of_source_payment_pref**
> UpdatePositionsPaymentPrefSuccessResponse associate_payment_pref_with_positions_of_source_payment_pref(user_id, target_payment_pref_id, account_id, source_payment_pref_id, should_update_account_mailing_address=should_update_account_mailing_address)

Associate payment pref with positions of source payment pref

Searches for all positions within an account that has a source payment pref and alters their payment prefs to the specified payment pref.

### Example


```python
import main_openapi_client
from main_openapi_client.models.update_positions_payment_pref_success_response import UpdatePositionsPaymentPrefSuccessResponse
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
    api_instance = main_openapi_client.PaymentPrefsApi(api_client)
    user_id = 56 # int | User ID of the resource
    target_payment_pref_id = 56 # int | Target Payment Pref ID.
    account_id = 56 # int | Account id.
    source_payment_pref_id = 56 # int | Source Payment Pref ID.
    should_update_account_mailing_address = True # bool | If the Account mailing address should be updated. (optional)

    try:
        # Associate payment pref with positions of source payment pref
        api_response = api_instance.associate_payment_pref_with_positions_of_source_payment_pref(user_id, target_payment_pref_id, account_id, source_payment_pref_id, should_update_account_mailing_address=should_update_account_mailing_address)
        print("The response of PaymentPrefsApi->associate_payment_pref_with_positions_of_source_payment_pref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentPrefsApi->associate_payment_pref_with_positions_of_source_payment_pref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the resource | 
 **target_payment_pref_id** | **int**| Target Payment Pref ID. | 
 **account_id** | **int**| Account id. | 
 **source_payment_pref_id** | **int**| Source Payment Pref ID. | 
 **should_update_account_mailing_address** | **bool**| If the Account mailing address should be updated. | [optional] 

### Return type

[**UpdatePositionsPaymentPrefSuccessResponse**](UpdatePositionsPaymentPrefSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of position ids |  -  |
**400** | Request/response validation failed |  -  |
**401** | The request was unauthorized |  -  |
**403** | The operation was forbidden |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **associate_payment_pref_with_positions_without_payment_pref**
> UpdatePositionsPaymentPrefSuccessResponse associate_payment_pref_with_positions_without_payment_pref(user_id, target_payment_pref_id, account_id, arena_id, should_update_account_mailing_address=should_update_account_mailing_address)

Associate payment pref with positions with no payment pref

Changes the payment pref tied to a position to the specified payment pref. Position must be under the specified account and have no payment pref already assigned to it

### Example


```python
import main_openapi_client
from main_openapi_client.models.update_positions_payment_pref_success_response import UpdatePositionsPaymentPrefSuccessResponse
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
    api_instance = main_openapi_client.PaymentPrefsApi(api_client)
    user_id = 56 # int | User ID of the resource
    target_payment_pref_id = 56 # int | Target Payment Pref ID.
    account_id = 56 # int | Account id.
    arena_id = 56 # int | Required arena_id to filter by.
    should_update_account_mailing_address = True # bool | If the Account mailing address should be updated. (optional)

    try:
        # Associate payment pref with positions with no payment pref
        api_response = api_instance.associate_payment_pref_with_positions_without_payment_pref(user_id, target_payment_pref_id, account_id, arena_id, should_update_account_mailing_address=should_update_account_mailing_address)
        print("The response of PaymentPrefsApi->associate_payment_pref_with_positions_without_payment_pref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentPrefsApi->associate_payment_pref_with_positions_without_payment_pref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the resource | 
 **target_payment_pref_id** | **int**| Target Payment Pref ID. | 
 **account_id** | **int**| Account id. | 
 **arena_id** | **int**| Required arena_id to filter by. | 
 **should_update_account_mailing_address** | **bool**| If the Account mailing address should be updated. | [optional] 

### Return type

[**UpdatePositionsPaymentPrefSuccessResponse**](UpdatePositionsPaymentPrefSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of position ids |  -  |
**400** | Request/response validation failed |  -  |
**401** | The request was unauthorized |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_prefs**
> List[PaymentPref] get_payment_prefs(ids)

Get a list of payment prefs

Get an un-paginated list of payment prefs filtered by a required list of payment pref IDs.

### Example


```python
import main_openapi_client
from main_openapi_client.models.payment_pref import PaymentPref
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
    api_instance = main_openapi_client.PaymentPrefsApi(api_client)
    ids = [56] # List[int] | Required comma separated list of ids to filter resources by.

    try:
        # Get a list of payment prefs
        api_response = api_instance.get_payment_prefs(ids)
        print("The response of PaymentPrefsApi->get_payment_prefs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentPrefsApi->get_payment_prefs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| Required comma separated list of ids to filter resources by. | 

### Return type

[**List[PaymentPref]**](PaymentPref.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of payment prefs |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_pref**
> PaymentPref update_payment_pref(id, update_payment_pref_options=update_payment_pref_options)

Update payment pref

Update (patch) the fields for a specific payment pref. This only supports verification status at the moment.

### Example


```python
import main_openapi_client
from main_openapi_client.models.payment_pref import PaymentPref
from main_openapi_client.models.update_payment_pref_options import UpdatePaymentPrefOptions
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
    api_instance = main_openapi_client.PaymentPrefsApi(api_client)
    id = 56 # int | Id of the resource
    update_payment_pref_options = main_openapi_client.UpdatePaymentPrefOptions() # UpdatePaymentPrefOptions | Fields used to update a payment pref (optional)

    try:
        # Update payment pref
        api_response = api_instance.update_payment_pref(id, update_payment_pref_options=update_payment_pref_options)
        print("The response of PaymentPrefsApi->update_payment_pref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentPrefsApi->update_payment_pref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the resource | 
 **update_payment_pref_options** | [**UpdatePaymentPrefOptions**](UpdatePaymentPrefOptions.md)| Fields used to update a payment pref | [optional] 

### Return type

[**PaymentPref**](PaymentPref.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A payment pref |  -  |
**400** | Request/response validation failed |  -  |
**404** | An expected resource was not found |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

