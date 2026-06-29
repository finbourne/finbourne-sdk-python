# AccountedQuote

The Valuation Point quote response for a Fund, including the origin of the quote relative to the Valuation Point period.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quote** | [Quote](Quote.md) | Optional | *No description available.* |
| **valuation_point_origin** | **str** | Optional | Designates if the quote was originally part of the Valuation Point or if it was added as part of a Complex Close action. Available values: None, Original, Added, OriginalAndAdded. |
| **added_origin_valuation_point_code** | **str** | Optional | The Valuation Point code, only for quotes added as part of a Complex Close action. |
| **added_origin_valuation_point_variant_code** | **str** | Optional | The Valuation Point variant code, only for quotes added as part of a Complex Close action. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AccountedQuote import AccountedQuote

instance = AccountedQuote(
    quote=Quote(...),  # optional
    valuation_point_origin="...",  # optional — Designates if the quote was originally part of the Valuation Point or if it was added as part of a Complex Close action. Available values: None, Original, Added, OriginalAndAdded.
    added_origin_valuation_point_code="...",  # optional — The Valuation Point code, only for quotes added as part of a Complex Close action.
    added_origin_valuation_point_variant_code="..."  # optional — The Valuation Point variant code, only for quotes added as part of a Complex Close action.
)
```


## Related Models

- [Quote](Quote.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

