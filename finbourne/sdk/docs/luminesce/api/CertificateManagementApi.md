# luminesce.CertificateManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_certificate**](CertificateManagementApi.md#download_certificate) | **GET** /honeycomb/api/Certificate/certificate | DownloadCertificate: Download domain or your personal certificates
[**list_certificates**](CertificateManagementApi.md#list_certificates) | **GET** /honeycomb/api/Certificate/certificates | ListCertificates: List previously minted certificates
[**manage_certificate**](CertificateManagementApi.md#manage_certificate) | **PUT** /honeycomb/api/Certificate/manage | ManageCertificate: Create / Renew / Revoke a certificate


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.luminesce.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.luminesce.api.certificate_management_api import CertificateManagementApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(CertificateManagementApi)
```

---

# **download_certificate**
> bytes downloadCertificate = download_certificate(type=type, file_type=file_type, may_auto_create=may_auto_create)

DownloadCertificate: Download domain or your personal certificates

 Downloads your latest Domain or your User certificate's public or private key - if any.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - certificate is not available for some reason - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(CertificateManagementApi)
type = luminesce.CertificateType() # CertificateType (optional)
file_type = luminesce.CertificateFileType() # CertificateFileType (optional)
may_auto_create = False # bool (optional)
api_response = api_instance.download_certificate(type=type, file_type=file_type, may_auto_create=may_auto_create)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**CertificateType**](.md)| User or Domain level cert (Domain level requires additional entitlements) | [optional] 
 **file_type** | [**CertificateFileType**](.md)| Should the public key or private key be downloaded? (both must be in place to run providers) | [optional] 
 **may_auto_create** | **bool**| If no matching cert is available, should an attempt be made to Create/Renew it with default options? | [optional] [default to False]

### Return type

**bytes**

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

---

# **list_certificates**
> List[CertificateState] listCertificates = list_certificates()

ListCertificates: List previously minted certificates

 Lists all the certificates previously minted to which you have access.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(CertificateManagementApi)
api_response = api_instance.list_certificates()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[CertificateState]**](CertificateState.md)

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

---

# **manage_certificate**
> CertificateState manageCertificate = manage_certificate(action=action, type=type, version=version, validity_start=validity_start, validity_end=validity_end, dry_run=dry_run)

ManageCertificate: Create / Renew / Revoke a certificate

 Manages a certificate.  This could be creating a new one, renewing an old one or revoking one explicitly.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something about the request cannot be processed - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(CertificateManagementApi)
action = luminesce.CertificateAction() # CertificateAction (optional)
type = luminesce.CertificateType() # CertificateType (optional)
version = 1 # int (optional)
validity_start = '2013-10-20T19:20:30+01:00' # datetime (optional)
validity_end = '2013-10-20T19:20:30+01:00' # datetime (optional)
dry_run = True # bool (optional)
api_response = api_instance.manage_certificate(action=action, type=type, version=version, validity_start=validity_start, validity_end=validity_end, dry_run=dry_run)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | [**CertificateAction**](.md)| The Action to perform, e.g. Create / Renew / Revoke | [optional] 
 **type** | [**CertificateType**](.md)| User or Domain level cert (Domain level requires additional entitlements) | [optional] 
 **version** | **int**| Version number of the cert, the request will fail to validate if incorrect | [optional] [default to 1]
 **validity_start** | **datetime**| When should the cert first be valid (defaults to the current time in UTC) | [optional] 
 **validity_end** | **datetime**| When should the cert no longer be valid (defaults to 13 months from now) | [optional] 
 **dry_run** | **bool**| True will just validate the request, but perform no changes to any system | [optional] [default to True]

### Return type

[**CertificateState**](CertificateState.md)

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

