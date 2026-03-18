# UpsertResultValuesDataRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **document_id** | [StructuredResultDataId](StructuredResultDataId.md) | Required | *No description available.* |
| **key** | **Dict[str, Optional[str]]** | Optional | The structured unit result data key. |
| **data_address** | **str** | Optional | The address of the piece of unit result data |
| **result_value** | [ResultValue](ResultValue.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertResultValuesDataRequest import UpsertResultValuesDataRequest

instance = UpsertResultValuesDataRequest(
    document_id=StructuredResultDataId(...),  # required
    key=,  # optional — The structured unit result data key.
    data_address="...",  # optional — The address of the piece of unit result data
    result_value=ResultValue(...)  # optional
)
```


## Related Models

- [StructuredResultDataId](StructuredResultDataId.md)
- [ResultValue](ResultValue.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

