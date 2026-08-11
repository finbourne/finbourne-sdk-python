# ResourceListWithHistogramOfVendorLog

ResourceList with additional aggregation data about the values.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **histogram** | [Histogram](Histogram.md) | Optional | *No description available.* |
| **values** | [List[VendorLog]](VendorLog.md) | Required | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **next_page** | **str** | Optional | *No description available.* |
| **previous_page** | **str** | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.ResourceListWithHistogramOfVendorLog import ResourceListWithHistogramOfVendorLog

instance = ResourceListWithHistogramOfVendorLog(
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
- [VendorLog](VendorLog.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

