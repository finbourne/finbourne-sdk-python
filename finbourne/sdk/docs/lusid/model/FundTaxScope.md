# FundTaxScope

The UK chargeable-gains tax scope of a fund at a point in time: the portfolios inside the regime and what the  regime's figures leave out.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **portfolios** | [List[ResourceId]](ResourceId.md) | Required | The portfolios within the UK chargeable-gains regime. A fund portfolio is in scope when its own details elect the regime. A NAV type that elects the regime puts its derived portfolio for each fund portfolio in scope. |
| **exclusions** | [FundTaxScopeExclusions](FundTaxScopeExclusions.md) | Required | *No description available.* |
| **effective_at** | **datetime** | Required | The effective datetime at which the tax scope was read. |
| **as_at** | **datetime** | Required | The asAt datetime at which the tax scope was read. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundTaxScope import FundTaxScope

instance = FundTaxScope(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    portfolios=[],  # required — The portfolios within the UK chargeable-gains regime. A fund portfolio is in scope when its own details elect the regime. A NAV type that elects the regime puts its derived portfolio for each fund portfolio in scope.
    exclusions=FundTaxScopeExclusions(...),  # required
    effective_at=datetime.now(),  # required — The effective datetime at which the tax scope was read.
    as_at=datetime.now(),  # required — The asAt datetime at which the tax scope was read.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md) — used in `portfolios`
- [FundTaxScopeExclusions](FundTaxScopeExclusions.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

