# ComplianceRuleV3DescribeResponse

A plain-English description of a V3 compliance rule: its identity, the kind of entity it examines, and a  single sentence describing what it checks. The sentence is empty for a rule the generator cannot fully  express.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **subject** | **str** | Optional | Available values: Holdings, Orders. |
| **plain_english** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleV3DescribeResponse import ComplianceRuleV3DescribeResponse

instance = ComplianceRuleV3DescribeResponse(
    id=ResourceId(...),  # optional
    subject="...",  # optional — Available values: Holdings, Orders.
    plain_english="..."  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

