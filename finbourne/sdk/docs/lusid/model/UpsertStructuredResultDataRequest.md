# UpsertStructuredResultDataRequest

The details of the structured unit result data item to upsert into Lusid.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [../model/StructuredResultDataId](StructuredResultDataId.md) | Required | *No description available.* |
| **data** | [../model/StructuredResultData](StructuredResultData.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertStructuredResultDataRequest import UpsertStructuredResultDataRequest

instance = UpsertStructuredResultDataRequest(
    id=StructuredResultDataId(...),  # required
    data=StructuredResultData(...)  # optional
)
```


## Related Models

- [StructuredResultDataId](StructuredResultDataId.md)
- [StructuredResultData](StructuredResultData.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

