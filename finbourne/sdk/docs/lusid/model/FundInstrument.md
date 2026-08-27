# FundInstrument

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | Unique instrument identifiers. Must only point to the same instrument |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundInstrument import FundInstrument

instance = FundInstrument(
    instrument_identifiers=  # required — Unique instrument identifiers. Must only point to the same instrument
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

