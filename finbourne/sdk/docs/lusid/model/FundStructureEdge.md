# FundStructureEdge

A link from one member of a Fund Structure to another, and how that link is held.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_from** | **str** | Required | The node code of the member that holds the link: the investor or the owner. |
| **to** | [FundStructureEdgeTarget](FundStructureEdgeTarget.md) | Required | *No description available.* |
| **linkage_type** | **str** | Optional | How the link is held. DedicatedShareClass (the default) means the source invests into a share class of the target; DirectEquityInstrument, GPInterest, LPInterest and CarryInterest mean the source holds that interest in the target through the instrument in viaInstrumentId. Available values: DedicatedShareClass, DirectEquityInstrument, GPInterest, LPInterest, CarryInterest. |
| **via_instrument_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureEdge import FundStructureEdge

instance = FundStructureEdge(
    var_from="...",  # required — The node code of the member that holds the link: the investor or the owner.
    to=FundStructureEdgeTarget(...),  # required
    linkage_type="...",  # optional — How the link is held. DedicatedShareClass (the default) means the source invests into a share class of the target; DirectEquityInstrument, GPInterest, LPInterest and CarryInterest mean the source holds that interest in the target through the instrument in viaInstrumentId. Available values: DedicatedShareClass, DirectEquityInstrument, GPInterest, LPInterest, CarryInterest.
    via_instrument_id=ResourceId(...)  # optional
)
```

- [FundStructureEdgeTarget](FundStructureEdgeTarget.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

