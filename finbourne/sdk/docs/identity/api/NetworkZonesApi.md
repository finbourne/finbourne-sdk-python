# identity.NetworkZonesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_zone**](NetworkZonesApi.md#create_network_zone) | **POST** /identity/api/networkzones | [EARLY ACCESS] CreateNetworkZone: Creates a network zone
[**delete_network_zone**](NetworkZonesApi.md#delete_network_zone) | **DELETE** /identity/api/networkzones/{code} | [EARLY ACCESS] DeleteNetworkZone: Deletes a network zone
[**get_network_zone**](NetworkZonesApi.md#get_network_zone) | **GET** /identity/api/networkzones/{code} | [EARLY ACCESS] GetNetworkZone: Retrieve a Network Zone
[**list_network_zones**](NetworkZonesApi.md#list_network_zones) | **GET** /identity/api/networkzones | [EARLY ACCESS] ListNetworkZones: Lists all network zones for a domain
[**update_network_zone**](NetworkZonesApi.md#update_network_zone) | **PUT** /identity/api/networkzones/{code} | [EARLY ACCESS] UpdateNetworkZone: Updates an existing network zone


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.network_zones_api import NetworkZonesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(NetworkZonesApi)
```

---

# **create_network_zone**
> NetworkZoneDefinitionResponse createNetworkZone = create_network_zone(create_network_zone_request)

[EARLY ACCESS] CreateNetworkZone: Creates a network zone

By default, the network zone will have its hierarchy set to last on creation.

### Example

```python
api_instance = api_client_factory.build(NetworkZonesApi)
create_network_zone_request = CreateNetworkZoneRequest()
api_response = api_instance.create_network_zone(create_network_zone_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_network_zone_request** | [**CreateNetworkZoneRequest**](CreateNetworkZoneRequest.md)| The details of the network zone to define | [required] 

### Return type

[**NetworkZoneDefinitionResponse**](NetworkZoneDefinitionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create Network Zone |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_network_zone**
> deleteNetworkZone = delete_network_zone(code)

[EARLY ACCESS] DeleteNetworkZone: Deletes a network zone

Will return a success if network zone already deleted

### Example

```python
api_instance = api_client_factory.build(NetworkZonesApi)
code = 'code_example' # str
api_instance.delete_network_zone(code)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The unique identifier of the network zone to delete | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_network_zone**
> NetworkZoneDefinitionResponse getNetworkZone = get_network_zone(code)

[EARLY ACCESS] GetNetworkZone: Retrieve a Network Zone

Retrieves a Network Zone

### Example

```python
api_instance = api_client_factory.build(NetworkZonesApi)
code = 'code_example' # str
api_response = api_instance.get_network_zone(code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The unique identifier of the network zone | [required] 

### Return type

[**NetworkZoneDefinitionResponse**](NetworkZoneDefinitionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Network Zone |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_network_zones**
> List[NetworkZoneDefinitionResponse] listNetworkZones = list_network_zones()

[EARLY ACCESS] ListNetworkZones: Lists all network zones for a domain

Lists all network zones for a domain

### Example

```python
api_instance = api_client_factory.build(NetworkZonesApi)
api_response = api_instance.list_network_zones()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[NetworkZoneDefinitionResponse]**](NetworkZoneDefinitionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Network Zones |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_network_zone**
> NetworkZoneDefinitionResponse updateNetworkZone = update_network_zone(code, update_network_zone_request)

[EARLY ACCESS] UpdateNetworkZone: Updates an existing network zone

Updates an existing network zone

### Example

```python
api_instance = api_client_factory.build(NetworkZonesApi)
code = 'code_example' # str
update_network_zone_request = UpdateNetworkZoneRequest()
api_response = api_instance.update_network_zone(code, update_network_zone_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The unique identifier of the network zone | [required] 
 **update_network_zone_request** | [**UpdateNetworkZoneRequest**](UpdateNetworkZoneRequest.md)| The updated definition of the network zone | [required] 

### Return type

[**NetworkZoneDefinitionResponse**](NetworkZoneDefinitionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Network Zone |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

