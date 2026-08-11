# UpdateNetworkZoneRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **description** | **str** | Optional | *No description available.* |
| **network_zone_ips** | [List[IpAddressDefinition]](IpAddressDefinition.md) | Required | *No description available.* |
| **action** | **str** | Optional | *No description available.* |
| **apply_rules** | [NetworkZonesApplyRules](NetworkZonesApplyRules.md) | Required | *No description available.* |
| **hierarchy** | **int** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.UpdateNetworkZoneRequest import UpdateNetworkZoneRequest

instance = UpdateNetworkZoneRequest(
    description="...",  # optional
    network_zone_ips=[],  # required
    action="...",  # optional
    apply_rules=NetworkZonesApplyRules(...),  # required
    hierarchy=0  # required
)
```

- [IpAddressDefinition](IpAddressDefinition.md)
- [NetworkZonesApplyRules](NetworkZonesApplyRules.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

