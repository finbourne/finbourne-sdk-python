# RunComplianceV3Request

A request to run one or more V3 compliance rules against a portfolio group, valuing holdings with the  supplied recipe. The pre-trade variant additionally includes the group's live order flow.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_ids** | [List[ResourceId]](ResourceId.md) | Required | *No description available.* |
| **portfolio_group_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **recipe_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **effective_at** | **datetime** | Optional | *No description available.* |
| **as_at** | **datetime** | Optional | *No description available.* |
| **evaluation_mode** | **str** | Optional | Available values: PerPortfolio, GroupTotal. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RunComplianceV3Request import RunComplianceV3Request

instance = RunComplianceV3Request(
    rule_ids=[],  # required
    portfolio_group_id=ResourceId(...),  # required
    recipe_id=ResourceId(...),  # required
    effective_at=datetime.now(),  # optional
    as_at=datetime.now(),  # optional
    evaluation_mode="..."  # optional — Available values: PerPortfolio, GroupTotal.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

