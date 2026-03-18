# lusid.ConfigurationRecipeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_configuration_recipe**](ConfigurationRecipeApi.md#delete_configuration_recipe) | **DELETE** /api/api/recipes/{scope}/{code} | DeleteConfigurationRecipe: Delete a Configuration Recipe, assuming that it is present.
[**delete_recipe_composer**](ConfigurationRecipeApi.md#delete_recipe_composer) | **DELETE** /api/api/recipes/composer/{scope}/{code} | DeleteRecipeComposer: Delete a Recipe Composer, assuming that it is present.
[**get_configuration_recipe**](ConfigurationRecipeApi.md#get_configuration_recipe) | **GET** /api/api/recipes/{scope}/{code} | GetConfigurationRecipe: Get Configuration Recipe
[**get_derived_recipe**](ConfigurationRecipeApi.md#get_derived_recipe) | **GET** /api/api/recipes/derived/{scope}/{code} | GetDerivedRecipe: Get Configuration Recipe either from the store or expanded from a Recipe Composer.
[**get_recipe_composer**](ConfigurationRecipeApi.md#get_recipe_composer) | **GET** /api/api/recipes/composer/{scope}/{code} | GetRecipeComposer: Get Recipe Composer
[**get_recipe_composer_resolved_inline**](ConfigurationRecipeApi.md#get_recipe_composer_resolved_inline) | **POST** /api/api/recipes/composer/resolvedinline$ | GetRecipeComposerResolvedInline: Given a Recipe Composer, this endpoint expands into a Configuration Recipe without persistence. Primarily used for testing purposes.
[**list_configuration_recipes**](ConfigurationRecipeApi.md#list_configuration_recipes) | **GET** /api/api/recipes | ListConfigurationRecipes: List the set of Configuration Recipes
[**list_derived_recipes**](ConfigurationRecipeApi.md#list_derived_recipes) | **GET** /api/api/recipes/derived | ListDerivedRecipes: List the complete set of all Configuration Recipes, both from the configuration recipe store and also from expanded recipe composers.
[**list_recipe_composers**](ConfigurationRecipeApi.md#list_recipe_composers) | **GET** /api/api/recipes/composer | ListRecipeComposers: List the set of Recipe Composers
[**upsert_configuration_recipe**](ConfigurationRecipeApi.md#upsert_configuration_recipe) | **POST** /api/api/recipes | UpsertConfigurationRecipe: Upsert a Configuration Recipe. This creates or updates the data in Lusid.
[**upsert_recipe_composer**](ConfigurationRecipeApi.md#upsert_recipe_composer) | **POST** /api/api/recipes/composer | UpsertRecipeComposer: Upsert a Recipe Composer. This creates or updates the data in Lusid.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.configuration_recipe_api import ConfigurationRecipeApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ConfigurationRecipeApi)
```

---

# **delete_configuration_recipe**
> AnnulSingleStructuredDataResponse deleteConfigurationRecipe = delete_configuration_recipe(scope, code)

DeleteConfigurationRecipe: Delete a Configuration Recipe, assuming that it is present.

Delete the specified Configuration Recipe from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.

### Example

```python
api_instance = api_client_factory.build(ConfigurationRecipeApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_configuration_recipe(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Configuration Recipe to delete. | [required] 
 **code** | **str**| The Configuration Recipe to delete. | [required] 

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

# **delete_recipe_composer**
> AnnulSingleStructuredDataResponse deleteRecipeComposer = delete_recipe_composer(scope, code)

DeleteRecipeComposer: Delete a Recipe Composer, assuming that it is present.

Delete the specified Recipe Composer from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.

### Example

```python
api_instance = api_client_factory.build(ConfigurationRecipeApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_recipe_composer(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Recipe Composer to delete. | [required] 
 **code** | **str**| The Recipe Composer to delete. | [required] 

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

# **get_configuration_recipe**
> GetRecipeResponse getConfigurationRecipe = get_configuration_recipe(scope, code, as_at=as_at)

GetConfigurationRecipe: Get Configuration Recipe

Get a Configuration Recipe from a single scope.                The response will return either the recipe that has been stored, or a failure explaining why the request was unsuccessful.                It is important to always check for any unsuccessful requests (failures).

### Example

```python
api_instance = api_client_factory.build(ConfigurationRecipeApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_configuration_recipe(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Configuration Recipe to retrieve. | [required] 
 **code** | **str**| The name of the recipe to retrieve the data for. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Configuration Recipe. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetRecipeResponse**](GetRecipeResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Configuration Recipe or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_derived_recipe**
> GetRecipeResponse getDerivedRecipe = get_derived_recipe(scope, code, as_at=as_at)

GetDerivedRecipe: Get Configuration Recipe either from the store or expanded from a Recipe Composer.

If scope-code is referring to a Configuration Recipe it is returned, if it refers to Recipe Composer, it is expanded into a Configuration Recipe and returned.

### Example

```python
api_instance = api_client_factory.build(ConfigurationRecipeApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_derived_recipe(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Configuration Recipe or Recipe Composer to return. | [required] 
 **code** | **str**| The code of the Configuration Recipe or Recipe Composer to return. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Configuration Recipe. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetRecipeResponse**](GetRecipeResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Configuration Recipe or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_recipe_composer**
> GetRecipeComposerResponse getRecipeComposer = get_recipe_composer(scope, code, as_at=as_at)

GetRecipeComposer: Get Recipe Composer

Get a Recipe Composer from a single scope.                The response will return either the recipe composer that has been stored, or a failure explaining why the request was unsuccessful.                It is important to always check for any unsuccessful requests (failures).

### Example

```python
api_instance = api_client_factory.build(ConfigurationRecipeApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_recipe_composer(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Recipe Composer to retrieve. | [required] 
 **code** | **str**| The name of the Recipe Composer to retrieve the data for. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Recipe Composer. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetRecipeComposerResponse**](GetRecipeComposerResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Recipe Composer or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_recipe_composer_resolved_inline**
> GetRecipeResponse getRecipeComposerResolvedInline = get_recipe_composer_resolved_inline(upsert_recipe_composer_request)

GetRecipeComposerResolvedInline: Given a Recipe Composer, this endpoint expands into a Configuration Recipe without persistence. Primarily used for testing purposes.

Resolves an inline recipe composer into a ConfigurationRecipe.

### Example

```python
api_instance = api_client_factory.build(ConfigurationRecipeApi)
upsert_recipe_composer_request = UpsertRecipeComposerRequest()
api_response = api_instance.get_recipe_composer_resolved_inline(upsert_recipe_composer_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_recipe_composer_request** | [**UpsertRecipeComposerRequest**](UpsertRecipeComposerRequest.md)| Recipe composer used to expand into the Configuration Recipe. | [required] 

### Return type

[**GetRecipeResponse**](GetRecipeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully resolved Configuration Recipe. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_configuration_recipes**
> ResourceListOfGetRecipeResponse listConfigurationRecipes = list_configuration_recipes(as_at=as_at, filter=filter)

ListConfigurationRecipes: List the set of Configuration Recipes

List the set of configuration recipes at the specified date/time and scope. Note this only returns recipes stored directly and does not include any recipes expanded from recipe composers.

### Example

```python
api_instance = api_client_factory.build(ConfigurationRecipeApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_configuration_recipes(as_at=as_at, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Configuration Recipes. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfGetRecipeResponse**](ResourceListOfGetRecipeResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested configuration recipes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_derived_recipes**
> ResourceListOfGetRecipeResponse listDerivedRecipes = list_derived_recipes(as_at=as_at, filter=filter)

ListDerivedRecipes: List the complete set of all Configuration Recipes, both from the configuration recipe store and also from expanded recipe composers.

This endpoints returns a union of the output of ListConfigurationRecipes and the resolved Recipe Composers from the ListRecipeComposers endpoints.  Recipe Composers that fail to generate a valid Configuration Recipe will not be reported.

### Example

```python
api_instance = api_client_factory.build(ConfigurationRecipeApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_derived_recipes(as_at=as_at, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Configuration Recipes. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set, note this functionality is not yet enabled for this endpoint. | [optional] 

### Return type

[**ResourceListOfGetRecipeResponse**](ResourceListOfGetRecipeResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested configuration recipes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_recipe_composers**
> ResourceListOfGetRecipeComposerResponse listRecipeComposers = list_recipe_composers(as_at=as_at, filter=filter)

ListRecipeComposers: List the set of Recipe Composers

List the set of Recipe Composers at the specified date/time and scope

### Example

```python
api_instance = api_client_factory.build(ConfigurationRecipeApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_recipe_composers(as_at=as_at, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Recipes Composers. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set, note this functionality is not yet enabled for this endpoint. | [optional] 

### Return type

[**ResourceListOfGetRecipeComposerResponse**](ResourceListOfGetRecipeComposerResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested recipe composers |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_configuration_recipe**
> UpsertSingleStructuredDataResponse upsertConfigurationRecipe = upsert_configuration_recipe(upsert_recipe_request)

UpsertConfigurationRecipe: Upsert a Configuration Recipe. This creates or updates the data in Lusid.

Update or insert one Configuration Recipe in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Configuration Recipe or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

```python
api_instance = api_client_factory.build(ConfigurationRecipeApi)
upsert_recipe_request = UpsertRecipeRequest()
api_response = api_instance.upsert_configuration_recipe(upsert_recipe_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_recipe_request** | [**UpsertRecipeRequest**](UpsertRecipeRequest.md)| The Configuration Recipe to update or insert | [required] 

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

---

# **upsert_recipe_composer**
> UpsertSingleStructuredDataResponse upsertRecipeComposer = upsert_recipe_composer(upsert_recipe_composer_request)

UpsertRecipeComposer: Upsert a Recipe Composer. This creates or updates the data in Lusid.

Update or insert one Recipe Composer in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Recipe Composer or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

```python
api_instance = api_client_factory.build(ConfigurationRecipeApi)
upsert_recipe_composer_request = UpsertRecipeComposerRequest()
api_response = api_instance.upsert_recipe_composer(upsert_recipe_composer_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_recipe_composer_request** | [**UpsertRecipeComposerRequest**](UpsertRecipeComposerRequest.md)| The Recipe Composer to update or insert | [required] 

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

