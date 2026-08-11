# SingleValuationPointQueryParameters

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **date_or_diary_entry** | [DateOrDiaryEntry](DateOrDiaryEntry.md) | Required | *No description available.* |
| **variant** | **str** | Optional | Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SingleValuationPointQueryParameters import SingleValuationPointQueryParameters

instance = SingleValuationPointQueryParameters(
    date_or_diary_entry=DateOrDiaryEntry(...),  # required
    variant="..."  # optional — Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates.
)
```


## Related Models

- [DateOrDiaryEntry](DateOrDiaryEntry.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

