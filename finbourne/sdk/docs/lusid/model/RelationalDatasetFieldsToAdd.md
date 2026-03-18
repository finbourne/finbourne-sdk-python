# RelationalDatasetFieldsToAdd

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **series_identifiers** | [List[CreateSeriesIdentifierField]](CreateSeriesIdentifierField.md) | Optional | The schema defining the structure and data types of the relational dataset. |
| **value_and_metadata_fields** | [List[RelationalDatasetFieldDefinition]](RelationalDatasetFieldDefinition.md) | Optional | The schema defining the structure and data types of the relational dataset. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RelationalDatasetFieldsToAdd import RelationalDatasetFieldsToAdd

instance = RelationalDatasetFieldsToAdd(
    series_identifiers=[],  # optional — The schema defining the structure and data types of the relational dataset.
    value_and_metadata_fields=[]  # optional — The schema defining the structure and data types of the relational dataset.
)
```


## Related Models

- [CreateSeriesIdentifierField](CreateSeriesIdentifierField.md) — used in `series_identifiers`
- [RelationalDatasetFieldDefinition](RelationalDatasetFieldDefinition.md) — used in `value_and_metadata_fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

