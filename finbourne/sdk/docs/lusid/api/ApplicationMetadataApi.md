# lusid.ApplicationMetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_excel_addin**](ApplicationMetadataApi.md#get_excel_addin) | **GET** /api/api/metadata/downloads/exceladdin | GetExcelAddin: Download Excel Addin
[**get_lusid_versions**](ApplicationMetadataApi.md#get_lusid_versions) | **GET** /api/api/metadata/versions | GetLusidVersions: Get LUSID versions
[**list_access_controlled_resources**](ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/api/metadata/access/resources | ListAccessControlledResources: Get resources available for access control


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.application_metadata_api import ApplicationMetadataApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ApplicationMetadataApi)
```

---

# **get_excel_addin**
> FileResponse getExcelAddin = get_excel_addin(version=version)

GetExcelAddin: Download Excel Addin

Download the LUSID Excel Addin for Microsoft Excel. Not providing a specific value will return the latest version being returned

### Example

```python
api_instance = api_client_factory.build(ApplicationMetadataApi)
version = 'version_example' # str (optional)
api_response = api_instance.get_excel_addin(version=version)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| The requested version of the Excel plugin | [optional] 

### Return type

[**FileResponse**](FileResponse.md)

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

# **get_lusid_versions**
> VersionSummaryDto getLusidVersions = get_lusid_versions()

GetLusidVersions: Get LUSID versions

Get the semantic versions associated with LUSID and its ecosystem

### Example

```python
api_instance = api_client_factory.build(ApplicationMetadataApi)
api_response = api_instance.get_lusid_versions()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionSummaryDto**](VersionSummaryDto.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection of versions associated with LUSID |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_access_controlled_resources**
> ResourceListOfAccessControlledResource listAccessControlledResources = list_access_controlled_resources(filter=filter)

ListAccessControlledResources: Get resources available for access control

Get the comprehensive set of resources that are available for access control

### Example

```python
api_instance = api_client_factory.build(ApplicationMetadataApi)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_access_controlled_resources(filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Optional. Expression to filter the result set.               For example, to filter on the Application, use \&quot;application eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfAccessControlledResource**](ResourceListOfAccessControlledResource.md)

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

