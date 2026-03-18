# InstrumentPaymentDiaryLeg

A leg containing a set of cashflows.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **leg_index** | **int** | Optional | Index (integer) for the leg of a payment diary. |
| **leg_id** | **str** | Optional | Identifier string for the leg of a payment diary. |
| **rows** | [List[InstrumentPaymentDiaryRow]](InstrumentPaymentDiaryRow.md) | Optional | List of individual cashflows within the payment diary. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentPaymentDiaryLeg import InstrumentPaymentDiaryLeg

instance = InstrumentPaymentDiaryLeg(
    leg_index=0,  # optional — Index (integer) for the leg of a payment diary.
    leg_id="...",  # optional — Identifier string for the leg of a payment diary.
    rows=[]  # optional — List of individual cashflows within the payment diary.
)
```

- [InstrumentPaymentDiaryRow](InstrumentPaymentDiaryRow.md) — used in `rows`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

