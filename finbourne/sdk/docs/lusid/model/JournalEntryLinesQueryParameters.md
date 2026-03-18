# JournalEntryLinesQueryParameters

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start** | [DateOrDiaryEntry](DateOrDiaryEntry.md) | Optional | *No description available.* |
| **end** | [DateOrDiaryEntry](DateOrDiaryEntry.md) | Optional | *No description available.* |
| **variant** | **str** | Optional | Unique Variant for the given Valuation points. If not provided, defaults to empty string. |
| **date_mode** | **str** | Optional | The mode of calculation of the journal entry lines. The available values are: ActivityDate, AccountingDate. |
| **general_ledger_profile_code** | **str** | Optional | The optional code of a general ledger profile used to decorate journal entry lines with levels. |
| **property_keys** | **List[str]** | Optional | A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39; domain to decorate onto the journal entry lines. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.JournalEntryLinesQueryParameters import JournalEntryLinesQueryParameters

instance = JournalEntryLinesQueryParameters(
    start=DateOrDiaryEntry(...),  # optional
    end=DateOrDiaryEntry(...),  # optional
    variant="...",  # optional — Unique Variant for the given Valuation points. If not provided, defaults to empty string.
    date_mode="...",  # optional — The mode of calculation of the journal entry lines. The available values are: ActivityDate, AccountingDate.
    general_ledger_profile_code="...",  # optional — The optional code of a general ledger profile used to decorate journal entry lines with levels.
    property_keys=  # optional — A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39; domain to decorate onto the journal entry lines.
)
```


## Related Models

- [DateOrDiaryEntry](DateOrDiaryEntry.md)
- [DateOrDiaryEntry](DateOrDiaryEntry.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

