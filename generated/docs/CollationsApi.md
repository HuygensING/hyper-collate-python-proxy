# swagger_client.CollationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_collation**](CollationsApi.md#add_collation) | **PUT** /collations/{name} | Create a new collation with the given name
[**add_xml_witness**](CollationsApi.md#add_xml_witness) | **PUT** /collations/{name}/witnesses/{sigil} | Add a witness to the collation
[**get_ascii_table_visualization**](CollationsApi.md#get_ascii_table_visualization) | **GET** /collations/{name}/ascii_table | Get an ASCII table visualization of the collation graph
[**get_collation_info**](CollationsApi.md#get_collation_info) | **GET** /collations/{name} | Get information about the collation
[**get_collation_names**](CollationsApi.md#get_collation_names) | **GET** /collations | List all collation names
[**get_dot_visualization**](CollationsApi.md#get_dot_visualization) | **GET** /collations/{name}/dot | Get a .dot visualization of the collation graph
[**get_witness_xml**](CollationsApi.md#get_witness_xml) | **GET** /collations/{name}/witnesses/{sigil} | Return the XML source of the witness


# **add_collation**
> add_collation(name)

Create a new collation with the given name



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollationsApi()
name = 'name_example' # str | Collation name

try:
    # Create a new collation with the given name
    api_instance.add_collation(name)
except ApiException as e:
    print("Exception when calling CollationsApi->add_collation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Collation name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_xml_witness**
> add_xml_witness(name, sigil, body=body)

Add a witness to the collation



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollationsApi()
name = 'name_example' # str | Collation name
sigil = 'sigil_example' # str | Witness sigil
body = 'body_example' # str | Witness Source (XML) (optional)

try:
    # Add a witness to the collation
    api_instance.add_xml_witness(name, sigil, body=body)
except ApiException as e:
    print("Exception when calling CollationsApi->add_xml_witness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Collation name | 
 **sigil** | **str**| Witness sigil | 
 **body** | **str**| Witness Source (XML) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/xml; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ascii_table_visualization**
> get_ascii_table_visualization(name)

Get an ASCII table visualization of the collation graph



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollationsApi()
name = 'name_example' # str | Collation name

try:
    # Get an ASCII table visualization of the collation graph
    api_instance.get_ascii_table_visualization(name)
except ApiException as e:
    print("Exception when calling CollationsApi->get_ascii_table_visualization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Collation name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collation_info**
> get_collation_info(name)

Get information about the collation



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollationsApi()
name = 'name_example' # str | Collation name

try:
    # Get information about the collation
    api_instance.get_collation_info(name)
except ApiException as e:
    print("Exception when calling CollationsApi->get_collation_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Collation name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collation_names**
> list[str] get_collation_names()

List all collation names



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollationsApi()

try:
    # List all collation names
    api_response = api_instance.get_collation_names()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollationsApi->get_collation_names: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dot_visualization**
> get_dot_visualization(name)

Get a .dot visualization of the collation graph



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollationsApi()
name = 'name_example' # str | Collation name

try:
    # Get a .dot visualization of the collation graph
    api_instance.get_dot_visualization(name)
except ApiException as e:
    print("Exception when calling CollationsApi->get_dot_visualization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Collation name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_witness_xml**
> get_witness_xml(name, sigil)

Return the XML source of the witness



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollationsApi()
name = 'name_example' # str | Collation name
sigil = 'sigil_example' # str | Witness sigil

try:
    # Return the XML source of the witness
    api_instance.get_witness_xml(name, sigil)
except ApiException as e:
    print("Exception when calling CollationsApi->get_witness_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Collation name | 
 **sigil** | **str**| Witness sigil | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

