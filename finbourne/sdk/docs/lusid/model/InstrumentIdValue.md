# InstrumentIdValue

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **str** | Required | The value of the identifier. |
| **effective_at** | **datetime** | Optional | The effective datetime from which the identifier will be valid. If left unspecified the default value is the beginning of time. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentIdValue import InstrumentIdValue

instance = InstrumentIdValue(
    value="...",  # required — The value of the identifier.
    effective_at=datetime.now()  # optional — The effective datetime from which the identifier will be valid. If left unspecified the default value is the beginning of time.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

