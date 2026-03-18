# QuoteId

The unique identifier of the quote.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quote_series_id** | [QuoteSeriesId](QuoteSeriesId.md) | Required | *No description available.* |
| **effective_at** | **str** | Required | The effective datetime or cut label at which the quote is valid from. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QuoteId import QuoteId

instance = QuoteId(
    quote_series_id=QuoteSeriesId(...),  # required
    effective_at="..."  # required — The effective datetime or cut label at which the quote is valid from.
)
```


## Related Models

- [QuoteSeriesId](QuoteSeriesId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

