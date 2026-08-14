# RecResult

An individual reconciliation result — the aggregate result for a set of core rule values within a  rec type, with its type/status, review and exception axes, rule values and item-level detail.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The system-generated identifier for the rec result. Comprises the rec definition id, the instance id, the rec type and the core rule values. |
| **rec_type** | **str** | Required | The type of rec that the result belongs to (e.g. Holding). Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity. |
| **instance_id** | [RecInstanceId](RecInstanceId.md) | Required | *No description available.* |
| **rec_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **run_number** | **int** | Required | The run number within the instance. Increments with each re-run. |
| **run_as_at** | **datetime** | Required | The asAt datetime at which the run happened. |
| **dates_reconciled** | [RecDatesReconciled](RecDatesReconciled.md) | Required | *No description available.* |
| **result_type** | **str** | Required | The type of result. Exceptions: PartialMatch, PartialCross, Break. Non-exceptions: Match, Cross. Available values: Match, Cross, PartialMatch, PartialCross, Break. |
| **result_cardinality** | **str** | Required | The item cardinality of the result, read left to right (e.g. OneToOne, ManyToNone). Available values: OneToOne, OneToMany, ManyToOne, ManyToMany, OneToNone, ManyToNone, NoneToOne, NoneToMany, NoneToNone. |
| **result_life_cycle** | **str** | Required | The run-over-run change in the result, evaluated each run against the prior run. Available values: New, Unchanged, Changed, Cleared. |
| **exception** | [RecResultException](RecResultException.md) | Optional | *No description available.* |
| **review** | [RecResultReview](RecResultReview.md) | Required | *No description available.* |
| **core_rules** | [List[CoreRuleValues]](CoreRuleValues.md) | Required | The core matching rules and the values that pin this result to its reconciled position. |
| **aggregate_rules** | [List[AggregateRuleValues]](AggregateRuleValues.md) | Required | The aggregate matching rules and their measured values. |
| **supplemental_attributes** | [List[SupplementalAttributeValues]](SupplementalAttributeValues.md) | Required | Additional attribute values carried on the result for context. Do not contribute to matching or the result id. |
| **items** | [RecResultItemDetails](RecResultItemDetails.md) | Required | *No description available.* |
| **comments** | [List[RecUserComment]](RecUserComment.md) | Required | User-authored comments attached to the result. Carried forward across runs. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Properties in the RecResult domain. Filterable and sortable. |
| **assigned_user** | **str** | Optional | The LUSID user id assigned to the result. |
| **assigned_role** | **str** | Optional | The LUSID IAM role id assigned to the result. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResult import RecResult

instance = RecResult(
    id="...",  # required — The system-generated identifier for the rec result. Comprises the rec definition id, the instance id, the rec type and the core rule values.
    rec_type="...",  # required — The type of rec that the result belongs to (e.g. Holding). Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity.
    instance_id=RecInstanceId(...),  # required
    rec_definition_id=ResourceId(...),  # required
    run_number=0,  # required — The run number within the instance. Increments with each re-run.
    run_as_at=datetime.now(),  # required — The asAt datetime at which the run happened.
    dates_reconciled=RecDatesReconciled(...),  # required
    result_type="...",  # required — The type of result. Exceptions: PartialMatch, PartialCross, Break. Non-exceptions: Match, Cross. Available values: Match, Cross, PartialMatch, PartialCross, Break.
    result_cardinality="...",  # required — The item cardinality of the result, read left to right (e.g. OneToOne, ManyToNone). Available values: OneToOne, OneToMany, ManyToOne, ManyToMany, OneToNone, ManyToNone, NoneToOne, NoneToMany, NoneToNone.
    result_life_cycle="...",  # required — The run-over-run change in the result, evaluated each run against the prior run. Available values: New, Unchanged, Changed, Cleared.
    exception=RecResultException(...),  # optional
    review=RecResultReview(...),  # required
    core_rules=[],  # required — The core matching rules and the values that pin this result to its reconciled position.
    aggregate_rules=[],  # required — The aggregate matching rules and their measured values.
    supplemental_attributes=[],  # required — Additional attribute values carried on the result for context. Do not contribute to matching or the result id.
    items=RecResultItemDetails(...),  # required
    comments=[],  # required — User-authored comments attached to the result. Carried forward across runs.
    properties=PerpetualProperty(...),  # optional — Properties in the RecResult domain. Filterable and sortable.
    assigned_user="...",  # optional — The LUSID user id assigned to the result.
    assigned_role="...",  # optional — The LUSID IAM role id assigned to the result.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [RecInstanceId](RecInstanceId.md)
- [ResourceId](ResourceId.md)
- [RecDatesReconciled](RecDatesReconciled.md)
- [RecResultException](RecResultException.md)
- [RecResultReview](RecResultReview.md)
- [CoreRuleValues](CoreRuleValues.md) — used in `core_rules`
- [AggregateRuleValues](AggregateRuleValues.md) — used in `aggregate_rules`
- [SupplementalAttributeValues](SupplementalAttributeValues.md) — used in `supplemental_attributes`
- [RecResultItemDetails](RecResultItemDetails.md)
- [RecUserComment](RecUserComment.md) — used in `comments`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

