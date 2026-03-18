# GroupReconciliationReviewStatuses

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **count_pending** | **int** | Required | The number of comparison results of reviewStatus \&quot;Pending\&quot; with this instanceId and reconciliationType |
| **link_pending** | [Link](Link.md) | Required | *No description available.* |
| **count_reviewed** | **int** | Required | The number of comparison results of reviewStatus \&quot;Reviewed\&quot; with this instanceId and reconciliationType |
| **link_reviewed** | [Link](Link.md) | Required | *No description available.* |
| **count_matched** | **int** | Required | The number of comparison results of reviewStatus \&quot;Matched\&quot; with this instanceId and reconciliationType |
| **link_matched** | [Link](Link.md) | Required | *No description available.* |
| **count_invalid** | **int** | Required | The number of comparison results of reviewStatus \&quot;Invalid\&quot; with this instanceId and reconciliationType |
| **link_invalid** | [Link](Link.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationReviewStatuses import GroupReconciliationReviewStatuses

instance = GroupReconciliationReviewStatuses(
    count_pending=0,  # required — The number of comparison results of reviewStatus \&quot;Pending\&quot; with this instanceId and reconciliationType
    link_pending=Link(...),  # required
    count_reviewed=0,  # required — The number of comparison results of reviewStatus \&quot;Reviewed\&quot; with this instanceId and reconciliationType
    link_reviewed=Link(...),  # required
    count_matched=0,  # required — The number of comparison results of reviewStatus \&quot;Matched\&quot; with this instanceId and reconciliationType
    link_matched=Link(...),  # required
    count_invalid=0,  # required — The number of comparison results of reviewStatus \&quot;Invalid\&quot; with this instanceId and reconciliationType
    link_invalid=Link(...)  # required
)
```

- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

