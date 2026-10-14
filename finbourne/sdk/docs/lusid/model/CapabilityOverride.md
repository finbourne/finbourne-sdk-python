# CapabilityOverride

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **capability** | **str** | Required | Available values: RecallableDistributions, RecallCalls, ReturnOfExcessContributions, SubsequentCloseEqualisation, PartnerPnlAllocation, DistributionMechanism, DistributionCharacterSource, SecondaryTransfer, ExcuseExclude, DealScopedPnl, NettedCallAndDistribution. |
| **setting** | **str** | Required | Available values: Allowed, Forbidden. |
| **reason** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CapabilityOverride import CapabilityOverride

instance = CapabilityOverride(
    capability="...",  # required — Available values: RecallableDistributions, RecallCalls, ReturnOfExcessContributions, SubsequentCloseEqualisation, PartnerPnlAllocation, DistributionMechanism, DistributionCharacterSource, SecondaryTransfer, ExcuseExclude, DealScopedPnl, NettedCallAndDistribution.
    setting="...",  # required — Available values: Allowed, Forbidden.
    reason="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

