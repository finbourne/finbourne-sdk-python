# ValuationPointDataResponse

The Valuation Point Data Response for the Fund and specified date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **type** | **str** | Required | The Type of the associated Diary Entry (&#39;PeriodBoundary&#39;,&#39;ValuationPoint&#39;,&#39;Other&#39; or &#39;Adhoc&#39; when a diary entry wasn&#39;t used). |
| **status** | **str** | Required | The status of a Diary Entry of Type &#39;ValuationPoint&#39;. Defaults to &#39;Estimate&#39; when upserting a diary entry, moves to &#39;Candidate&#39; or &#39;Final&#39; when a ValuationPoint is accepted, and &#39;Final&#39; when it is finalised. The status of a Diary Entry becomes &#39;Unofficial&#39; when a diary entry wasn&#39;t used. |
| **fund_details** | [FundDetails](FundDetails.md) | Required | *No description available.* |
| **fund_valuation_point_data** | [FundValuationPointData](FundValuationPointData.md) | Required | *No description available.* |
| **share_class_data** | [List[ShareClassData]](ShareClassData.md) | Required | The data for all share classes in fund. Share classes are identified by their short codes. |
| **valuation_point_code** | **str** | Optional | The code of the valuation point. |
| **previous_valuation_point_code** | **str** | Optional | The code of the previous valuation point. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ValuationPointDataResponse import ValuationPointDataResponse

instance = ValuationPointDataResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    type="...",  # required — The Type of the associated Diary Entry (&#39;PeriodBoundary&#39;,&#39;ValuationPoint&#39;,&#39;Other&#39; or &#39;Adhoc&#39; when a diary entry wasn&#39;t used).
    status="...",  # required — The status of a Diary Entry of Type &#39;ValuationPoint&#39;. Defaults to &#39;Estimate&#39; when upserting a diary entry, moves to &#39;Candidate&#39; or &#39;Final&#39; when a ValuationPoint is accepted, and &#39;Final&#39; when it is finalised. The status of a Diary Entry becomes &#39;Unofficial&#39; when a diary entry wasn&#39;t used.
    fund_details=FundDetails(...),  # required
    fund_valuation_point_data=FundValuationPointData(...),  # required
    share_class_data=[],  # required — The data for all share classes in fund. Share classes are identified by their short codes.
    valuation_point_code="...",  # optional — The code of the valuation point.
    previous_valuation_point_code="...",  # optional — The code of the previous valuation point.
    links=[]  # optional
)
```

- [FundDetails](FundDetails.md)
- [FundValuationPointData](FundValuationPointData.md)
- [ShareClassData](ShareClassData.md) — used in `share_class_data`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

