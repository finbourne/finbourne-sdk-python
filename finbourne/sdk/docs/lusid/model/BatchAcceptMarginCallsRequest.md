# BatchAcceptMarginCallsRequest

Accepts several margin calls at their default agreed amounts, reporting the ones that could not be accepted.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **calls** | [List[MarginCallKey]](MarginCallKey.md) | Required | The calls to accept, each at its default agreed amount. A call that cannot be accepted is reported in failed and does not stop the others. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchAcceptMarginCallsRequest import BatchAcceptMarginCallsRequest

instance = BatchAcceptMarginCallsRequest(
    calls=[]  # required — The calls to accept, each at its default agreed amount. A call that cannot be accepted is reported in failed and does not stop the others.
)
```


## Related Models

- [MarginCallKey](MarginCallKey.md) — used in `calls`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

