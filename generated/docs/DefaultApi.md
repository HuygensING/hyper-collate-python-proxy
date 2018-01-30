# swagger_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fav_icon**](DefaultApi.md#get_fav_icon) | **GET** /favicon.ico | Placeholder for favicon.ico
[**get_home_page**](DefaultApi.md#get_home_page) | **GET** / | Show the server homepage
[**no_robots**](DefaultApi.md#no_robots) | **GET** /robots.txt | Placeholder for robots.txt


# **get_fav_icon**
> get_fav_icon()

Placeholder for favicon.ico



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Placeholder for favicon.ico
    api_instance.get_fav_icon()
except ApiException as e:
    print("Exception when calling DefaultApi->get_fav_icon: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_home_page**
> get_home_page()

Show the server homepage



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Show the server homepage
    api_instance.get_home_page()
except ApiException as e:
    print("Exception when calling DefaultApi->get_home_page: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **no_robots**
> str no_robots()

Placeholder for robots.txt



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Placeholder for robots.txt
    api_response = api_instance.no_robots()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->no_robots: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

