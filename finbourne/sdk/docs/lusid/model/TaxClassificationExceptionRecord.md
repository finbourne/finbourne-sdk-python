# TaxClassificationExceptionRecord

An instrument the engine could not classify, or a qualifying-investments flip, for the exceptions feed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **luid** | **str** | Required | The LUSID instrument identifier of the instrument the exception was raised for. |
| **instrument_name** | **str** | Optional | The name of the instrument the exception was raised for. |
| **exception** | [TaxClassificationException](TaxClassificationException.md) | Required | *No description available.* |
| **effective_at** | **datetime** | Required | The effective date the exception was observed at. |
| **as_at** | **datetime** | Required | The asAt time the exception was observed at. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxClassificationExceptionRecord import TaxClassificationExceptionRecord

instance = TaxClassificationExceptionRecord(
    luid="...",  # required — The LUSID instrument identifier of the instrument the exception was raised for.
    instrument_name="...",  # optional — The name of the instrument the exception was raised for.
    exception=TaxClassificationException(...),  # required
    effective_at=datetime.now(),  # required — The effective date the exception was observed at.
    as_at=datetime.now()  # required — The asAt time the exception was observed at.
)
```

- [TaxClassificationException](TaxClassificationException.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

