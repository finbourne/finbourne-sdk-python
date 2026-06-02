# ValuationPoint

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **valuation_point_code** | **str** | Optional | The code of the Valuation Point. |
| **variant** | **str** | Optional | The Variant name for the Valuation Point. |
| **name** | **str** | Optional | Identifiable Name assigned to the Valuation Point. |
| **status** | **str** | Required | The status of the Valuation Point. Available values: Undefined, Estimate, Final, Candidate, Unofficial. |
| **apply_clear_down** | **bool** | Optional | Indicates whether a clear down was applied when the Valuation Point was created. |
| **effective_at** | **datetime** | Required | The effective time of the Valuation Point. |
| **query_as_at** | **datetime** | Optional | The AsAt time of the Valuation Point. This is the AsAt time that will be used when requests are made using the entry. |
| **holdings_as_at** | **datetime** | Optional | The AsAt time used for building holdings in the Valuation Point. |
| **valuation_as_at** | **datetime** | Optional | The AsAt time used for performing valuations in the Valuation Point. |
| **previous** | [PreviousValuationPoint](PreviousValuationPoint.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The Valuation Point properties. These are from the &#39;DiaryEntry&#39; domain. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ValuationPoint import ValuationPoint

instance = ValuationPoint(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    valuation_point_code="...",  # optional — The code of the Valuation Point.
    variant="...",  # optional — The Variant name for the Valuation Point.
    name="...",  # optional — Identifiable Name assigned to the Valuation Point.
    status="...",  # required — The status of the Valuation Point. Available values: Undefined, Estimate, Final, Candidate, Unofficial.
    apply_clear_down=True,  # optional — Indicates whether a clear down was applied when the Valuation Point was created.
    effective_at=datetime.now(),  # required — The effective time of the Valuation Point.
    query_as_at=datetime.now(),  # optional — The AsAt time of the Valuation Point. This is the AsAt time that will be used when requests are made using the entry.
    holdings_as_at=datetime.now(),  # optional — The AsAt time used for building holdings in the Valuation Point.
    valuation_as_at=datetime.now(),  # optional — The AsAt time used for performing valuations in the Valuation Point.
    previous=PreviousValuationPoint(...),  # optional
    properties=ModelProperty(...),  # optional — The Valuation Point properties. These are from the &#39;DiaryEntry&#39; domain.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [PreviousValuationPoint](PreviousValuationPoint.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

