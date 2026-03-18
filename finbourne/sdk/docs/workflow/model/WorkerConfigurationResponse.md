# WorkerConfigurationResponse

Readonly information about how the worker should be executed

## oneOf Type

`WorkerConfigurationResponse` can be one of the following types:

* [FailResponse](./FailResponse.md)
* [GroupReconciliationResponse](./GroupReconciliationResponse.md)
* [HealthCheckResponse](./HealthCheckResponse.md)
* [LibraryResponse](./LibraryResponse.md)
* [LuminesceViewResponse](./LuminesceViewResponse.md)
* [LusidEntityDataQualityCheckResponse](./LusidEntityDataQualityCheckResponse.md)
* [SchedulerJobResponse](./SchedulerJobResponse.md)
* [SleepResponse](./SleepResponse.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.workflow.models.WorkerConfigurationResponse import WorkerConfigurationResponse

# Construct using any of the compatible types above
fail_response_instance = workflow.models.fail_response.FailResponse(
                        type = 'Fail', )

instance = WorkerConfigurationResponse(fail_response_instance)
```

## Related Models

- [FailResponse](./FailResponse.md)
- [GroupReconciliationResponse](./GroupReconciliationResponse.md)
- [HealthCheckResponse](./HealthCheckResponse.md)
- [LibraryResponse](./LibraryResponse.md)
- [LuminesceViewResponse](./LuminesceViewResponse.md)
- [LusidEntityDataQualityCheckResponse](./LusidEntityDataQualityCheckResponse.md)
- [SchedulerJobResponse](./SchedulerJobResponse.md)
- [SleepResponse](./SleepResponse.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

