# Quote

The quote id, value and lineage of the quotes all keyed by a unique correlation id.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quote_id** | [QuoteId](QuoteId.md) | Required | *No description available.* |
| **metric_value** | [MetricValue](MetricValue.md) | Optional | *No description available.* |
| **lineage** | **str** | Optional | Description of the quote&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. |
| **cut_label** | **str** | Optional | The cut label that this quote was updated or inserted with. |
| **uploaded_by** | **str** | Required | The unique id of the user that updated or inserted the quote. |
| **as_at** | **datetime** | Required | The asAt datetime at which the quote was committed to LUSID. |
| **scale_factor** | **float** | Optional | An optional scale factor for non-standard scaling of quotes against the instrument. For example, if you wish the quote&#39;s Value to be scaled down by a factor of 100, enter 100. If not supplied, the default ScaleFactor is 1. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Quote import Quote

instance = Quote(
    quote_id=QuoteId(...),  # required
    metric_value=MetricValue(...),  # optional
    lineage="...",  # optional — Description of the quote&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;.
    cut_label="...",  # optional — The cut label that this quote was updated or inserted with.
    uploaded_by="...",  # required — The unique id of the user that updated or inserted the quote.
    as_at=datetime.now(),  # required — The asAt datetime at which the quote was committed to LUSID.
    scale_factor=0.0  # optional — An optional scale factor for non-standard scaling of quotes against the instrument. For example, if you wish the quote&#39;s Value to be scaled down by a factor of 100, enter 100. If not supplied, the default ScaleFactor is 1.
)
```


## Related Models

- [QuoteId](QuoteId.md)
- [MetricValue](MetricValue.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

