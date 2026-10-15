# PartnerStatementLine

One figure on a partner statement.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The key of the figure. |
| **label** | **str** | Required | The label of the figure. |
| **amount** | **float** | Required | The amount of the figure. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerStatementLine import PartnerStatementLine

instance = PartnerStatementLine(
    key="...",  # required — The key of the figure.
    label="...",  # required — The label of the figure.
    amount=0.0  # required — The amount of the figure.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

