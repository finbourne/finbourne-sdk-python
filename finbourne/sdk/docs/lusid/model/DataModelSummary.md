# DataModelSummary

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the Custom Data Model. |
| **description** | **str** | Optional | A description for the Custom Data Model. |
| **entity_type** | **str** | Required | The entity type that the Custom Data Model binds to. |
| **type** | **str** | Required | Either Root or Leaf or Intermediate. |
| **precedence** | **int** | Required | Where in the hierarchy this model sits. |
| **parent** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **children** | [List[DataModelSummary]](DataModelSummary.md) | Required | Child Custom Data Models that will inherit from this data model. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DataModelSummary import DataModelSummary

instance = DataModelSummary(
    id=ResourceId(...),  # required
    display_name="...",  # required — The name of the Custom Data Model.
    description="...",  # optional — A description for the Custom Data Model.
    entity_type="...",  # required — The entity type that the Custom Data Model binds to.
    type="...",  # required — Either Root or Leaf or Intermediate.
    precedence=0,  # required — Where in the hierarchy this model sits.
    parent=ResourceId(...),  # optional
    children=[]  # required — Child Custom Data Models that will inherit from this data model.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [DataModelSummary](DataModelSummary.md) — used in `children`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

