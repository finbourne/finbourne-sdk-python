# BatchUpsertPropertyDefinitionPropertiesResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [../model/Dict[str, ModelProperty]](ModelProperty.md) | Required | The properties that have been successfully upserted |
| **failed** | [../model/Dict[str, ErrorDetail]](ErrorDetail.md) | Required | The properties that could not be upserted along with a reason for their failure. |
| **as_at_date** | **datetime** | Required | The as-at datetime at which properties were created or updated. |
| **links** | [../model/List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchUpsertPropertyDefinitionPropertiesResponse import BatchUpsertPropertyDefinitionPropertiesResponse

instance = BatchUpsertPropertyDefinitionPropertiesResponse(
    values=ModelProperty(...),  # required — The properties that have been successfully upserted
    failed=ErrorDetail(...),  # required — The properties that could not be upserted along with a reason for their failure.
    as_at_date=datetime.now(),  # required — The as-at datetime at which properties were created or updated.
    links=[]  # optional
)
```


## Related Models

- [ModelProperty](ModelProperty.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

