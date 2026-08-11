# ValuationPointDataQueryParameters

The parameters used in getting the ValuationPointData.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start** | [DateOrDiaryEntry](DateOrDiaryEntry.md) | Optional | *No description available.* |
| **end** | [DateOrDiaryEntry](DateOrDiaryEntry.md) | Required | *No description available.* |
| **variant** | **str** | Optional | Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ValuationPointDataQueryParameters import ValuationPointDataQueryParameters

instance = ValuationPointDataQueryParameters(
    start=DateOrDiaryEntry(...),  # optional
    end=DateOrDiaryEntry(...),  # required
    variant="..."  # optional — Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates.
)
```


## Related Models

- [DateOrDiaryEntry](DateOrDiaryEntry.md)
- [DateOrDiaryEntry](DateOrDiaryEntry.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

