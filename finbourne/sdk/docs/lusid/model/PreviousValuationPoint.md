# PreviousValuationPoint

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **valuation_point_code** | **str** | Required | The code of the Valuation Point. |
| **name** | **str** | Optional | Identifiable Name assigned to the Valuation Point. |
| **effective_at** | **datetime** | Required | The effective time of the Valuation Point. |
| **query_as_at** | **datetime** | Required | The AsAt time of the Valuation Point. This is the AsAt time that will be used when requests are made using the entry. |
| **holdings_as_at** | **datetime** | Optional | The AsAt time used for building holdings in the Valuation Point. |
| **valuation_as_at** | **datetime** | Optional | The AsAt time used for performing valuations in the Valuation Point. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PreviousValuationPoint import PreviousValuationPoint

instance = PreviousValuationPoint(
    valuation_point_code="...",  # required — The code of the Valuation Point.
    name="...",  # optional — Identifiable Name assigned to the Valuation Point.
    effective_at=datetime.now(),  # required — The effective time of the Valuation Point.
    query_as_at=datetime.now(),  # required — The AsAt time of the Valuation Point. This is the AsAt time that will be used when requests are made using the entry.
    holdings_as_at=datetime.now(),  # optional — The AsAt time used for building holdings in the Valuation Point.
    valuation_as_at=datetime.now()  # optional — The AsAt time used for performing valuations in the Valuation Point.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

