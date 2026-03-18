# StagedModificationStagingRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **staging_rule_set_id** | **str** | Optional | System generated unique id for the staging rule set. |
| **rule_id** | **str** | Optional | The ID of the staging rule. |
| **required_approvals** | **int** | Optional | The number of approvals required. If left blank, one approval is needed. |
| **current_user_can_decide** | **bool** | Optional | True or False indicating whether the current user can make a decision on the staged modification. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StagedModificationStagingRule import StagedModificationStagingRule

instance = StagedModificationStagingRule(
    staging_rule_set_id="...",  # optional — System generated unique id for the staging rule set.
    rule_id="...",  # optional — The ID of the staging rule.
    required_approvals=0,  # optional — The number of approvals required. If left blank, one approval is needed.
    current_user_can_decide=True  # optional — True or False indicating whether the current user can make a decision on the staged modification.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

