# Account

An account
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code given for the Account. |
| **description** | **str** | Optional | A description for the Account. |
| **type** | **str** | Required | The Account type. Can have the values: Asset/Liabilities/Income/Expense/Capital/Revenue. |
| **status** | **str** | Required | The Account status. Can be Active, Inactive or Deleted. The available values are: Active, Inactive, Deleted |
| **control** | **str** | Optional | This allows users to specify whether this a protected Account that prevents direct manual journal adjustment. Can have the values: System/ManualIt will default to “Manual”. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Account. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Account import Account

instance = Account(
    code="...",  # required — The code given for the Account.
    description="...",  # optional — A description for the Account.
    type="...",  # required — The Account type. Can have the values: Asset/Liabilities/Income/Expense/Capital/Revenue.
    status="...",  # required — The Account status. Can be Active, Inactive or Deleted. The available values are: Active, Inactive, Deleted
    control="...",  # optional — This allows users to specify whether this a protected Account that prevents direct manual journal adjustment. Can have the values: System/ManualIt will default to “Manual”.
    properties=ModelProperty(...)  # optional — A set of properties for the Account.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

