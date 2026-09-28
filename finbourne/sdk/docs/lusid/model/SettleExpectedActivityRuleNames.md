# SettleExpectedActivityRuleNames

Names the matching rules that carry the settlement semantics a SettleExpectedActivity writeback depends  upon. Each named rule's target-side formula must be the unmodified settlement activity field; the origin  side is unconstrained.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **activity_type** | **str** | Required | The core rule whose target-side formula is the unmodified &#39;activityType&#39;. Settlement instructions are suggested where the origin-side value is Settled and the target-side value is Expected. |
| **activity_date** | **str** | Required | The core rule whose target-side formula is the unmodified &#39;activityDate&#39;. The origin side supplies the actual settlement date. |
| **units** | **str** | Required | The aggregate rule whose target-side formula is the unmodified &#39;units&#39;. The origin side supplies the units, and the tolerance on this rule classifies the units difference. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettleExpectedActivityRuleNames import SettleExpectedActivityRuleNames

instance = SettleExpectedActivityRuleNames(
    activity_type="...",  # required — The core rule whose target-side formula is the unmodified &#39;activityType&#39;. Settlement instructions are suggested where the origin-side value is Settled and the target-side value is Expected.
    activity_date="...",  # required — The core rule whose target-side formula is the unmodified &#39;activityDate&#39;. The origin side supplies the actual settlement date.
    units="..."  # required — The aggregate rule whose target-side formula is the unmodified &#39;units&#39;. The origin side supplies the units, and the tolerance on this rule classifies the units difference.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

