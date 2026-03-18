# JournalEntryLineShareClassBreakdown

The apportionment from overall fund level journal entry Line to the share class.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **short_code** | **str** | Optional | The share class identifier. |
| **apportionment_factor** | **float** | Optional | The share class apportionment factor (capital ratio). |
| **local_value** | **float** | Optional | This journal entry line&#39;s local value amount after apportionment is applied. |
| **base_value** | **float** | Optional | This journal entry line&#39;s base value amount after apportionment is applied |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.JournalEntryLineShareClassBreakdown import JournalEntryLineShareClassBreakdown

instance = JournalEntryLineShareClassBreakdown(
    short_code="...",  # optional — The share class identifier.
    apportionment_factor=0.0,  # optional — The share class apportionment factor (capital ratio).
    local_value=0.0,  # optional — This journal entry line&#39;s local value amount after apportionment is applied.
    base_value=0.0  # optional — This journal entry line&#39;s base value amount after apportionment is applied
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

