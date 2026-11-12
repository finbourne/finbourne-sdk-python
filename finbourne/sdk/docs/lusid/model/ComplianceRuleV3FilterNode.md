# ComplianceRuleV3FilterNode

A node in a rule's filter tree: either a group combining child nodes with all/any, or a leaf condition.  The concrete kind is named by the FilterNodeType property.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **filter_node_type** | **str** | Required | Available values: ComplianceRuleV3FilterGroup, ComplianceRuleV3FilterCondition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleV3FilterNode import ComplianceRuleV3FilterNode

instance = ComplianceRuleV3FilterNode(
    filter_node_type="..."  # required — Available values: ComplianceRuleV3FilterGroup, ComplianceRuleV3FilterCondition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

