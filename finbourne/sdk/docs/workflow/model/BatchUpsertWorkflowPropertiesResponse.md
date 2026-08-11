# BatchUpsertWorkflowPropertiesResponse

The result of a batch upsert of properties on a Workflow.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The properties that were successfully upserted or deleted, keyed by property key. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The properties that could not be upserted or deleted, keyed by property key. |
| **as_at_date** | **datetime** | Optional | The asAt datetime at which the properties were updated or created. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.BatchUpsertWorkflowPropertiesResponse import BatchUpsertWorkflowPropertiesResponse

instance = BatchUpsertWorkflowPropertiesResponse(
    values=PerpetualProperty(...),  # optional — The properties that were successfully upserted or deleted, keyed by property key.
    failed=ErrorDetail(...),  # optional — The properties that could not be upserted or deleted, keyed by property key.
    as_at_date=datetime.now(),  # optional — The asAt datetime at which the properties were updated or created.
    links=[]  # optional
)
```


## Related Models

- [PerpetualProperty](PerpetualProperty.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

