# WorkerConfiguration

Information about how the worker should be executed

## oneOf Type

`WorkerConfiguration` can be one of the following types:

* [Fail](./Fail.md)
* [GroupReconciliation](./GroupReconciliation.md)
* [HealthCheck](./HealthCheck.md)
* [LuminesceView](./LuminesceView.md)
* [LusidEntityDataQualityCheck](./LusidEntityDataQualityCheck.md)
* [SchedulerJob](./SchedulerJob.md)
* [Sleep](./Sleep.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.workflow.models.WorkerConfiguration import WorkerConfiguration

# Construct using any of the compatible types above
fail_instance = workflow.models.fail.Fail(
                        type = 'Fail', )

instance = WorkerConfiguration(fail_instance)
```

## Related Models

- [Fail](./Fail.md)
- [GroupReconciliation](./GroupReconciliation.md)
- [HealthCheck](./HealthCheck.md)
- [LuminesceView](./LuminesceView.md)
- [LusidEntityDataQualityCheck](./LusidEntityDataQualityCheck.md)
- [SchedulerJob](./SchedulerJob.md)
- [Sleep](./Sleep.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

