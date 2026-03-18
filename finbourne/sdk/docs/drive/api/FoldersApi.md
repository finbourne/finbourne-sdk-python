# drive.FoldersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folder**](FoldersApi.md#create_folder) | **POST** /drive/api/folders | [EARLY ACCESS] CreateFolder: Create a new folder in LUSID Drive
[**delete_folder**](FoldersApi.md#delete_folder) | **DELETE** /drive/api/folders/{id} | [EARLY ACCESS] DeleteFolder: Delete a specified folder and all subfolders
[**get_folder**](FoldersApi.md#get_folder) | **GET** /drive/api/folders/{id} | [EARLY ACCESS] GetFolder: Get metadata of folder
[**get_folder_contents**](FoldersApi.md#get_folder_contents) | **GET** /drive/api/folders/{id}/contents | GetFolderContents: List contents of a folder
[**get_root_folder**](FoldersApi.md#get_root_folder) | **GET** /drive/api/folders | GetRootFolder: List contents of root folder
[**move_folder**](FoldersApi.md#move_folder) | **POST** /drive/api/folders/{id} | [EARLY ACCESS] MoveFolder: Move files to specified folder
[**update_folder**](FoldersApi.md#update_folder) | **PUT** /drive/api/folders/{id} | [EARLY ACCESS] UpdateFolder: Update an existing folder&#39;s name, path


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.drive.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.drive.api.folders_api import FoldersApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(FoldersApi)
```

---

# **create_folder**
> StorageObject createFolder = create_folder(create_folder)

[EARLY ACCESS] CreateFolder: Create a new folder in LUSID Drive

### Example

```python
api_instance = api_client_factory.build(FoldersApi)
create_folder = CreateFolder()
api_response = api_instance.create_folder(create_folder)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_folder** | [**CreateFolder**](CreateFolder.md)| A CreateFolder object that defines the name and path of the new folder | [required] 

### Return type

[**StorageObject**](StorageObject.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_folder**
> deleteFolder = delete_folder(id)

[EARLY ACCESS] DeleteFolder: Delete a specified folder and all subfolders

### Example

```python
api_instance = api_client_factory.build(FoldersApi)
id = 'id_example' # str
api_instance.delete_folder(id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder | [required] 

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
**404** | No folder with this Id exists |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_folder**
> StorageObject getFolder = get_folder(id)

[EARLY ACCESS] GetFolder: Get metadata of folder

### Example

```python
api_instance = api_client_factory.build(FoldersApi)
id = 'id_example' # str
api_response = api_instance.get_folder(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder | [required] 

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
**404** | No folder with this Id exists |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_folder_contents**
> PagedResourceListOfStorageObject getFolderContents = get_folder_contents(id, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

GetFolderContents: List contents of a folder

### Example

```python
api_instance = api_client_factory.build(FoldersApi)
id = 'id_example' # str
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
start = 56 # int (optional)
limit = 56 # int (optional)
filter = '' # str (optional)
api_response = api_instance.get_folder_contents(id, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder | [required] 
 **page** | **str**| The pagination token to use to continue listing contents from a previous call to list contents.             This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields             must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfStorageObject**](PagedResourceListOfStorageObject.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No folder with this Id exists |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_root_folder**
> PagedResourceListOfStorageObject getRootFolder = get_root_folder(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

GetRootFolder: List contents of root folder

### Example

```python
api_instance = api_client_factory.build(FoldersApi)
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
start = 56 # int (optional)
limit = 56 # int (optional)
filter = 'true' # str (optional)
api_response = api_instance.get_root_folder(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing contents from a previous call to list contents.             This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields             must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] [default to &#39;true&#39;]

### Return type

[**PagedResourceListOfStorageObject**](PagedResourceListOfStorageObject.md)

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

# **move_folder**
> PagedResourceListOfStorageObject moveFolder = move_folder(id, request_body, overwrite=overwrite, delete_source=delete_source)

[EARLY ACCESS] MoveFolder: Move files to specified folder

### Example

```python
api_instance = api_client_factory.build(FoldersApi)
id = 'id_example' # str
request_body = ["FolderID1","FolderID2","FolderID3"] # List[str]
overwrite = False # bool (optional)
delete_source = False # bool (optional)
api_response = api_instance.move_folder(id, request_body, overwrite=overwrite, delete_source=delete_source)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder where the files should be moved | [required] 
 **request_body** | [**List[str]**](str.md)| Enumerable of unique IDs of files that should be moved | [required] 
 **overwrite** | **bool**| True if the destination has file with same name if should be overwritten | [optional] [default to False]
 **delete_source** | **bool**| If true after moving the original file is deleted | [optional] [default to False]

### Return type

[**PagedResourceListOfStorageObject**](PagedResourceListOfStorageObject.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No folder or file with the supplied Id exists |  -  |
**409** | There is already a file with the same name at this location |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_folder**
> StorageObject updateFolder = update_folder(id, update_folder)

[EARLY ACCESS] UpdateFolder: Update an existing folder's name, path

### Example

```python
api_instance = api_client_factory.build(FoldersApi)
id = 'id_example' # str
update_folder = UpdateFolder()
api_response = api_instance.update_folder(id, update_folder)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder | [required] 
 **update_folder** | [**UpdateFolder**](UpdateFolder.md)| An UpdateFolder object that defines the new name or path of the folder | [required] 

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
**404** | No folder with this Id exists |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

