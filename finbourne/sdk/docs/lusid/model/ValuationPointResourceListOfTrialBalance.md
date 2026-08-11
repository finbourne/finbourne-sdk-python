# ValuationPointResourceListOfTrialBalance

ResourceList with extra header fields used by the various ValuationPoint endpoints for returning additional context related to the list of results.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_valuation_point** | [DiaryEntry](DiaryEntry.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Required | *No description available.* |
| **values** | [List[TrialBalance]](TrialBalance.md) | Required | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **next_page** | **str** | Optional | *No description available.* |
| **previous_page** | **str** | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ValuationPointResourceListOfTrialBalance import ValuationPointResourceListOfTrialBalance

instance = ValuationPointResourceListOfTrialBalance(
    start_valuation_point=DiaryEntry(...),  # optional
    version=Version(...),  # required
    values=[],  # required
    href="...",  # optional
    next_page="...",  # optional
    previous_page="...",  # optional
    links=[]  # optional
)
```


## Related Models

- [DiaryEntry](DiaryEntry.md)
- [Version](Version.md)
- [TrialBalance](TrialBalance.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

