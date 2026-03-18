# Lineage

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | *No description available.* |
| **subtype** | **str** | Optional | *No description available.* |
| **legend_text** | **str** | Optional | *No description available.* |
| **alias** | **str** | Optional | *No description available.* |
| **column_title_tooltip** | **str** | Optional | *No description available.* |
| **column_title_icon** | [LineageColumnIcon](LineageColumnIcon.md) | Optional | *No description available.* |
| **explain_title** | **str** | Optional | *No description available.* |
| **explain_tooltip** | **str** | Optional | *No description available.* |
| **arrow_to_parent_tooltip** | **str** | Optional | *No description available.* |
| **full_formula** | **str** | Optional | *No description available.* |
| **documentation_as_html** | **str** | Optional | *No description available.* |
| **documentation_as_mark_down** | **str** | Optional | *No description available.* |
| **children** | [List[Lineage]](Lineage.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.Lineage import Lineage

instance = Lineage(
    type="...",  # optional
    subtype="...",  # optional
    legend_text="...",  # optional
    alias="...",  # optional
    column_title_tooltip="...",  # optional
    column_title_icon=LineageColumnIcon(...),  # optional
    explain_title="...",  # optional
    explain_tooltip="...",  # optional
    arrow_to_parent_tooltip="...",  # optional
    full_formula="...",  # optional
    documentation_as_html="...",  # optional
    documentation_as_mark_down="...",  # optional
    children=[]  # optional
)
```

- [LineageColumnIcon](LineageColumnIcon.md)
- [Lineage](Lineage.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

