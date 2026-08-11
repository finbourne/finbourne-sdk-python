# IntellisenseItem

Representation of an item in an Intellisense popup
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **caption** | **str** | Required | The value to show the user in the popup |
| **value** | **str** | Required | The value to substitute in |
| **meta** | **str** | Optional | The light-grey text shown to the right of the Caption in the popup |
| **score** | **int** | Optional | How important is this.  Bigger is more important. |
| **doc_html** | **str** | Optional | Popup further info (as in a whole documentation article!) |
| **type** | [IntellisenseType](IntellisenseType.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.IntellisenseItem import IntellisenseItem

instance = IntellisenseItem(
    caption="...",  # required — The value to show the user in the popup
    value="...",  # required — The value to substitute in
    meta="...",  # optional — The light-grey text shown to the right of the Caption in the popup
    score=0,  # optional — How important is this.  Bigger is more important.
    doc_html="...",  # optional — Popup further info (as in a whole documentation article!)
    type=IntellisenseType(...)  # optional
)
```

- [IntellisenseType](IntellisenseType.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

