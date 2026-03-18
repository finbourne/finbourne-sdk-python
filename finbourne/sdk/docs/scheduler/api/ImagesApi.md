# scheduler.ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image**](ImagesApi.md#get_image) | **GET** /scheduler2/api/images/{name} | GetImage: Get metadata of a Docker Image
[**list_images**](ImagesApi.md#list_images) | **GET** /scheduler2/api/images/repository/{name} | ListImages: List all images under same image repository
[**list_repositories**](ImagesApi.md#list_repositories) | **GET** /scheduler2/api/images/repository | ListRepositories: List all Docker image repositories
[**upload_image**](ImagesApi.md#upload_image) | **POST** /scheduler2/api/images | UploadImage: Upload a Docker Image used for Scheduler jobs


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.scheduler.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.scheduler.api.images_api import ImagesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ImagesApi)
```

---

# **get_image**
> Image getImage = get_image(name)

GetImage: Get metadata of a Docker Image

### Example

```python
api_instance = api_client_factory.build(ImagesApi)
name = 'name_example' # str
api_response = api_instance.get_image(name)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name and tag of a Docker image. Format \&quot;ExampleImageName:latest\&quot; | [required] 

### Return type

[**Image**](Image.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_images**
> ResourceListOfImageSummary listImages = list_images(name, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

ListImages: List all images under same image repository

### Example

```python
api_instance = api_client_factory.build(ImagesApi)
name = 'name_example' # str
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
start = 56 # int (optional)
limit = 2000 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_images(name, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Repository | [required] 
 **page** | **str**| The pagination token to use to continue listing images from a previous call to list images.             This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields             must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. | [optional] [default to 2000]
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ResourceListOfImageSummary**](ResourceListOfImageSummary.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_repositories**
> ResourceListOfRepository listRepositories = list_repositories(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

ListRepositories: List all Docker image repositories

### Example

```python
api_instance = api_client_factory.build(ImagesApi)
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
start = 56 # int (optional)
limit = 2000 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_repositories(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing images from a previous call to list images.             This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields             must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. | [optional] [default to 2000]
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ResourceListOfRepository**](ResourceListOfRepository.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upload_image**
> UploadImageInstructions uploadImage = upload_image(upload_image_request)

UploadImage: Upload a Docker Image used for Scheduler jobs

Every image must have at least one tag. Note: your image will not be available until the returned Docker commands are executed.

### Example

```python
api_instance = api_client_factory.build(ImagesApi)
upload_image_request = UploadImageRequest()
api_response = api_instance.upload_image(upload_image_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_image_request** | [**UploadImageRequest**](UploadImageRequest.md)| Request to upload image | [required] 

### Return type

[**UploadImageInstructions**](UploadImageInstructions.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

