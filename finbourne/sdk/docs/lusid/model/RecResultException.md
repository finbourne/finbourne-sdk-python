# RecResultException

The exception lifecycle of a rec result. Present only for exception result types  (Break, PartialMatch, PartialCross); null for Match and Cross.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Required | Whether the exception is Open or Closed. Available values: Open, Closed. |
| **closure_type** | **str** | Optional | How the exception was closed. Non-null only when status is Closed. Available values: Cleared, Accepted, ForceMatched. |
| **as_at_closed** | **datetime** | Optional | The asAt of the transaction that closed the exception. Non-null only when status is Closed. |
| **as_at_closure_invalidated** | **datetime** | Optional | First-failure bookmark: the asAt at which a judgement closure&#39;s validity condition first failed against the latest run&#39;s data. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultException import RecResultException

instance = RecResultException(
    status="...",  # required — Whether the exception is Open or Closed. Available values: Open, Closed.
    closure_type="...",  # optional — How the exception was closed. Non-null only when status is Closed. Available values: Cleared, Accepted, ForceMatched.
    as_at_closed=datetime.now(),  # optional — The asAt of the transaction that closed the exception. Non-null only when status is Closed.
    as_at_closure_invalidated=datetime.now()  # optional — First-failure bookmark: the asAt at which a judgement closure&#39;s validity condition first failed against the latest run&#39;s data.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

