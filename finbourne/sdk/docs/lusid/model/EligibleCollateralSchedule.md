# EligibleCollateralSchedule

An eligible collateral schedule: the collateral a party may post under a margin arrangement and the valuation  percentage each class of collateral is accepted at.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **description** | **str** | Optional | A description of the Eligible Collateral Schedule. Optional. |
| **rows** | [List[EligibleCollateralRow]](EligibleCollateralRow.md) | Optional | The classes of collateral that may be posted, each with the valuation percentage it is accepted at. At least one and at most 200 rows. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties to decorate onto the Eligible Collateral Schedule. Filterable. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EligibleCollateralSchedule import EligibleCollateralSchedule

instance = EligibleCollateralSchedule(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    description="...",  # optional — A description of the Eligible Collateral Schedule. Optional.
    rows=[],  # optional — The classes of collateral that may be posted, each with the valuation percentage it is accepted at. At least one and at most 200 rows.
    version=Version(...),  # optional
    properties=ModelProperty(...),  # optional — A set of properties to decorate onto the Eligible Collateral Schedule. Filterable.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [EligibleCollateralRow](EligibleCollateralRow.md) — used in `rows`
- [Version](Version.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

