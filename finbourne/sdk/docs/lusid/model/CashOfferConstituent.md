# CashOfferConstituent

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **offer_price** | **float** | Required | *No description available.* |
| **currency** | **str** | Required | *No description available.* |
| **settlement_date** | **datetime** | Required | *No description available.* |
| **min_piece_size** | **float** | Optional | *No description available.* |
| **min_increment** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CashOfferConstituent import CashOfferConstituent

instance = CashOfferConstituent(
    offer_price=0.0,  # required
    currency="...",  # required
    settlement_date=datetime.now(),  # required
    min_piece_size=0.0,  # optional
    min_increment=0.0  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

