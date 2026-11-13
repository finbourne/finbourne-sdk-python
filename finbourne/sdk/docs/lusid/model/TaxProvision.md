# TaxProvision

The deferred tax provision struck for a fund at a valuation point: the realised and notionally realised  (deemed disposal) gains it is built from, the indexation and loss relief applied, the rate, the resulting  provision amount, its movement since the previous valuation point and, once approved, who approved it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **fund** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **nav_type_code** | **str** | Required | The NAV type the provision was struck for. |
| **diary_entry_code** | **str** | Required | The diary entry code of the valuation point the provision was struck at. |
| **effective_at** | **datetime** | Required | The effective date of the valuation point the provision was struck at. |
| **as_at** | **datetime** | Required | The asAt datetime at which this version of the provision was recorded. |
| **status** | **str** | Required | Whether the provision is an Estimate or has been Approved. An approved provision has been posted to the fund as an accrual. |
| **realised_gains** | **float** | Required | The chargeable gains realised by disposals since the start of the tax period, after indexation allowance. |
| **unrealised_gains** | **float** | Required | The chargeable gains that would arise on a notional deemed disposal of the fund&#39;s holdings at the valuation point. |
| **indexation_allowance** | **float** | Required | The indexation allowance taken against the gains in this provision. |
| **losses_brought_forward** | **float** | Required | The allowable losses standing at the start of the tax period and available to offset gains. |
| **losses_used** | **float** | Required | The losses brought forward that were used against the gains in this provision. |
| **losses_carried_forward** | **float** | Required | The allowable losses remaining after this provision, to be carried forward to the next tax period. Only realised losses are carried; a notional loss on the deemed disposal is not. |
| **rate_applied** | **float** | Required | The tax rate applied to the net chargeable gains to arrive at the provision amount. |
| **provision_amount** | **float** | Required | The deferred tax provision amount at the valuation point. |
| **movement** | [TaxProvisionMovement](TaxProvisionMovement.md) | Required | *No description available.* |
| **approved_by** | **str** | Optional | The user who approved the provision, if it has been approved. |
| **approved_at** | **datetime** | Optional | The asAt datetime at which the provision was approved, if it has been approved. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxProvision import TaxProvision

instance = TaxProvision(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    fund=ResourceId(...),  # required
    nav_type_code="...",  # required — The NAV type the provision was struck for.
    diary_entry_code="...",  # required — The diary entry code of the valuation point the provision was struck at.
    effective_at=datetime.now(),  # required — The effective date of the valuation point the provision was struck at.
    as_at=datetime.now(),  # required — The asAt datetime at which this version of the provision was recorded.
    status="...",  # required — Whether the provision is an Estimate or has been Approved. An approved provision has been posted to the fund as an accrual.
    realised_gains=0.0,  # required — The chargeable gains realised by disposals since the start of the tax period, after indexation allowance.
    unrealised_gains=0.0,  # required — The chargeable gains that would arise on a notional deemed disposal of the fund&#39;s holdings at the valuation point.
    indexation_allowance=0.0,  # required — The indexation allowance taken against the gains in this provision.
    losses_brought_forward=0.0,  # required — The allowable losses standing at the start of the tax period and available to offset gains.
    losses_used=0.0,  # required — The losses brought forward that were used against the gains in this provision.
    losses_carried_forward=0.0,  # required — The allowable losses remaining after this provision, to be carried forward to the next tax period. Only realised losses are carried; a notional loss on the deemed disposal is not.
    rate_applied=0.0,  # required — The tax rate applied to the net chargeable gains to arrive at the provision amount.
    provision_amount=0.0,  # required — The deferred tax provision amount at the valuation point.
    movement=TaxProvisionMovement(...),  # required
    approved_by="...",  # optional — The user who approved the provision, if it has been approved.
    approved_at=datetime.now(),  # optional — The asAt datetime at which the provision was approved, if it has been approved.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [TaxProvisionMovement](TaxProvisionMovement.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

