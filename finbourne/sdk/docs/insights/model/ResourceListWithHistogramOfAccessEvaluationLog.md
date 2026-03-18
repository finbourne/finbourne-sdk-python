# ResourceListWithHistogramOfAccessEvaluationLog

ResourceList with additional aggregation data about the values.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **histogram** | [Histogram](Histogram.md) | Optional | *No description available.* |
| **values** | [List[AccessEvaluationLog]](AccessEvaluationLog.md) | Required | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **next_page** | **str** | Optional | *No description available.* |
| **previous_page** | **str** | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.ResourceListWithHistogramOfAccessEvaluationLog import ResourceListWithHistogramOfAccessEvaluationLog

instance = ResourceListWithHistogramOfAccessEvaluationLog(
    histogram=Histogram(...),  # optional
    values=[],  # required
    href="...",  # optional
    next_page="...",  # optional
    previous_page="...",  # optional
    links=[]  # optional
)
```


## Related Models

- [Histogram](Histogram.md)
- [AccessEvaluationLog](AccessEvaluationLog.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

