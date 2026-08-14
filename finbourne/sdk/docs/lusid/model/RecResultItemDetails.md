# RecResultItemDetails

The individual items that make up a rec result, split by side. Zero counts and empty arrays for  results that have cleared.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **count_left** | **int** | Required | The number of items grouped on the left side. |
| **count_right** | **int** | Required | The number of items grouped on the right side. |
| **left** | [List[RecResultItem]](RecResultItem.md) | Optional | The left-side items. |
| **right** | [List[RecResultItem]](RecResultItem.md) | Optional | The right-side items. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultItemDetails import RecResultItemDetails

instance = RecResultItemDetails(
    count_left=0,  # required — The number of items grouped on the left side.
    count_right=0,  # required — The number of items grouped on the right side.
    left=[],  # optional — The left-side items.
    right=[]  # optional — The right-side items.
)
```

- [RecResultItem](RecResultItem.md) — used in `left`
- [RecResultItem](RecResultItem.md) — used in `right`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

