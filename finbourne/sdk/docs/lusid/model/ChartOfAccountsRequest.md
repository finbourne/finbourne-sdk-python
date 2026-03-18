# ChartOfAccountsRequest

The request used to create a chart of account.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code given for the Chart of Accounts. |
| **display_name** | **str** | Optional | The name of the Chart of Account. |
| **description** | **str** | Optional | A description of the Chart of Accounts. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Chart of Accounts. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ChartOfAccountsRequest import ChartOfAccountsRequest

instance = ChartOfAccountsRequest(
    code="...",  # required — The code given for the Chart of Accounts.
    display_name="...",  # optional — The name of the Chart of Account.
    description="...",  # optional — A description of the Chart of Accounts.
    properties=ModelProperty(...)  # optional — A set of properties for the Chart of Accounts.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

