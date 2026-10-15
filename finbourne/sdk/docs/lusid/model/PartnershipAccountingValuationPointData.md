# PartnershipAccountingValuationPointData

The partnership accounting view of a valuation point: what is left on the income summary to allocate to the  partners, and the configuration pack the allocation books under.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **unallocated_income_summary** | **float** | Required | The balance on the income summary account over the valuation point&#39;s period that has not yet been allocated to the partners. Must be zero before the valuation point can be finalised. |
| **config_pack_scope** | **str** | Required | The scope of the configuration pack. |
| **config_pack_code** | **str** | Required | The code of the configuration pack. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnershipAccountingValuationPointData import PartnershipAccountingValuationPointData

instance = PartnershipAccountingValuationPointData(
    unallocated_income_summary=0.0,  # required — The balance on the income summary account over the valuation point&#39;s period that has not yet been allocated to the partners. Must be zero before the valuation point can be finalised.
    config_pack_scope="...",  # required — The scope of the configuration pack.
    config_pack_code="..."  # required — The code of the configuration pack.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

