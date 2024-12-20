# main_openapi_client.DiligencesApi

All URIs are relative to */internal/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_diligences**](DiligencesApi.md#create_diligences) | **POST** /diligences | Create a diligence object and underlying KYC/watchlists
[**get_diligences**](DiligencesApi.md#get_diligences) | **GET** /diligences | Get a list of diligences


# **create_diligences**
> Diligence create_diligences(create_diligence=create_diligence)

Create a diligence object and underlying KYC/watchlists

Create a diligence and underlying KYC/watchlists. This method is considered deprecated and used to bridge the gap until the compliance service API is fully available.

### Example


```python
import main_openapi_client
from main_openapi_client.models.create_diligence import CreateDiligence
from main_openapi_client.models.diligence import Diligence
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
    api_instance = main_openapi_client.DiligencesApi(api_client)
    create_diligence = main_openapi_client.CreateDiligence() # CreateDiligence |  (optional)

    try:
        # Create a diligence object and underlying KYC/watchlists
        api_response = api_instance.create_diligences(create_diligence=create_diligence)
        print("The response of DiligencesApi->create_diligences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiligencesApi->create_diligences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_diligence** | [**CreateDiligence**](CreateDiligence.md)|  | [optional] 

### Return type

[**Diligence**](Diligence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A diligence object |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diligences**
> List[Diligence] get_diligences(diligence_category, object_type=object_type, object_id=object_id, object_ids=object_ids, diligence_type=diligence_type, diligence_status=diligence_status)

Get a list of diligences

Get an un-paginated list of diligences

### Example


```python
import main_openapi_client
from main_openapi_client.models.diligence import Diligence
from main_openapi_client.models.diligence_category import DiligenceCategory
from main_openapi_client.models.diligence_status import DiligenceStatus
from main_openapi_client.models.diligence_type import DiligenceType
from main_openapi_client.models.object_type import ObjectType
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
    api_instance = main_openapi_client.DiligencesApi(api_client)
    diligence_category = main_openapi_client.DiligenceCategory() # DiligenceCategory | Category of diligences to filter on
    object_type = main_openapi_client.ObjectType() # ObjectType | Optional object_type to filter by. Should match an ObjectType enum. (optional)
    object_id = 56 # int | Object ID to filter on (optional)
    object_ids = [56] # List[int] | Object IDs to filter on (optional)
    diligence_type = main_openapi_client.DiligenceType() # DiligenceType | Type of Diligence to filter on (optional)
    diligence_status = main_openapi_client.DiligenceStatus() # DiligenceStatus | Status of diligence in submission workflow. (optional)

    try:
        # Get a list of diligences
        api_response = api_instance.get_diligences(diligence_category, object_type=object_type, object_id=object_id, object_ids=object_ids, diligence_type=diligence_type, diligence_status=diligence_status)
        print("The response of DiligencesApi->get_diligences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiligencesApi->get_diligences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diligence_category** | [**DiligenceCategory**](.md)| Category of diligences to filter on | 
 **object_type** | [**ObjectType**](.md)| Optional object_type to filter by. Should match an ObjectType enum. | [optional] 
 **object_id** | **int**| Object ID to filter on | [optional] 
 **object_ids** | [**List[int]**](int.md)| Object IDs to filter on | [optional] 
 **diligence_type** | [**DiligenceType**](.md)| Type of Diligence to filter on | [optional] 
 **diligence_status** | [**DiligenceStatus**](.md)| Status of diligence in submission workflow. | [optional] 

### Return type

[**List[Diligence]**](Diligence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Diligences |  -  |
**400** | Request/response validation failed |  -  |
**500** | An unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

