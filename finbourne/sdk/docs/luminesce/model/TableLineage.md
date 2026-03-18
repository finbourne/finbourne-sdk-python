# TableLineage

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **column_lineage** | [List[Lineage]](Lineage.md) | Optional | *No description available.* |
| **whole_table_lineage** | [Lineage](Lineage.md) | Optional | *No description available.* |
| **failure_reason** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.TableLineage import TableLineage

instance = TableLineage(
    column_lineage=[],  # optional
    whole_table_lineage=Lineage(...),  # optional
    failure_reason="..."  # optional
)
```


## Related Models

- [Lineage](Lineage.md)
- [Lineage](Lineage.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

