# PartnerAllocation

One partner's share of an allocation pool.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The investor record the allocation belongs to. |
| **basis_weight** | **float** | Required | The partner&#39;s weight in the pool&#39;s basis. |
| **amount** | **float** | Required | The amount allocated to the partner. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerAllocation import PartnerAllocation

instance = PartnerAllocation(
    investor_record_id="...",  # required — The investor record the allocation belongs to.
    basis_weight=0.0,  # required — The partner&#39;s weight in the pool&#39;s basis.
    amount=0.0  # required — The amount allocated to the partner.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

