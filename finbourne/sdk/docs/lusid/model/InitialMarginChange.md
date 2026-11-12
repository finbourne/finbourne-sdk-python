# InitialMarginChange

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **we_post_before** | **float** | Required | What we must post to the set today, after the threshold. |
| **we_post_after** | **float** | Required | What we would post to the set after the move, after the threshold. |
| **they_post_before** | **float** | Optional | What the counterparty must post today. Null where the run does not know it, as under SIMM without their sensitivities. |
| **they_post_after** | **float** | Optional | What the counterparty would post after the move. Null where the run does not know it. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InitialMarginChange import InitialMarginChange

instance = InitialMarginChange(
    we_post_before=0.0,  # required — What we must post to the set today, after the threshold.
    we_post_after=0.0,  # required — What we would post to the set after the move, after the threshold.
    they_post_before=0.0,  # optional — What the counterparty must post today. Null where the run does not know it, as under SIMM without their sensitivities.
    they_post_after=0.0  # optional — What the counterparty would post after the move. Null where the run does not know it.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

