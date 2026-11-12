# ComplianceRuleContribution

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **order_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instrument** | **str** | Required | The LUSID instrument identifier (LUID) of the instrument for this contribution. |
| **instrument_type** | **str** | Optional | Optional. The economic type of the instrument for this contribution. |
| **holding_type** | **str** | Optional | Optional. The holding type of this contribution. |
| **holding_id** | **str** | Optional | Optional. The internal holding identifier encoding the detail of what the holding includes. |
| **held_by** | **str** | Optional | Optional. Where this holding sits relative to the rule&#39;s benchmark: portfolio, benchmark or both.  Meaningful only for benchmark-relative rules. |
| **keys_used** | [List[ComplianceKeyUsed]](ComplianceKeyUsed.md) | Required | The keys this holding contributed to the rule: each key the rule read (plus the portfolio NAV key), with the  role(s) it played, the holding&#39;s own value for it, and which bag the value came from. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleContribution import ComplianceRuleContribution

instance = ComplianceRuleContribution(
    portfolio_id=ResourceId(...),  # required
    order_id=ResourceId(...),  # optional
    instrument="...",  # required — The LUSID instrument identifier (LUID) of the instrument for this contribution.
    instrument_type="...",  # optional — Optional. The economic type of the instrument for this contribution.
    holding_type="...",  # optional — Optional. The holding type of this contribution.
    holding_id="...",  # optional — Optional. The internal holding identifier encoding the detail of what the holding includes.
    held_by="...",  # optional — Optional. Where this holding sits relative to the rule&#39;s benchmark: portfolio, benchmark or both.  Meaningful only for benchmark-relative rules.
    keys_used=[]  # required — The keys this holding contributed to the rule: each key the rule read (plus the portfolio NAV key), with the  role(s) it played, the holding&#39;s own value for it, and which bag the value came from.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ComplianceKeyUsed](ComplianceKeyUsed.md) — used in `keys_used`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

