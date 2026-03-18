# ColumnStateType

Representation of a column within the grid
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **col_id** | **str** | Required | Unique identifier for the column |
| **hide** | **bool** | Required | Flag to determine whether the column is visible in the grid |
| **sort** | **str** | Optional | The sort order (asc or desc) |
| **sort_index** | **int** | Optional | The index of the sort to determine the order in which the sorts are applied |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ColumnStateType import ColumnStateType

instance = ColumnStateType(
    col_id="...",  # required — Unique identifier for the column
    hide=True,  # required — Flag to determine whether the column is visible in the grid
    sort="...",  # optional — The sort order (asc or desc)
    sort_index=0  # optional — The index of the sort to determine the order in which the sorts are applied
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

