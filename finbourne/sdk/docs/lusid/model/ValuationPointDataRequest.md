# ValuationPointDataRequest

The ValuationPointDataRequest.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **diary_entry_code** | **str** | Required | Unique code for the Valuation Point. |
| **diary_entry_variant** | **str** | Optional | Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ValuationPointDataRequest import ValuationPointDataRequest

instance = ValuationPointDataRequest(
    diary_entry_code="...",  # required — Unique code for the Valuation Point.
    diary_entry_variant="..."  # optional — Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

