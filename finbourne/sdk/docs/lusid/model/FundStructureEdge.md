# FundStructureEdge

A link from one member of a Fund Structure to another, and how that link is held.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_from** | **str** | Required | The node code of the member that holds the link: the investor or the owner. |
| **to** | [FundStructureEdgeTarget](FundStructureEdgeTarget.md) | Required | *No description available.* |
| **linkage_type** | **str** | Optional | How the link is held. DedicatedShareClass (the default) means the source invests into a share class of the target; DirectEquityInstrument, GPInterest, LPInterest and CarryInterest mean the source holds that interest in the target through the instrument in viaInstrumentId. Available values: DedicatedShareClass, DirectEquityInstrument, GPInterest, LPInterest, CarryInterest. |
| **via_instrument_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **sharing_percentage** | **float** | Optional | The holder&#39;s ILPA sharing percentage in the target member, adjusted for transfers and equalisation but not reduced by ordinary distributions. Between 0 and 1 inclusive; the percentages declared into any one member must sum to no more than 1. Defaults to 1 (sole ownership) when not supplied. A value of 0 records a full exit: keep the edge and set it to 0 from the date the interest ended, so that the change in percentage from one version of the structure to the next tells the P&amp;L flow what was disposed of. Each disposal or acquisition trade of the holder&#39;s needs its own version of the structure, effective on that trade&#39;s date: proceeds received on a date with no change in percentage are taken as a distribution on the retained interest, not a disposal. A change in percentage with no trade of the holder&#39;s on its date takes effect at the holder&#39;s next transaction on the member or period close, whichever comes first. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureEdge import FundStructureEdge

instance = FundStructureEdge(
    var_from="...",  # required — The node code of the member that holds the link: the investor or the owner.
    to=FundStructureEdgeTarget(...),  # required
    linkage_type="...",  # optional — How the link is held. DedicatedShareClass (the default) means the source invests into a share class of the target; DirectEquityInstrument, GPInterest, LPInterest and CarryInterest mean the source holds that interest in the target through the instrument in viaInstrumentId. Available values: DedicatedShareClass, DirectEquityInstrument, GPInterest, LPInterest, CarryInterest.
    via_instrument_id=ResourceId(...),  # optional
    sharing_percentage=0.0  # optional — The holder&#39;s ILPA sharing percentage in the target member, adjusted for transfers and equalisation but not reduced by ordinary distributions. Between 0 and 1 inclusive; the percentages declared into any one member must sum to no more than 1. Defaults to 1 (sole ownership) when not supplied. A value of 0 records a full exit: keep the edge and set it to 0 from the date the interest ended, so that the change in percentage from one version of the structure to the next tells the P&amp;L flow what was disposed of. Each disposal or acquisition trade of the holder&#39;s needs its own version of the structure, effective on that trade&#39;s date: proceeds received on a date with no change in percentage are taken as a distribution on the retained interest, not a disposal. A change in percentage with no trade of the holder&#39;s on its date takes effect at the holder&#39;s next transaction on the member or period close, whichever comes first.
)
```

- [FundStructureEdgeTarget](FundStructureEdgeTarget.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

