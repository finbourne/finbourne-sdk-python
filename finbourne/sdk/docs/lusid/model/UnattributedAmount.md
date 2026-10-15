# UnattributedAmount

An amount on the income summary an allocation run could not attribute to any pool.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **gl_code** | **str** | Required | The general ledger account the unattributed amount sits in. |
| **amount** | **float** | Required | The amount allocated to the partner. |
| **reason** | **str** | Required | Why the amount could not be attributed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UnattributedAmount import UnattributedAmount

instance = UnattributedAmount(
    gl_code="...",  # required — The general ledger account the unattributed amount sits in.
    amount=0.0,  # required — The amount allocated to the partner.
    reason="..."  # required — Why the amount could not be attributed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

