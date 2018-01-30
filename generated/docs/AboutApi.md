# swagger_client.AboutApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_about**](AboutApi.md#get_about) | **GET** /about | Get some info about the server


# **get_about**
> AboutInfo get_about()

Get some info about the server



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AboutApi()

try:
    # Get some info about the server
    api_response = api_instance.get_about()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->get_about: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AboutInfo**](AboutInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

