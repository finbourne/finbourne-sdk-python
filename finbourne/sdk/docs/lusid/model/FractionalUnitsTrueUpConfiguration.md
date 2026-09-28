# FractionalUnitsTrueUpConfiguration

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fractional_units_handling** | **str** | Optional | The fractional-units handling scheme for the portfolio&#39;s corporate-action processing. This can be: LotLevelRounding or CustodianLevelTrueUp. Defaults to LotLevelRounding, today&#39;s per-lot-only processing, if not specified. Available values: LotLevelRounding, CustodianLevelTrueUp. |
| **nominated_sub_holding_key** | **str** | Optional | The sub-holding key (from the &#39;Transaction&#39; domain) that custodian-level fractional-units true-ups are booked to. The key must be one of the portfolio&#39;s sub-holding keys, must have a pre-defined property definition, and event processing never creates it. |
| **nominated_sub_holding_key_value** | **str** | Optional | The value of the nominated sub-holding key under which the true-up holding is booked, for example the bucket that quarantines fractional rounding true-ups. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FractionalUnitsTrueUpConfiguration import FractionalUnitsTrueUpConfiguration

instance = FractionalUnitsTrueUpConfiguration(
    fractional_units_handling="...",  # optional — The fractional-units handling scheme for the portfolio&#39;s corporate-action processing. This can be: LotLevelRounding or CustodianLevelTrueUp. Defaults to LotLevelRounding, today&#39;s per-lot-only processing, if not specified. Available values: LotLevelRounding, CustodianLevelTrueUp.
    nominated_sub_holding_key="...",  # optional — The sub-holding key (from the &#39;Transaction&#39; domain) that custodian-level fractional-units true-ups are booked to. The key must be one of the portfolio&#39;s sub-holding keys, must have a pre-defined property definition, and event processing never creates it.
    nominated_sub_holding_key_value="..."  # optional — The value of the nominated sub-holding key under which the true-up holding is booked, for example the bucket that quarantines fractional rounding true-ups.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

