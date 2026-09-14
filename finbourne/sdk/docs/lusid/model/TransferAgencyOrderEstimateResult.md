# TransferAgencyOrderEstimateResult

The estimated values for one order, together with the market facts they were struck from. The market facts  are repeated on every order priced against the same share class so that each result stands alone.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **order_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **most_recent_valuation_date** | **datetime** | Optional | *No description available.* |
| **price_per_share** | **float** | Optional | *No description available.* |
| **price_currency** | **str** | Optional | *No description available.* |
| **estimated_units** | **float** | Optional | *No description available.* |
| **estimated_amount** | **float** | Optional | *No description available.* |
| **estimated_amount_currency** | **str** | Optional | *No description available.* |
| **fx_rate_used** | **float** | Optional | *No description available.* |
| **excluded_orders** | [List[TransferAgencyExcludedOrder]](TransferAgencyExcludedOrder.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransferAgencyOrderEstimateResult import TransferAgencyOrderEstimateResult

instance = TransferAgencyOrderEstimateResult(
    order_id=ResourceId(...),  # optional
    most_recent_valuation_date=datetime.now(),  # optional
    price_per_share=0.0,  # optional
    price_currency="...",  # optional
    estimated_units=0.0,  # optional
    estimated_amount=0.0,  # optional
    estimated_amount_currency="...",  # optional
    fx_rate_used=0.0,  # optional
    excluded_orders=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TransferAgencyExcludedOrder](TransferAgencyExcludedOrder.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

