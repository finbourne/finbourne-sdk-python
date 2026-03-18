# CustomSortBy

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **field_name** | **str** | Required | The name of the field to sort by. |
| **priority_values** | **List[str]** | Optional | An optional list of priority field values to sort by, in the order they should be prioritized. |
| **remainder_order** | **str** | Required | The sorting direction for the remaining field values. Either ascending (ASC) or descending (DESC). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomSortBy import CustomSortBy

instance = CustomSortBy(
    field_name="...",  # required — The name of the field to sort by.
    priority_values=,  # optional — An optional list of priority field values to sort by, in the order they should be prioritized.
    remainder_order="..."  # required — The sorting direction for the remaining field values. Either ascending (ASC) or descending (DESC).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

