# RelativeBoundary

One end of a relative time range. Exactly one of the options must be set: Finbourne.Insights.WebApi.Dtos.Querying.RelativeBoundary.Now (the current instant), Finbourne.Insights.WebApi.Dtos.Querying.RelativeBoundary.Midnight (the start of the current day in the range's time zone), Finbourne.Insights.WebApi.Dtos.Querying.RelativeBoundary.Offset (a duration back from now) or Finbourne.Insights.WebApi.Dtos.Querying.RelativeBoundary.Absolute (an explicit instant).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **now** | **bool** | Optional | When &#x60;true&#x60;, this boundary is the current instant (\&quot;now\&quot;). |
| **midnight** | **bool** | Optional | When &#x60;true&#x60;, this boundary is the start of the current day (midnight) in the range&#39;s time zone. |
| **offset** | [RelativeOffset](RelativeOffset.md) | Optional | *No description available.* |
| **absolute** | **datetime** | Optional | An explicit absolute instant. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.RelativeBoundary import RelativeBoundary

instance = RelativeBoundary(
    now=True,  # optional — When &#x60;true&#x60;, this boundary is the current instant (\&quot;now\&quot;).
    midnight=True,  # optional — When &#x60;true&#x60;, this boundary is the start of the current day (midnight) in the range&#39;s time zone.
    offset=RelativeOffset(...),  # optional
    absolute=datetime.now()  # optional — An explicit absolute instant.
)
```

- [RelativeOffset](RelativeOffset.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

