# lusid.ScriptedTranslationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_translation_dialect**](ScriptedTranslationApi.md#get_translation_dialect) | **GET** /api/api/scriptedtranslation/dialects/{scope}/{vendor}/{sourceSystem}/{entityType}/{serialisationFormat}/{version} | [EARLY ACCESS] GetTranslationDialect: Get a dialect.
[**get_translation_script**](ScriptedTranslationApi.md#get_translation_script) | **GET** /api/api/scriptedtranslation/scripts/{scope}/{code}/{version} | [EARLY ACCESS] GetTranslationScript: Retrieve a translation script by its identifier.
[**list_dialect_ids**](ScriptedTranslationApi.md#list_dialect_ids) | **GET** /api/api/scriptedtranslation/dialects/ids | [EARLY ACCESS] ListDialectIds: List dialect identifiers matching an optional filter.
[**list_translation_script_ids**](ScriptedTranslationApi.md#list_translation_script_ids) | **GET** /api/api/scriptedtranslation/scripts/ids | [EARLY ACCESS] ListTranslationScriptIds: List translation script identifiers.
[**translate_entities**](ScriptedTranslationApi.md#translate_entities) | **POST** /api/api/scriptedtranslation/translateentities | [EARLY ACCESS] TranslateEntities: Translate a collection of entities with a specified translation script.
[**translate_entities_inlined**](ScriptedTranslationApi.md#translate_entities_inlined) | **POST** /api/api/scriptedtranslation/translateentitiesinlined | [EARLY ACCESS] TranslateEntitiesInlined: Translate a collection of entities, inlining the body of the translation script.
[**upsert_translation_dialect**](ScriptedTranslationApi.md#upsert_translation_dialect) | **POST** /api/api/scriptedtranslation/dialects | [EARLY ACCESS] UpsertTranslationDialect: Upsert a Dialect.
[**upsert_translation_script**](ScriptedTranslationApi.md#upsert_translation_script) | **POST** /api/api/scriptedtranslation/scripts | [EARLY ACCESS] UpsertTranslationScript: Upsert a translation script.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.scripted_translation_api import ScriptedTranslationApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ScriptedTranslationApi)
```

---

# **get_translation_dialect**
> Dialect getTranslationDialect = get_translation_dialect(scope, vendor, source_system, entity_type, serialisation_format, version, as_at=as_at)

[EARLY ACCESS] GetTranslationDialect: Get a dialect.

Get the dialect with the given identifier at the specific asAt time.

### Example

```python
api_instance = api_client_factory.build(ScriptedTranslationApi)
scope = 'scope_example' # str
vendor = 'vendor_example' # str
source_system = 'source_system_example' # str
entity_type = 'entity_type_example' # str
serialisation_format = 'serialisation_format_example' # str
version = 'version_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_translation_dialect(scope, vendor, source_system, entity_type, serialisation_format, version, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the dialect. | [required] 
 **vendor** | **str**| The vendor of the dialect, the entity that created it. e.g. ISDA, FINBOURNE. | [required] 
 **source_system** | **str**| The source system of the dialect, the system that understands it. e.g. LUSID, QuantLib. | [required] 
 **entity_type** | **str**| The type of entity this dialect describes e.g. Instrument. | [required] 
 **serialisation_format** | **str**| The serialisation format of a document in this dialect. e.g. JSON, XML. | [required] 
 **version** | **str**| The semantic version of the dialect: MAJOR.MINOR.PATCH. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the dialect. Defaults to return the latest version of the dialect if not specified. | [optional] 

### Return type

[**Dialect**](Dialect.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dialect with the given ID. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_translation_script**
> TranslationScript getTranslationScript = get_translation_script(scope, code, version, as_at=as_at)

[EARLY ACCESS] GetTranslationScript: Retrieve a translation script by its identifier.

Retrieves a translation script to be used for translating financial entities.

### Example

```python
api_instance = api_client_factory.build(ScriptedTranslationApi)
scope = 'scope_example' # str
code = 'code_example' # str
version = 'version_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_translation_script(scope, code, version, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the translation script. | [required] 
 **code** | **str**| Code of the translation script. | [required] 
 **version** | **str**| Semantic version of the translation script. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the translation script. Defaults to latest. | [optional] 

### Return type

[**TranslationScript**](TranslationScript.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested translation script. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_dialect_ids**
> PagedResourceListOfDialectId listDialectIds = list_dialect_ids(as_at=as_at, page=page, limit=limit, filter=filter)

[EARLY ACCESS] ListDialectIds: List dialect identifiers matching an optional filter.

List the stored dialects' identifiers with pagination and filtering at the specified asAt time.

### Example

```python
api_instance = api_client_factory.build(ScriptedTranslationApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_dialect_ids(as_at=as_at, page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the dialects.              Defaults to return the latest version of the dialect if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing dialect IDs from a previous call to list dialect IDs.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfDialectId**](PagedResourceListOfDialectId.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of dialect IDs. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_translation_script_ids**
> PagedResourceListOfTranslationScriptId listTranslationScriptIds = list_translation_script_ids(as_at=as_at, limit=limit, filter=filter, page=page)

[EARLY ACCESS] ListTranslationScriptIds: List translation script identifiers.

List translation script ids.

### Example

```python
api_instance = api_client_factory.build(ScriptedTranslationApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_translation_script_ids(as_at=as_at, limit=limit, filter=filter, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the script identifiers. Defaults to latest. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, Id.Version.Major eq 1 to list IDs with major version 1              or Id.Scope eq &#39;my-scripts&#39; to list result only for a particular scope. | [optional] 
 **page** | **str**| The pagination token to use to continue listing translation script IDs; this              value is returned from the previous call. If a pagination token is provided, the filter field              must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfTranslationScriptId**](PagedResourceListOfTranslationScriptId.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested translation script IDs. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **translate_entities**
> TranslateEntitiesResponse translateEntities = translate_entities(translate_entities_request)

[EARLY ACCESS] TranslateEntities: Translate a collection of entities with a specified translation script.

Run the provided translation request. The entities to translate are specified in the request body as a  dictionary with (ephemeral) unique correlation IDs. The script to use and optional dialect to validate  results against are sourced from the database.

### Example

```python
api_instance = api_client_factory.build(ScriptedTranslationApi)
translate_entities_request = TranslateEntitiesRequest()
api_response = api_instance.translate_entities(translate_entities_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_entities_request** | [**TranslateEntitiesRequest**](TranslateEntitiesRequest.md)| The entities to translate, along with identifiers for the script and (optional) dialect to use. | [required] 

### Return type

[**TranslateEntitiesResponse**](TranslateEntitiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The translated entities along with any errors for entities that failed to be translated indexed by their correlation IDs. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **translate_entities_inlined**
> TranslateEntitiesResponse translateEntitiesInlined = translate_entities_inlined(translate_entities_inlined_request)

[EARLY ACCESS] TranslateEntitiesInlined: Translate a collection of entities, inlining the body of the translation script.

Run the provided translation request. The entities to translate, script to use and dialect to validate results against  are all specified in the request body. The entities are given as a dictionary with (ephemeral) unique correlation IDs.

### Example

```python
api_instance = api_client_factory.build(ScriptedTranslationApi)
translate_entities_inlined_request = TranslateEntitiesInlinedRequest()
api_response = api_instance.translate_entities_inlined(translate_entities_inlined_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_entities_inlined_request** | [**TranslateEntitiesInlinedRequest**](TranslateEntitiesInlinedRequest.md)| The entities to translate, along with the script to use and an optional schema for validation. | [required] 

### Return type

[**TranslateEntitiesResponse**](TranslateEntitiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The translated entities along with any errors for entities that failed to be translated indexed by their correlation IDs. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_translation_dialect**
> Dialect upsertTranslationDialect = upsert_translation_dialect(upsert_dialect_request)

[EARLY ACCESS] UpsertTranslationDialect: Upsert a Dialect.

Upsert the given dialect.

### Example

```python
api_instance = api_client_factory.build(ScriptedTranslationApi)
upsert_dialect_request = UpsertDialectRequest()
api_response = api_instance.upsert_translation_dialect(upsert_dialect_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_dialect_request** | [**UpsertDialectRequest**](UpsertDialectRequest.md)| The dialect to upsert. | [required] 

### Return type

[**Dialect**](Dialect.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted dialect. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_translation_script**
> TranslationScript upsertTranslationScript = upsert_translation_script(upsert_translation_script_request)

[EARLY ACCESS] UpsertTranslationScript: Upsert a translation script.

Upserts a translation script to be used for translating financial entities.

### Example

```python
api_instance = api_client_factory.build(ScriptedTranslationApi)
upsert_translation_script_request = UpsertTranslationScriptRequest()
api_response = api_instance.upsert_translation_script(upsert_translation_script_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_translation_script_request** | [**UpsertTranslationScriptRequest**](UpsertTranslationScriptRequest.md)| The translation script to be upserted. | [required] 

### Return type

[**TranslationScript**](TranslationScript.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully created translation script. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

