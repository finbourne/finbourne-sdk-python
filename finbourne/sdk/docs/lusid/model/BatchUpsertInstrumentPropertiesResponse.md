# BatchUpsertInstrumentPropertiesResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | **Dict[str, Optional[List[ModelProperty]]]** | Required | The properties that have been successfully upserted |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Required | The properties that could not be upserted along with a reason for their failure. |
| **as_at_date** | **datetime** | Required | The as-at datetime at which properties were created or updated. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchUpsertInstrumentPropertiesResponse import BatchUpsertInstrumentPropertiesResponse

instance = BatchUpsertInstrumentPropertiesResponse(
    values=,  # required — The properties that have been successfully upserted
    failed=ErrorDetail(...),  # required — The properties that could not be upserted along with a reason for their failure.
    as_at_date=datetime.now(),  # required — The as-at datetime at which properties were created or updated.
    links=[]  # optional
)
```

- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

