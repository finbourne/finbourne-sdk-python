# NetworkZoneDefinitionResponse

The Client facing representation of a NetworkZone
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Optional | The Network Zone Code |
| **hierarchy** | **int** | Optional | Hierarchy of the Network Zone |
| **description** | **str** | Optional | The Description of the Network Zone |
| **created_at** | **datetime** | Optional | Network Zone Creation timestamp |
| **updated_at** | **datetime** | Optional | Timestamp of the last update |
| **network_zone_ips** | [List[IpAddressDefinition]](IpAddressDefinition.md) | Optional | Network zone IP information (IPs and CIDR ranges) |
| **action** | **str** | Optional | Kind of action to apply when a request matches this Network Zone (Block/Allow/NoOp) |
| **apply_rules** | [NetworkZonesApplyRules](NetworkZonesApplyRules.md) | Optional | *No description available.* |
| **created_by** | **str** | Optional | User Id that created the Network Zone |
| **updated_by** | **str** | Optional | User Id of the last update on the Network Zone |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.NetworkZoneDefinitionResponse import NetworkZoneDefinitionResponse

instance = NetworkZoneDefinitionResponse(
    code="...",  # optional — The Network Zone Code
    hierarchy=0,  # optional — Hierarchy of the Network Zone
    description="...",  # optional — The Description of the Network Zone
    created_at=datetime.now(),  # optional — Network Zone Creation timestamp
    updated_at=datetime.now(),  # optional — Timestamp of the last update
    network_zone_ips=[],  # optional — Network zone IP information (IPs and CIDR ranges)
    action="...",  # optional — Kind of action to apply when a request matches this Network Zone (Block/Allow/NoOp)
    apply_rules=NetworkZonesApplyRules(...),  # optional
    created_by="...",  # optional — User Id that created the Network Zone
    updated_by="..."  # optional — User Id of the last update on the Network Zone
)
```

- [IpAddressDefinition](IpAddressDefinition.md) — used in `network_zone_ips`
- [NetworkZonesApplyRules](NetworkZonesApplyRules.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

