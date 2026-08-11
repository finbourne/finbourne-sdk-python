# GroupReconciliationResultStatuses

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **count_new** | **int** | Required | The number of comparison results of resultStatus \&quot;New\&quot; with this instanceId and reconciliationType |
| **link_new** | [Link](Link.md) | Required | *No description available.* |
| **count_confirmed** | **int** | Required | The number of comparison results of resultStatus \&quot;Confirmed\&quot; with this instanceId and reconciliationType |
| **link_confirmed** | [Link](Link.md) | Required | *No description available.* |
| **count_changed** | **int** | Required | The number of comparison results of resultStatus \&quot;Changed\&quot; with this instanceId and reconciliationType |
| **link_changed** | [Link](Link.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationResultStatuses import GroupReconciliationResultStatuses

instance = GroupReconciliationResultStatuses(
    count_new=0,  # required — The number of comparison results of resultStatus \&quot;New\&quot; with this instanceId and reconciliationType
    link_new=Link(...),  # required
    count_confirmed=0,  # required — The number of comparison results of resultStatus \&quot;Confirmed\&quot; with this instanceId and reconciliationType
    link_confirmed=Link(...),  # required
    count_changed=0,  # required — The number of comparison results of resultStatus \&quot;Changed\&quot; with this instanceId and reconciliationType
    link_changed=Link(...)  # required
)
```

- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

