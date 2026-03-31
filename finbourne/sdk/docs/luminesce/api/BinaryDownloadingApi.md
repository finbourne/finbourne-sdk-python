# luminesce.BinaryDownloadingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_binary**](BinaryDownloadingApi.md#download_binary) | **GET** /honeycomb/api/Download/download | DownloadBinary: Download a Luminesce Binary you may run on-site
[**get_binary_versions**](BinaryDownloadingApi.md#get_binary_versions) | **GET** /honeycomb/api/Download/versions | GetBinaryVersions: List available versions of binaries


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.luminesce.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.luminesce.api.binary_downloading_api import BinaryDownloadingApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(BinaryDownloadingApi)
```

---

# **download_binary**
> bytes downloadBinary = download_binary(type=type, version=version)

DownloadBinary: Download a Luminesce Binary you may run on-site

 Downloads the latest version (or specific if needs be) of the specified Luminesce Binary, given the required entitlements.  > This endpoint is an alternative to time-consuming manual distribution via Drive or Email. > it relies on an underlying datastore that is not quite as \"Highly Available\" to the degree  > that FINBOURNE services generally are.   > Thus it is not subject to the same SLAs as other API endpoints are. > *If you perceive an outage, please try again later.*  Once a file has been downloaded the following steps can be used to install it (for the dotnet tools at least):  (1) Open a terminal and cd to the directory you downloaded it to  (2) Install / extract files from that package via:  ``` dotnet tool install NameOfFileWithoutVersionNumberOrExtension -g --add-source \".\" ``` e.g. ``` dotnet tool install Finbourne.Luminesce.DbProviders.Oracle_Snowflake -g --add-source \".\" ``` More information on the installations can be found [here](https://support.lusid.com/docs/how-do-i-use-the-luminesce-cli).  (3) Execute them (see documentation for specific binary, e.g. [Sql.Db.Mine](https://support.lusid.com/docs/readwrite-to-sql-databases-sqldbmine) or [CLI](https://support.lusid.com/docs/how-do-i-use-the-luminesce-cli)).  The installed binaries can then be found in - Windows - `%USERPROFILE%\\.dotnet\\tools\\.store\\` - Linux/macOS - `$HOME/.dotnet/tools/.store/`  Note that the binaries all require the dotnet runtime to be installed. - `dotnet8` is required for all currently supported versions  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - binary file is not available for some reason (e.g. permissions or invalid version) - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(BinaryDownloadingApi)
type = luminesce.LuminesceBinaryType() # LuminesceBinaryType (optional)
version = 'version_example' # str (optional)
api_response = api_instance.download_binary(type=type, version=version)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**LuminesceBinaryType**](.md)| Type of binary to download (each requires separate licenses and entitlements) | [optional] 
 **version** | **str**| An explicit version of the binary.  Leave blank to get the latest version (recommended) | [optional] 

### Return type

**bytes**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The .nupkg or .msi file of the requested binary |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_binary_versions**
> List[str] getBinaryVersions = get_binary_versions(type=type)

GetBinaryVersions: List available versions of binaries

 Gets all available versions of a given binary type (from newest to oldest) This does not mean you are entitled to download them.

### Example

```python
api_instance = api_client_factory.build(BinaryDownloadingApi)
type = luminesce.LuminesceBinaryType() # LuminesceBinaryType (optional)
api_response = api_instance.get_binary_versions(type=type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**LuminesceBinaryType**](.md)| Type of binary to fetch available versions of | [optional] 

### Return type

**List[str]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

