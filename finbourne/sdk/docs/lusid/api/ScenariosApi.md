# lusid.ScenariosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scenario_from_template**](ScenariosApi.md#create_scenario_from_template) | **POST** /api/api/scenarios/{scope}/$fromTemplate | [EARLY ACCESS] CreateScenarioFromTemplate: [EARLY ACCESS] CreateScenarioFromTemplate: Create a Scenario from a pre-built template.
[**delete_scenario**](ScenariosApi.md#delete_scenario) | **DELETE** /api/api/scenarios/{scope}/{code} | [EARLY ACCESS] DeleteScenario: Delete a Scenario, assuming that it is present.
[**get_scenario**](ScenariosApi.md#get_scenario) | **GET** /api/api/scenarios/{scope}/{code} | [EARLY ACCESS] GetScenario: Get Scenario
[**list_scenario_versions**](ScenariosApi.md#list_scenario_versions) | **GET** /api/api/scenarios/{scope}/{code}/versions | [EARLY ACCESS] ListScenarioVersions: List the versions of a Scenario
[**list_scenarios**](ScenariosApi.md#list_scenarios) | **GET** /api/api/scenarios/{scope} | [EARLY ACCESS] ListScenarios: List the set of Scenario definitions
[**preview_scenario**](ScenariosApi.md#preview_scenario) | **POST** /api/api/scenarios/$preview | [EARLY ACCESS] PreviewScenario: Preview a Scenario
[**upsert_scenario**](ScenariosApi.md#upsert_scenario) | **POST** /api/api/scenarios | [EARLY ACCESS] UpsertScenario: Upsert a Scenario. This creates or updates the scenario definition in LUSID.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.scenarios_api import ScenariosApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ScenariosApi)
```

---

# **create_scenario_from_template**
> UpsertSingleStructuredDataResponse createScenarioFromTemplate = create_scenario_from_template(scope, create_scenario_from_template_request)

[EARLY ACCESS] CreateScenarioFromTemplate: [EARLY ACCESS] CreateScenarioFromTemplate: Create a Scenario from a pre-built template.

Creates and stores a scenario built from a pre-defined parameterised template, for example a  parallel rates shift or an equity crash. The template determines the scenario's shifts; the  parameters supply the targets (e.g. currency or instrument) and optionally override the default  shift size. The created scenario is stored in the given scope and behaves exactly like a  hand-built scenario.                Available templates: RatesUp, RatesDown, CurveSteepener, CurveFlattener, VolSpike, EquityCrash,  FxShock, RiskOff.

### Example

```python
api_instance = api_client_factory.build(ScenariosApi)
scope = 'scope_example' # str
create_scenario_from_template_request = CreateScenarioFromTemplateRequest()
api_response = api_instance.create_scenario_from_template(scope, create_scenario_from_template_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the scenario | [required] 
 **create_scenario_from_template_request** | [**CreateScenarioFromTemplateRequest**](CreateScenarioFromTemplateRequest.md)| The template, code and parameters to create the scenario from | [required] 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully created scenario or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_scenario**
> AnnulSingleStructuredDataResponse deleteScenario = delete_scenario(scope, code)

[EARLY ACCESS] DeleteScenario: Delete a Scenario, assuming that it is present.

Delete the specified Scenario definition from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.

### Example

```python
api_instance = api_client_factory.build(ScenariosApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_scenario(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Scenario to delete. | [required] 
 **code** | **str**| The Scenario to delete. | [required] 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_scenario**
> GetScenarioResponse getScenario = get_scenario(scope, code, as_at=as_at)

[EARLY ACCESS] GetScenario: Get Scenario

Get a Scenario definition from a single scope.                The response will return either the scenario that has been stored, or a failure explaining why the request was unsuccessful.

### Example

```python
api_instance = api_client_factory.build(ScenariosApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_scenario(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Scenario to retrieve. | [required] 
 **code** | **str**| The code of the Scenario to retrieve. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Scenario. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetScenarioResponse**](GetScenarioResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Scenario or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_scenario_versions**
> PagedResourceListOfVersion listScenarioVersions = list_scenario_versions(scope, code, as_at=as_at, limit=limit, page=page)

[EARLY ACCESS] ListScenarioVersions: List the versions of a Scenario

List the AsAt versions of a single Scenario definition, newest first: one entry per change,  with the version number, the AsAt datetime it was written, and the user that wrote it.                Scenarios are perpetual (AsAt-only), so a version's AsAt datetime identifies it completely:  pass it as the asAt on GetScenario to view that version, or as the scenario reference's  asAt on a valuation to price under it.

### Example

```python
api_instance = api_client_factory.build(ScenariosApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_scenario_versions(scope, code, as_at=as_at, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Scenario to list versions for. | [required] 
 **code** | **str**| The code of the Scenario to list versions for. | [required] 
 **as_at** | **datetime**| The asAt datetime to cap the version history at. Defaults to all versions up to now. | [optional] 
 **limit** | **int**| Maximum number of results to return. Defaults to 100. | [optional] 
 **page** | **str**| Pagination token from a previous result to fetch the next page. | [optional] 

### Return type

[**PagedResourceListOfVersion**](PagedResourceListOfVersion.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The versions of the scenario, newest first |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_scenarios**
> PagedResourceListOfGetScenarioResponse listScenarios = list_scenarios(scope, as_at=as_at, filter=filter, limit=limit, page=page)

[EARLY ACCESS] ListScenarios: List the set of Scenario definitions

List the set of scenario definitions at the specified date/time and scope.

### Example

```python
api_instance = api_client_factory.build(ScenariosApi)
scope = 'scope_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_scenarios(scope, as_at=as_at, filter=filter, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to list scenarios for. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the scenarios. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| Maximum number of results to return. Defaults to 100. | [optional] 
 **page** | **str**| Pagination token from a previous result to fetch the next page. | [optional] 

### Return type

[**PagedResourceListOfGetScenarioResponse**](PagedResourceListOfGetScenarioResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested scenarios |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **preview_scenario**
> ScenarioPreviewResponse previewScenario = preview_scenario(scenario_preview_request)

[EARLY ACCESS] PreviewScenario: Preview a Scenario

Preview what a scenario would do to a portfolio's market data, without running a valuation.                The portfolio's market data dependencies are resolved through the given recipe and the scenario's  shifts are applied; the response lists every market data target the shifts changed, with values  before and after, plus any market data that matched a shift but could not honour it. Supply  either a reference to a stored scenario, or inline shift definitions to test a definition before  saving it.

### Example

```python
api_instance = api_client_factory.build(ScenariosApi)
scenario_preview_request = ScenarioPreviewRequest()
api_response = api_instance.preview_scenario(scenario_preview_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_preview_request** | [**ScenarioPreviewRequest**](ScenarioPreviewRequest.md)| The recipe, portfolios, effective date and scenario (stored reference or inline shifts) to preview | [required] 

### Return type

[**ScenarioPreviewResponse**](ScenarioPreviewResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The preview of the scenario&#39;s effect on the portfolio&#39;s market data, or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_scenario**
> UpsertSingleStructuredDataResponse upsertScenario = upsert_scenario(upsert_scenario_request)

[EARLY ACCESS] UpsertScenario: Upsert a Scenario. This creates or updates the scenario definition in LUSID.

Update or insert one Scenario definition. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted scenario or failure message if unsuccessful.

### Example

```python
api_instance = api_client_factory.build(ScenariosApi)
upsert_scenario_request = UpsertScenarioRequest()
api_response = api_instance.upsert_scenario(upsert_scenario_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_scenario_request** | [**UpsertScenarioRequest**](UpsertScenarioRequest.md)| The Scenario to update or insert | [required] 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

