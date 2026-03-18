# GroupReconciliationResultTypes

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **count_match** | **int** | Required | The number of comparison results of resultType \&quot;Match\&quot; with this instanceId and reconciliationType |
| **link_matches** | [Link](Link.md) | Required | *No description available.* |
| **count_partial_match** | **int** | Required | The number of comparison results of resultType \&quot;PartialMatch\&quot; with this instanceId and reconciliationType |
| **link_partial_matches** | [Link](Link.md) | Required | *No description available.* |
| **count_break** | **int** | Required | The number of comparison results of resultType \&quot;Break\&quot; with this instanceId and reconciliationType |
| **link_breaks** | [Link](Link.md) | Required | *No description available.* |
| **count_resolved** | **int** | Required | The number of comparison results of resultType \&quot;Resolved\&quot; with this instanceId and reconciliationType |
| **link_resolved** | [Link](Link.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationResultTypes import GroupReconciliationResultTypes

instance = GroupReconciliationResultTypes(
    count_match=0,  # required — The number of comparison results of resultType \&quot;Match\&quot; with this instanceId and reconciliationType
    link_matches=Link(...),  # required
    count_partial_match=0,  # required — The number of comparison results of resultType \&quot;PartialMatch\&quot; with this instanceId and reconciliationType
    link_partial_matches=Link(...),  # required
    count_break=0,  # required — The number of comparison results of resultType \&quot;Break\&quot; with this instanceId and reconciliationType
    link_breaks=Link(...),  # required
    count_resolved=0,  # required — The number of comparison results of resultType \&quot;Resolved\&quot; with this instanceId and reconciliationType
    link_resolved=Link(...)  # required
)
```

- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

