# drive.FilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesApi.md#create_file) | **POST** /drive/api/files | CreateFile: Uploads a file to Lusid Drive. If using an SDK, consider using the UploadAsStreamAsync function for larger files instead.
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /drive/api/files/{id} | [EARLY ACCESS] DeleteFile: Deletes a file from Drive.
[**download_file**](FilesApi.md#download_file) | **GET** /drive/api/files/{id}/contents | DownloadFile: Download the file from Drive.
[**get_file**](FilesApi.md#get_file) | **GET** /drive/api/files/{id} | [EARLY ACCESS] GetFile: Get a file stored in Drive.
[**update_file_contents**](FilesApi.md#update_file_contents) | **PUT** /drive/api/files/{id}/contents | [EARLY ACCESS] UpdateFileContents: Updates contents of a file in Drive.
[**update_file_metadata**](FilesApi.md#update_file_metadata) | **PUT** /drive/api/files/{id} | [EARLY ACCESS] UpdateFileMetadata: Updates metadata for a file in Drive.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.drive.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.drive.api.files_api import FilesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(FilesApi)
```

---

# **create_file**
> StorageObject createFile = create_file(x_lusid_drive_filename, x_lusid_drive_path, content_length, body)

CreateFile: Uploads a file to Lusid Drive. If using an SDK, consider using the UploadAsStreamAsync function for larger files instead.

### Example

```python
api_instance = api_client_factory.build(FilesApi)
x_lusid_drive_filename = 'x_lusid_drive_filename_example' # str
x_lusid_drive_path = 'x_lusid_drive_path_example' # str
content_length = 56 # int
body = None # bytes
api_response = api_instance.create_file(x_lusid_drive_filename, x_lusid_drive_path, content_length, body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_lusid_drive_filename** | **str**| File name. | [required] 
 **x_lusid_drive_path** | **str**| File path. | [required] 
 **content_length** | **int**| The size in bytes of the file to be uploaded | [required] 
 **body** | **bytes**|  | [required] 

### Return type

[**StorageObject**](StorageObject.md)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_file**
> deleteFile = delete_file(id)

[EARLY ACCESS] DeleteFile: Deletes a file from Drive.

### Example

```python
api_instance = api_client_factory.build(FilesApi)
id = 'id_example' # str
api_instance.delete_file(id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be deleted. | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **download_file**
> bytes downloadFile = download_file(id)

DownloadFile: Download the file from Drive.

### Example

```python
api_instance = api_client_factory.build(FilesApi)
id = 'id_example' # str
api_response = api_instance.download_file(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be downloaded. | [required] 

### Return type

**bytes**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | Malware detected, restricted from downloading file. |  -  |
**423** | Virus scan in progress, restricted from downloading file. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_file**
> StorageObject getFile = get_file(id)

[EARLY ACCESS] GetFile: Get a file stored in Drive.

### Example

```python
api_instance = api_client_factory.build(FilesApi)
id = 'id_example' # str
api_response = api_instance.get_file(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be retrieved. | [required] 

### Return type

[**StorageObject**](StorageObject.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_file_contents**
> StorageObject updateFileContents = update_file_contents(id, content_length, body)

[EARLY ACCESS] UpdateFileContents: Updates contents of a file in Drive.

### Example

```python
api_instance = api_client_factory.build(FilesApi)
id = 'id_example' # str
content_length = 56 # int
body = None # bytes
api_response = api_instance.update_file_contents(id, content_length, body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique file identifier | [required] 
 **content_length** | **int**| The size in bytes of the file to be uploaded | [required] 
 **body** | **bytes**|  | [required] 

### Return type

[**StorageObject**](StorageObject.md)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_file_metadata**
> StorageObject updateFileMetadata = update_file_metadata(id, update_file)

[EARLY ACCESS] UpdateFileMetadata: Updates metadata for a file in Drive.

### Example

```python
api_instance = api_client_factory.build(FilesApi)
id = 'id_example' # str
update_file = UpdateFile()
api_response = api_instance.update_file_metadata(id, update_file)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be updated | [required] 
 **update_file** | [**UpdateFile**](UpdateFile.md)| Update to be applied to file | [required] 

### Return type

[**StorageObject**](StorageObject.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

