# CreateNetworkZoneRequest

The Create Network Zone Request information
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **network_zone_ips** | [List[IpAddressDefinition]](IpAddressDefinition.md) | Required | *No description available.* |
| **action** | **str** | Optional | *No description available.* |
| **apply_rules** | [NetworkZonesApplyRules](NetworkZonesApplyRules.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.CreateNetworkZoneRequest import CreateNetworkZoneRequest

instance = CreateNetworkZoneRequest(
    code="...",  # required
    description="...",  # optional
    network_zone_ips=[],  # required
    action="...",  # optional
    apply_rules=NetworkZonesApplyRules(...)  # required
)
```

- [IpAddressDefinition](IpAddressDefinition.md)
- [NetworkZonesApplyRules](NetworkZonesApplyRules.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

