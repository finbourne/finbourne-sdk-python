# AllocationEventNoticeCumulative

Cumulative balances to date for a partner on a notice.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **contributions** | **float** | Required | Cumulative contributions after the event. |
| **distributions** | **float** | Required | Cumulative distributions after the event. |
| **recallable** | **float** | Required | Cumulative recallable distributions after the event. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventNoticeCumulative import AllocationEventNoticeCumulative

instance = AllocationEventNoticeCumulative(
    contributions=0.0,  # required — Cumulative contributions after the event.
    distributions=0.0,  # required — Cumulative distributions after the event.
    recallable=0.0  # required — Cumulative recallable distributions after the event.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

