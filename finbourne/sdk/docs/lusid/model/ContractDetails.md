# ContractDetails

Set of identifiers of an existing FlexibleLoan contract.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifiers** | **Dict[str, Optional[str]]** | Required | Unique instrument identifiers. |
| **lusid_instrument_id** | **str** | Optional | LUSID&#39;s internal unique instrument identifier - readonly field, resolved from the instrument identifiers. *(read-only)* |
| **instrument_scope** | **str** | Optional | The scope in which the FlexibleLoan instrument lies - readonly field, resolved from the instrument identifiers. *(read-only)* |
| **instrument_name** | **str** | Optional | The name of the FlexibleLoan instrument - readonly field, resolved from the instrument identifiers. *(read-only)* |
| **dom_ccy** | **str** | Optional | The domestic currency of the instrument - readonly field, resolved from the instrument identifiers. *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ContractDetails import ContractDetails

instance = ContractDetails(
    identifiers=,  # required — Unique instrument identifiers.
    lusid_instrument_id="...",  # optional — LUSID&#39;s internal unique instrument identifier - readonly field, resolved from the instrument identifiers.
    instrument_scope="...",  # optional — The scope in which the FlexibleLoan instrument lies - readonly field, resolved from the instrument identifiers.
    instrument_name="...",  # optional — The name of the FlexibleLoan instrument - readonly field, resolved from the instrument identifiers.
    dom_ccy="..."  # optional — The domestic currency of the instrument - readonly field, resolved from the instrument identifiers.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

