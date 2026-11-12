# ElectionProrationRate

The proration rate the issuer applies to one option of a multi-option event, keyed by the option's election key.  An entry overrides the event-level proration rate for that election only.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **election_key** | **str** | Required | The election key of the option this proration rate applies to. |
| **proration_rate** | **float** | Required | The fraction of the quantity instructed on this option that the issuer accepts. Must be in (0, 1]. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ElectionProrationRate import ElectionProrationRate

instance = ElectionProrationRate(
    election_key="...",  # required — The election key of the option this proration rate applies to.
    proration_rate=0.0  # required — The fraction of the quantity instructed on this option that the issuer accepts. Must be in (0, 1].
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

