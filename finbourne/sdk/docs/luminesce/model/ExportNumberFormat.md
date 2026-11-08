# ExportNumberFormat

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **min_decimals** | **int** | Optional | *No description available.* |
| **max_decimals** | **int** | Optional | *No description available.* |
| **thousand_separator** | **bool** | Optional | *No description available.* |
| **display_as_percentage** | **bool** | Optional | *No description available.* |
| **negative_number_format** | [ExportNegativeNumberFormat](ExportNegativeNumberFormat.md) | Optional | *No description available.* |
| **excel_format** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ExportNumberFormat import ExportNumberFormat

instance = ExportNumberFormat(
    min_decimals=0,  # optional
    max_decimals=0,  # optional
    thousand_separator=True,  # optional
    display_as_percentage=True,  # optional
    negative_number_format=ExportNegativeNumberFormat(...),  # optional
    excel_format="..."  # optional
)
```

- [ExportNegativeNumberFormat](ExportNegativeNumberFormat.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

