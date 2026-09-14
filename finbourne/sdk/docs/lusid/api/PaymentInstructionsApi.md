# lusid.PaymentInstructionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_payment_instruction**](PaymentInstructionsApi.md#delete_payment_instruction) | **DELETE** /api/api/paymentinstructions/{scope}/{code} | [EXPERIMENTAL] DeletePaymentInstruction: Delete Payment Instruction
[**get_payment_instruction**](PaymentInstructionsApi.md#get_payment_instruction) | **GET** /api/api/paymentinstructions/{scope}/{code} | [EXPERIMENTAL] GetPaymentInstruction: Get Payment Instruction
[**get_payment_instructions_by_payment_record_ids**](PaymentInstructionsApi.md#get_payment_instructions_by_payment_record_ids) | **POST** /api/api/paymentinstructions/$getByPaymentRecordIds | [EXPERIMENTAL] GetPaymentInstructionsByPaymentRecordIds: Get Payment Instructions by Payment Record Ids
[**upsert_payment_instructions**](PaymentInstructionsApi.md#upsert_payment_instructions) | **POST** /api/api/paymentinstructions | [EXPERIMENTAL] UpsertPaymentInstructions: Upsert Payment Instructions


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.payment_instructions_api import PaymentInstructionsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(PaymentInstructionsApi)
```

---

# **delete_payment_instruction**
> DeletedEntityResponse deletePaymentInstruction = delete_payment_instruction(scope, code)

[EXPERIMENTAL] DeletePaymentInstruction: Delete Payment Instruction

Delete a Payment Instruction. Deletion will be valid from the payment instruction's creation datetime.  This means that the payment instruction will no longer exist at any effective datetime from the asAt datetime  of deletion. Any payment records the instruction owns are released and become available to another instruction.  A payment instruction that has been released, instructed, sent, cancelled or failed cannot be deleted.

### Example

```python
api_instance = api_client_factory.build(PaymentInstructionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_payment_instruction(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the payment instruction. | [required] 
 **code** | **str**| The code of the payment instruction. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting the payment instruction |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_payment_instruction**
> PaymentInstruction getPaymentInstruction = get_payment_instruction(scope, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetPaymentInstruction: Get Payment Instruction

Retrieve a single Payment Instruction.

### Example

```python
api_instance = api_client_factory.build(PaymentInstructionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
property_keys = ['property_keys_example'] # List[str] (optional)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_payment_instruction(scope, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the payment instruction. | [required] 
 **code** | **str**| The code of the payment instruction. | [required] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the \&quot;PaymentInstruction\&quot; domain to decorate onto the              payment instruction. These take the format {domain}/{scope}/{code} e.g. \&quot;PaymentInstruction/myScope/myProperty\&quot;. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the payment instruction.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the payment instruction. Defaults to return the latest              version of the payment instruction if not specified. | [optional] 

### Return type

[**PaymentInstruction**](../model/PaymentInstruction.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested payment instruction |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_payment_instructions_by_payment_record_ids**
> GetPaymentInstructionsResponse getPaymentInstructionsByPaymentRecordIds = get_payment_instructions_by_payment_record_ids(request_body, property_keys=property_keys, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetPaymentInstructionsByPaymentRecordIds: Get Payment Instructions by Payment Record Ids

Retrieve the Payment Instructions that reference the given Payment Records. Payment record ids are unique  across the system scope, so no scope or identifier type is required. The response contains the payment  instructions that could be found, keyed by the payment record id used to retrieve them, along with the  nature of any failures.

### Example

```python
api_instance = api_client_factory.build(PaymentInstructionsApi)
request_body = ["payment-record-id-1","payment-record-id-2"] # List[str]
property_keys = ['property_keys_example'] # List[str] (optional)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_payment_instructions_by_payment_record_ids(request_body, property_keys=property_keys, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](../model/str.md)| A collection of payment record ids to retrieve payment instructions for.              Duplicate ids are ignored. | [required] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the \&quot;PaymentInstruction\&quot; domain to decorate onto each              payment instruction. These take the format {domain}/{scope}/{code} e.g. \&quot;PaymentInstruction/myScope/myProperty\&quot;. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the payment instructions.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the payment instructions. Defaults to return the latest              version of each payment instruction if not specified. | [optional] 

### Return type

[**GetPaymentInstructionsResponse**](../model/GetPaymentInstructionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payment instructions that could be found for the supplied payment record ids, along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_payment_instructions**
> PaymentInstructionsResponse upsertPaymentInstructions = upsert_payment_instructions(request_body)

[EXPERIMENTAL] UpsertPaymentInstructions: Upsert Payment Instructions

Create or update a collection of Payment Instructions.

### Example

```python
api_instance = api_client_factory.build(PaymentInstructionsApi)
request_body = {"paymentInstruction1":{"id":{"scope":"myScope","code":"paymentInstruction1"},"paymentRecordIds":[{"portfolioId":{"scope":"myScope","code":"myPortfolio"},"transactionId":"transaction1","paymentRecordId":"paymentRecord1"}],"currency":"GBP","totalPaymentAmount":1000.0,"paymentDate":"2024-01-01T00:00:00.0000000+00:00","payorPaymentDetailsReference":{"seriesScope":"myScope","applicableEntity":{"entityType":"Portfolio","entityScope":"myScope","identifierType":"code","identifierScope":"myScope","identifierValue":"LUID_00003D4Q"},"seriesIdentifiers":{"paymentType":"Dividend","currency":"GBP"},"effectiveDate":"2024-01-01T00:00:00.0000000+00:00","asAtDate":"2024-01-01T00:00:00.0000000+00:00"},"payeePaymentDetailsReference":{"seriesScope":"myScope","applicableEntity":{"entityType":"Portfolio","entityScope":"myScope","identifierType":"code","identifierScope":"myScope","identifierValue":"LUID_00003D4R"},"seriesIdentifiers":{"paymentType":"Dividend","currency":"GBP"},"effectiveDate":"2024-01-01T00:00:00.0000000+00:00","asAtDate":"2024-01-01T00:00:00.0000000+00:00"}}} # Dict[str, PaymentInstructionRequest]
api_response = api_instance.upsert_payment_instructions(request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, PaymentInstructionRequest]**](../model/PaymentInstructionRequest.md)| A collection of requests to create or update Payment Instructions. | [required] 

### Return type

[**PaymentInstructionsResponse**](../model/PaymentInstructionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The successfully created or updated payment instructions along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

