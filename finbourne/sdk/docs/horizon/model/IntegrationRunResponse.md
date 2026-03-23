# IntegrationRunResponse

Integration run response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **UUID** | Required |  |
| **ref_run_id** | **UUID** | Optional |  |
| **attempt** | **int** | Required |  |
| **instance_id** | **UUID** | Optional | *No description available.* |
| **instance_name** | **str** | Optional | *No description available.* |
| **status** | **str** | Optional |  |
| **message** | **str** | Optional |  |
| **integration** | [IntegrationRunIntegration](IntegrationRunIntegration.md) | Required | *No description available.* |
| **version** | [IntegrationRunVersion](IntegrationRunVersion.md) | Required | *No description available.* |
| **integration_logs** | **Dict[str, Dict[str, IntegrationRunLog]]** | Optional |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.IntegrationRunResponse import IntegrationRunResponse

instance = IntegrationRunResponse(
    run_id="...",  # required — 
    ref_run_id="...",  # optional — 
    attempt=0,  # required — 
    instance_id="...",  # optional
    instance_name="...",  # optional
    status="...",  # optional — 
    message="...",  # optional — 
    integration=IntegrationRunIntegration(...),  # required
    version=IntegrationRunVersion(...),  # required
    integration_logs=  # optional — 
)
```

- [IntegrationRunIntegration](IntegrationRunIntegration.md)
- [IntegrationRunVersion](IntegrationRunVersion.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

