# FundPartnerUnfundedReconciliation

The unfunded commitment statement of one partner over a period: the register's opening unfunded, the booked  activity that moves it, the closing unfunded that implies, and the register's own closing unfunded it is checked against.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The investor record the statement is for. |
| **fund_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **currency** | **str** | Required | The currency of every amount on the statement, being the commitment currency of the register line. |
| **period_from** | **datetime** | Required | The effective datetime the statement opens at. |
| **period_to** | **datetime** | Required | The effective datetime the statement closes at. |
| **opening_unfunded** | **float** | Required | The unfunded commitment at the opening datetime, from the register. |
| **contributions_inside_commitment** | **float** | Required | Capital called inside the commitment over the period, which reduces unfunded. Contributions outside the commitment, such as equalisation interest, are listed but do not count here. |
| **recallable_distributions** | **float** | Required | Distributions over the period returned as recallable, which restore unfunded. |
| **expired_recallable** | **float** | Required | Recallable distributions whose recall deadline passed in the period without being recalled, which reduce unfunded. |
| **commitment_changes** | **float** | Required | Changes to the commitment over the period, which move unfunded one for one. |
| **transfers** | **float** | Required | Commitment transferred in or out over the period, which moves unfunded one for one. |
| **closing_unfunded** | **float** | Required | Opening unfunded less contributions inside the commitment, plus recallable distributions, less expired recallable, plus or minus commitment changes and transfers. |
| **register_unfunded** | **float** | Required | The unfunded commitment at the closing datetime, from the register. |
| **difference** | **float** | Required | Closing unfunded less the register&#39;s unfunded at the closing datetime. Zero when the statement ties. |
| **ties** | **bool** | Required | Whether the closing unfunded equals the register&#39;s unfunded at the closing datetime. |
| **lines** | [List[FundPartnerUnfundedReconciliationLine]](FundPartnerUnfundedReconciliationLine.md) | Required | Every booked allocation to the partner over the period, in event date order, with the ILPA transaction type each is reported under and its effect on unfunded. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundPartnerUnfundedReconciliation import FundPartnerUnfundedReconciliation

instance = FundPartnerUnfundedReconciliation(
    investor_record_id="...",  # required — The investor record the statement is for.
    fund_id=ResourceId(...),  # required
    currency="...",  # required — The currency of every amount on the statement, being the commitment currency of the register line.
    period_from=datetime.now(),  # required — The effective datetime the statement opens at.
    period_to=datetime.now(),  # required — The effective datetime the statement closes at.
    opening_unfunded=0.0,  # required — The unfunded commitment at the opening datetime, from the register.
    contributions_inside_commitment=0.0,  # required — Capital called inside the commitment over the period, which reduces unfunded. Contributions outside the commitment, such as equalisation interest, are listed but do not count here.
    recallable_distributions=0.0,  # required — Distributions over the period returned as recallable, which restore unfunded.
    expired_recallable=0.0,  # required — Recallable distributions whose recall deadline passed in the period without being recalled, which reduce unfunded.
    commitment_changes=0.0,  # required — Changes to the commitment over the period, which move unfunded one for one.
    transfers=0.0,  # required — Commitment transferred in or out over the period, which moves unfunded one for one.
    closing_unfunded=0.0,  # required — Opening unfunded less contributions inside the commitment, plus recallable distributions, less expired recallable, plus or minus commitment changes and transfers.
    register_unfunded=0.0,  # required — The unfunded commitment at the closing datetime, from the register.
    difference=0.0,  # required — Closing unfunded less the register&#39;s unfunded at the closing datetime. Zero when the statement ties.
    ties=True,  # required — Whether the closing unfunded equals the register&#39;s unfunded at the closing datetime.
    lines=[]  # required — Every booked allocation to the partner over the period, in event date order, with the ILPA transaction type each is reported under and its effect on unfunded.
)
```

- [ResourceId](ResourceId.md)
- [FundPartnerUnfundedReconciliationLine](FundPartnerUnfundedReconciliationLine.md) — used in `lines`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

