# AborRequest

The request used to create an Abor.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code given for the Abor. |
| **display_name** | **str** | Required | The name of the Abor. |
| **description** | **str** | Optional | The description for the Abor. |
| **portfolio_ids** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Required | The list with the portfolio ids which are part of the Abor. Note: These must all have the same base currency. |
| **abor_configuration_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Abor. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AborRequest import AborRequest

instance = AborRequest(
    code="...",  # required — The code given for the Abor.
    display_name="...",  # required — The name of the Abor.
    description="...",  # optional — The description for the Abor.
    portfolio_ids=[],  # required — The list with the portfolio ids which are part of the Abor. Note: These must all have the same base currency.
    abor_configuration_id=ResourceId(...),  # required
    properties=ModelProperty(...)  # optional — A set of properties for the Abor.
)
```

- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_ids`
- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

