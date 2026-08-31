# UnconfirmClosedPeriodRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **delete_subsequent_periods** | **bool** | Optional | Whether to delete every Closed Period that comes after the requested Closed Period on the Timeline. When false (the default) only the latest confirmed Closed Period may be unconfirmed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UnconfirmClosedPeriodRequest import UnconfirmClosedPeriodRequest

instance = UnconfirmClosedPeriodRequest(
    delete_subsequent_periods=True  # optional — Whether to delete every Closed Period that comes after the requested Closed Period on the Timeline. When false (the default) only the latest confirmed Closed Period may be unconfirmed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

