# PackTransactionType

A transaction type carried by a partnership configuration pack.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The transaction type. |
| **description** | **str** | Optional | A description of the transaction type. |
| **debit_account** | **str** | Required | The account debited. |
| **credit_account** | **str** | Required | The account credited. |
| **direction** | **str** | Required | The direction of the capital movement from the partner&#39;s point of view. Available values: Inflow, Outflow, Neutral. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PackTransactionType import PackTransactionType

instance = PackTransactionType(
    type="...",  # required — The transaction type.
    description="...",  # optional — A description of the transaction type.
    debit_account="...",  # required — The account debited.
    credit_account="...",  # required — The account credited.
    direction="..."  # required — The direction of the capital movement from the partner&#39;s point of view. Available values: Inflow, Outflow, Neutral.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

