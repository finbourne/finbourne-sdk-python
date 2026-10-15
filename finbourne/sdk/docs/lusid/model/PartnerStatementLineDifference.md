# PartnerStatementLineDifference

One figure that differs between two partner statements.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The key of the figure. |
| **before** | **float** | Optional | The figure on the statement compared against. |
| **after** | **float** | Optional | The figure on this statement. |
| **change** | **float** | Required | After less before. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerStatementLineDifference import PartnerStatementLineDifference

instance = PartnerStatementLineDifference(
    key="...",  # required — The key of the figure.
    before=0.0,  # optional — The figure on the statement compared against.
    after=0.0,  # optional — The figure on this statement.
    change=0.0  # required — After less before.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

