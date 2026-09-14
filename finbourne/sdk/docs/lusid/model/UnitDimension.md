# UnitDimension

One factor of a result's unit, modelled as dimensional analysis rather than a label, e.g. a  rates delta is GBP^1 . GBP.LIBOR.3M^-1 - \"GBP per basis point\". A result's `units` is a  flat list of these; the count tracks the order of the derivative (a ratio), not the result's  axes, and must not be indexed by axis.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **unit_domain** | **str** | Optional | The domain this factor is drawn from, e.g. \&quot;Ccy\&quot;, \&quot;Rate\&quot;, \&quot;Vol\&quot;, \&quot;Security\&quot;. |
| **name** | **str** | Optional | The name within the domain, e.g. a currency code or a curve identifier. |
| **power** | **int** | Optional | The exponent this factor is raised to. |
| **scale** | **float** | Optional | The scale of one unit of this factor, e.g. 1e-4 for a basis point. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UnitDimension import UnitDimension

instance = UnitDimension(
    unit_domain="...",  # optional — The domain this factor is drawn from, e.g. \&quot;Ccy\&quot;, \&quot;Rate\&quot;, \&quot;Vol\&quot;, \&quot;Security\&quot;.
    name="...",  # optional — The name within the domain, e.g. a currency code or a curve identifier.
    power=0,  # optional — The exponent this factor is raised to.
    scale=0.0  # optional — The scale of one unit of this factor, e.g. 1e-4 for a basis point.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

