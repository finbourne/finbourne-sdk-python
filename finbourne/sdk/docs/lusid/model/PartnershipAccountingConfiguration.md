# PartnershipAccountingConfiguration

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **enabled** | **bool** | Required | *No description available.* |
| **config_pack** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **commitment_currency_policy** | **str** | Optional | Available values: FundCurrencyOnly. |
| **register_portfolio_group** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **capital_model** | **str** | Optional | Available values: PartnershipCapitalAccounts, SeriesUnitised. |
| **capability_overrides** | [List[CapabilityOverride]](CapabilityOverride.md) | Optional | *No description available.* |
| **series** | [SeriesConfiguration](SeriesConfiguration.md) | Optional | *No description available.* |
| **effective_capabilities** | **Dict[str, Optional[str]]** | Optional | Derived on the way out; ignored on the way in. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnershipAccountingConfiguration import PartnershipAccountingConfiguration

instance = PartnershipAccountingConfiguration(
    enabled=True,  # required
    config_pack=ResourceId(...),  # optional
    commitment_currency_policy="...",  # optional — Available values: FundCurrencyOnly.
    register_portfolio_group=ResourceId(...),  # optional
    capital_model="...",  # optional — Available values: PartnershipCapitalAccounts, SeriesUnitised.
    capability_overrides=[],  # optional
    series=SeriesConfiguration(...),  # optional
    effective_capabilities=  # optional — Derived on the way out; ignored on the way in.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [CapabilityOverride](CapabilityOverride.md)
- [SeriesConfiguration](SeriesConfiguration.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

