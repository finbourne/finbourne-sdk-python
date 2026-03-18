# UpdateReferenceDataRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **request_definitions** | [List[FieldDefinition]](FieldDefinition.md) | Required | Definition of a reference data field. |
| **request_values** | [List[FieldValue]](FieldValue.md) | Required | Reference data. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateReferenceDataRequest import UpdateReferenceDataRequest

instance = UpdateReferenceDataRequest(
    request_definitions=[],  # required — Definition of a reference data field.
    request_values=[]  # required — Reference data.
)
```


## Related Models

- [FieldDefinition](FieldDefinition.md) — used in `request_definitions`
- [FieldValue](FieldValue.md) — used in `request_values`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

