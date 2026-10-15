# lusid.CollateralAgreementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collateral_agreement**](CollateralAgreementsApi.md#create_collateral_agreement) | **POST** /api/api/collateralagreements/{scope} | [EXPERIMENTAL] CreateCollateralAgreement: Create a Collateral Agreement.
[**delete_collateral_agreement**](CollateralAgreementsApi.md#delete_collateral_agreement) | **DELETE** /api/api/collateralagreements/{scope}/{code} | [EXPERIMENTAL] DeleteCollateralAgreement: Delete a Collateral Agreement.
[**get_collateral_agreement**](CollateralAgreementsApi.md#get_collateral_agreement) | **GET** /api/api/collateralagreements/{scope}/{code} | [EXPERIMENTAL] GetCollateralAgreement: Get a Collateral Agreement.
[**get_collateral_agreement_applicability**](CollateralAgreementsApi.md#get_collateral_agreement_applicability) | **GET** /api/api/collateralagreements/{scope}/{code}/$applicability | [EXPERIMENTAL] GetCollateralAgreementApplicability: Preview the portfolios a Collateral Agreement covers.
[**list_collateral_agreements**](CollateralAgreementsApi.md#list_collateral_agreements) | **GET** /api/api/collateralagreements | [EXPERIMENTAL] ListCollateralAgreements: List Collateral Agreements.
[**upsert_collateral_agreement**](CollateralAgreementsApi.md#upsert_collateral_agreement) | **PUT** /api/api/collateralagreements/{scope}/{code} | [EXPERIMENTAL] UpsertCollateralAgreement: Upsert a Collateral Agreement.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.collateral_agreements_api import CollateralAgreementsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(CollateralAgreementsApi)
```

---

# **create_collateral_agreement**
> CollateralAgreement createCollateralAgreement = create_collateral_agreement(scope, collateral_agreement_request)

[EXPERIMENTAL] CreateCollateralAgreement: Create a Collateral Agreement.

Create a new Collateral Agreement. The scope of the agreement is in the route and its code is in the request body.

### Example

```python
api_instance = api_client_factory.build(CollateralAgreementsApi)
scope = 'scope_example' # str
collateral_agreement_request = CollateralAgreementRequest()
api_response = api_instance.create_collateral_agreement(scope, collateral_agreement_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Collateral Agreement. | [required] 
 **collateral_agreement_request** | [**CollateralAgreementRequest**](../model/CollateralAgreementRequest.md)| The definition of the Collateral Agreement. | [required] 

### Return type

[**CollateralAgreement**](../model/CollateralAgreement.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Collateral Agreement. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_collateral_agreement**
> DeletedEntityResponse deleteCollateralAgreement = delete_collateral_agreement(scope, code, effective_at=effective_at)

[EXPERIMENTAL] DeleteCollateralAgreement: Delete a Collateral Agreement.

Delete a Collateral Agreement from the given effective datetime. It remains retrievable at earlier effective datetimes.

### Example

```python
api_instance = api_client_factory.build(CollateralAgreementsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_collateral_agreement(scope, code, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Collateral Agreement to be deleted. | [required] 
 **code** | **str**| The code of the Collateral Agreement to be deleted. Together with the scope this uniquely identifies the Collateral Agreement. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the Collateral Agreement is deleted. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Collateral Agreement was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_collateral_agreement**
> CollateralAgreement getCollateralAgreement = get_collateral_agreement(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetCollateralAgreement: Get a Collateral Agreement.

Retrieve the definition of a particular Collateral Agreement at an effective and asAt datetime.

### Example

```python
api_instance = api_client_factory.build(CollateralAgreementsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_collateral_agreement(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Collateral Agreement. | [required] 
 **code** | **str**| The code of the Collateral Agreement. Together with the scope this uniquely identifies the Collateral Agreement. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Collateral Agreement. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Collateral Agreement. Defaults to returning the latest version if not specified. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;CollateralAgreement&#39; domain to decorate onto the Collateral Agreement.              These must take the format {domain}/{scope}/{code}, for example &#39;CollateralAgreement/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**CollateralAgreement**](../model/CollateralAgreement.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Collateral Agreement. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_collateral_agreement_applicability**
> CollateralAgreementApplicability getCollateralAgreementApplicability = get_collateral_agreement_applicability(scope, code, effective_at=effective_at, as_at=as_at, limit=limit)

[EXPERIMENTAL] GetCollateralAgreementApplicability: Preview the portfolios a Collateral Agreement covers.

Evaluate the applicability filter of a Collateral Agreement against portfolios, using the same filter syntax as  listing portfolios, and return the portfolios it selects.

### Example

```python
api_instance = api_client_factory.build(CollateralAgreementsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
limit = 56 # int (optional)
api_response = api_instance.get_collateral_agreement_applicability(scope, code, effective_at=effective_at, as_at=as_at, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Collateral Agreement. | [required] 
 **code** | **str**| The code of the Collateral Agreement. Together with the scope this uniquely identifies the Collateral Agreement. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to evaluate the agreement and portfolios. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to evaluate the agreement and portfolios. Defaults to returning the latest version if not specified. | [optional] 
 **limit** | **int**| The maximum number of portfolios to return. Defaults to 100 if not specified. | [optional] 

### Return type

[**CollateralAgreementApplicability**](../model/CollateralAgreementApplicability.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolios the Collateral Agreement covers. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_collateral_agreements**
> PagedResourceListOfCollateralAgreement listCollateralAgreements = list_collateral_agreements(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListCollateralAgreements: List Collateral Agreements.

List all the Collateral Agreements matching the given criteria.

### Example

```python
api_instance = api_client_factory.build(CollateralAgreementsApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_collateral_agreements(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the Collateral Agreements. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list Collateral Agreements. Defaults to returning the latest version of each Collateral Agreement if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Collateral Agreements; this value is returned from the previous call. If a pagination token is provided, the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are Id.Scope, Id.Code, BaseCurrency, CounterpartyId.Code, CounterpartyId.IdTypeScope, CounterpartyId.IdTypeCode, ApplicabilityFilter, CutLabel, RecipeId.Scope, RecipeId.Code, MinimumTransferAmount, MatchTolerance, Rounding.Amount, Rounding.Deliveries, Rounding.Returns, SettlementLag.Cash, SettlementLag.Securities, Properties and Version. The margin items can be filtered with a single-condition any expression on either VariationMargin or InitialMargin over Code or Calculation.Method. For example, to filter on the counterparty code, specify \&quot;CounterpartyId.Code eq &#39;Acme&#39;\&quot;, and to find agreements with a variation margin item, specify \&quot;VariationMargin any (Code eq &#39;VM1&#39;)\&quot;. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;CollateralAgreement&#39; domain to decorate onto each Collateral Agreement.              These must take the format {domain}/{scope}/{code}, for example &#39;CollateralAgreement/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfCollateralAgreement**](../model/PagedResourceListOfCollateralAgreement.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Collateral Agreements. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_collateral_agreement**
> CollateralAgreement upsertCollateralAgreement = upsert_collateral_agreement(scope, code, upsert_collateral_agreement_request)

[EXPERIMENTAL] UpsertCollateralAgreement: Upsert a Collateral Agreement.

Create or replace the full definition of a Collateral Agreement from an effective datetime. A change to the  definition becomes a new bitemporal version: the agreement as it was declared at earlier effective datetimes,  and as of earlier asAt datetimes, remains retrievable.

### Example

```python
api_instance = api_client_factory.build(CollateralAgreementsApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_collateral_agreement_request = UpsertCollateralAgreementRequest()
api_response = api_instance.upsert_collateral_agreement(scope, code, upsert_collateral_agreement_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Collateral Agreement. | [required] 
 **code** | **str**| The code of the Collateral Agreement. Together with the scope this uniquely identifies the Collateral Agreement. | [required] 
 **upsert_collateral_agreement_request** | [**UpsertCollateralAgreementRequest**](../model/UpsertCollateralAgreementRequest.md)| The full definition of the Collateral Agreement from the effective datetime in the request, or the current LUSID system datetime if not specified. | [required] 

### Return type

[**CollateralAgreement**](../model/CollateralAgreement.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Collateral Agreement as it stands from the effective datetime. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

