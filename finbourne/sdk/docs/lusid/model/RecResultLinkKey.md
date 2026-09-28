# RecResultLinkKey

One item pairing that established a link between two rec results: the identifiers both results' items carried.  Exactly one of holdingId and transactionId is populated; taxLotId only ever accompanies a holdingId, and only  where the pairing was established at tax-lot precision.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **holding_id** | **str** | Optional | The holding both items carried, for a holding-keyed pairing. Null for a transaction-keyed one. |
| **tax_lot_id** | **str** | Optional | The tax lot both items carried within the holding, where the pairing was established at tax-lot precision. Null where it was established at holding precision, and always null for a transaction-keyed pairing. |
| **transaction_id** | **str** | Optional | The transaction both items carried, for a transaction-keyed pairing. Null for a holding-keyed one. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultLinkKey import RecResultLinkKey

instance = RecResultLinkKey(
    holding_id="...",  # optional — The holding both items carried, for a holding-keyed pairing. Null for a transaction-keyed one.
    tax_lot_id="...",  # optional — The tax lot both items carried within the holding, where the pairing was established at tax-lot precision. Null where it was established at holding precision, and always null for a transaction-keyed pairing.
    transaction_id="..."  # optional — The transaction both items carried, for a transaction-keyed pairing. Null for a holding-keyed one.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

