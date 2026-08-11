# CreateReferencePortfolioRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The name of the reference portfolio. |
| **description** | **str** | Optional | A long form text description of the portfolio. |
| **code** | **str** | Required | Unique identifier for the portfolio. |
| **created** | **datetime** | Optional | The original creation date, defaults to today if not specified when creating a portfolio. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Portfolio properties to add to the portfolio. |
| **instrument_scopes** | **List[str]** | Optional | Instrument Scopes. |
| **base_currency** | **str** | Optional | The base currency of the transaction portfolio in ISO 4217 currency code format. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateReferencePortfolioRequest import CreateReferencePortfolioRequest

instance = CreateReferencePortfolioRequest(
    display_name="...",  # required — The name of the reference portfolio.
    description="...",  # optional — A long form text description of the portfolio.
    code="...",  # required — Unique identifier for the portfolio.
    created=datetime.now(),  # optional — The original creation date, defaults to today if not specified when creating a portfolio.
    properties=ModelProperty(...),  # optional — Portfolio properties to add to the portfolio.
    instrument_scopes=,  # optional — Instrument Scopes.
    base_currency="..."  # optional — The base currency of the transaction portfolio in ISO 4217 currency code format.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

