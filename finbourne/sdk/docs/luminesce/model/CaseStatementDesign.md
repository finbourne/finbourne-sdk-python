# CaseStatementDesign

Representation of the selected field and a list of: filter, source, and target.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **selected_field** | **str** | Optional | Selected field in the SQL query. |
| **case_statement_items** | [List[CaseStatementItem]](CaseStatementItem.md) | Optional | A list containing the filter, source, and target. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.CaseStatementDesign import CaseStatementDesign

instance = CaseStatementDesign(
    selected_field="...",  # optional — Selected field in the SQL query.
    case_statement_items=[]  # optional — A list containing the filter, source, and target.
)
```

- [CaseStatementItem](CaseStatementItem.md) — used in `case_statement_items`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

