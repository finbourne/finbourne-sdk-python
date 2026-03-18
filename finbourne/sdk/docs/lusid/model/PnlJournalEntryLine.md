# PnlJournalEntryLine

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **pnl_bucket** | **str** | Optional | The Filter ID of the grouping used from the Fund Configuration PnL filters |
| **journal_entry_line** | [JournalEntryLine](JournalEntryLine.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PnlJournalEntryLine import PnlJournalEntryLine

instance = PnlJournalEntryLine(
    pnl_bucket="...",  # optional — The Filter ID of the grouping used from the Fund Configuration PnL filters
    journal_entry_line=JournalEntryLine(...),  # optional
    links=[]  # optional
)
```

- [JournalEntryLine](JournalEntryLine.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

