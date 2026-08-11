# QueryFundCashStatementParameters

Request body for querying a Fund Cash Statement.  Extends the diary entry query pattern with cash statement display mode.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start** | [DateOrDiaryEntry](DateOrDiaryEntry.md) | Optional | *No description available.* |
| **end** | [DateOrDiaryEntry](DateOrDiaryEntry.md) | Required | *No description available.* |
| **variant** | **str** | Optional | Optional diary entry variant (e.g. for multi-estimate scenarios). |
| **display_mode** | **str** | Optional | Cash statement display mode: ShowReversal (default) shows full reversal/TrueUp detail; Consolidated collapses reversals into AvgRateCorrection rows. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QueryFundCashStatementParameters import QueryFundCashStatementParameters

instance = QueryFundCashStatementParameters(
    start=DateOrDiaryEntry(...),  # optional
    end=DateOrDiaryEntry(...),  # required
    variant="...",  # optional — Optional diary entry variant (e.g. for multi-estimate scenarios).
    display_mode="..."  # optional — Cash statement display mode: ShowReversal (default) shows full reversal/TrueUp detail; Consolidated collapses reversals into AvgRateCorrection rows.
)
```


## Related Models

- [DateOrDiaryEntry](DateOrDiaryEntry.md)
- [DateOrDiaryEntry](DateOrDiaryEntry.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

