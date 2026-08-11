# AcceptEstimateValuationPointResponse

The Valuation Point Data Response for AcceptEstimate called on the Fund and specified date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **candidate_valuation_point** | [ValuationPointDataResponse](ValuationPointDataResponse.md) | Required | *No description available.* |
| **latest_valuation_point** | [ValuationPointDataResponse](ValuationPointDataResponse.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AcceptEstimateValuationPointResponse import AcceptEstimateValuationPointResponse

instance = AcceptEstimateValuationPointResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    candidate_valuation_point=ValuationPointDataResponse(...),  # required
    latest_valuation_point=ValuationPointDataResponse(...),  # optional
    links=[]  # optional
)
```

- [ValuationPointDataResponse](ValuationPointDataResponse.md)
- [ValuationPointDataResponse](ValuationPointDataResponse.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

