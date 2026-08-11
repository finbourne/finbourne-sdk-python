# InstanceResponse

record containing details of a single instance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **UUID** | Required | *No description available.* |
| **name** | **str** | Required | *No description available.* |
| **enabled** | **bool** | Required | *No description available.* |
| **portfolios** | [List[TpfPortfolio]](TpfPortfolio.md) | Required | *No description available.* |
| **schedule** | **str** | Optional | *No description available.* |
| **schedule_timezone** | **str** | Optional | *No description available.* |
| **last_run_at** | **datetime** | Optional | *No description available.* |
| **last_run_status** | **str** | Optional | *No description available.* |
| **latest_runs_in24_hours** | **str** | Optional | *No description available.* |
| **destinations** | [List[InstanceDestinations]](InstanceDestinations.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.InstanceResponse import InstanceResponse

instance = InstanceResponse(
    id="...",  # required
    name="...",  # required
    enabled=True,  # required
    portfolios=[],  # required
    schedule="...",  # optional
    schedule_timezone="...",  # optional
    last_run_at=datetime.now(),  # optional
    last_run_status="...",  # optional
    latest_runs_in24_hours="...",  # optional
    destinations=[]  # required
)
```

- [TpfPortfolio](TpfPortfolio.md)
- [InstanceDestinations](InstanceDestinations.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

