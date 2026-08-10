# ValuationPointResourceListOfAccountedComplexMarketData

ResourceList with extra header fields used by the various ValuationPoint endpoints for returning additional context related to the list of results.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_valuation_point** | [../model/DiaryEntry](DiaryEntry.md) | Optional | *No description available.* |
| **version** | [../model/Version](Version.md) | Required | *No description available.* |
| **values** | [../model/List[AccountedComplexMarketData]](AccountedComplexMarketData.md) | Required | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **next_page** | **str** | Optional | *No description available.* |
| **previous_page** | **str** | Optional | *No description available.* |
| **links** | [../model/List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ValuationPointResourceListOfAccountedComplexMarketData import ValuationPointResourceListOfAccountedComplexMarketData

instance = ValuationPointResourceListOfAccountedComplexMarketData(
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
- [AccountedComplexMarketData](AccountedComplexMarketData.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

