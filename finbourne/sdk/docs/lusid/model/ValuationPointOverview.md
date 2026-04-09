# ValuationPointOverview

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **diary_entry_code** | **str** | Required | The code for the Valuation Point. |
| **diary_entry_variant** | **str** | Optional | The Variant for the Valuation Point. Together with the valuation point code marks the unique branch for the NavType. |
| **effective_from** | **datetime** | Required | The effective time of the last Valuation Point. |
| **effective_to** | **datetime** | Required | The effective time of the current Valuation Point. |
| **query_as_at** | **datetime** | Optional | The query time of the Valuation Point. Defaults to latest. |
| **type** | **str** | Required | The type of the diary entry. This is &#39;ValuationPoint&#39;. |
| **status** | **str** | Required | The status of the Valuation Point. Can be &#39;Estimate&#39;, &#39;Candidate&#39; or &#39;Final&#39;. |
| **gav** | **float** | Required | The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types &#39;Asset&#39; and &#39;Liabilities&#39;. |
| **nav** | **float** | Required | The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period. |
| **holdings_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to QueryAsAt. |
| **valuations_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to QueryAsAt. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The Fee properties. These will be from the &#39;Fee&#39; domain. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ValuationPointOverview import ValuationPointOverview

instance = ValuationPointOverview(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    diary_entry_code="...",  # required — The code for the Valuation Point.
    diary_entry_variant="...",  # optional — The Variant for the Valuation Point. Together with the valuation point code marks the unique branch for the NavType.
    effective_from=datetime.now(),  # required — The effective time of the last Valuation Point.
    effective_to=datetime.now(),  # required — The effective time of the current Valuation Point.
    query_as_at=datetime.now(),  # optional — The query time of the Valuation Point. Defaults to latest.
    type="...",  # required — The type of the diary entry. This is &#39;ValuationPoint&#39;.
    status="...",  # required — The status of the Valuation Point. Can be &#39;Estimate&#39;, &#39;Candidate&#39; or &#39;Final&#39;.
    gav=0.0,  # required — The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types &#39;Asset&#39; and &#39;Liabilities&#39;.
    nav=0.0,  # required — The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period.
    holdings_as_at_override=datetime.now(),  # optional — The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to QueryAsAt.
    valuations_as_at_override=datetime.now(),  # optional — The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to QueryAsAt.
    properties=ModelProperty(...),  # optional — The Fee properties. These will be from the &#39;Fee&#39; domain.
    links=[]  # optional
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

