# AllocationMapParticipants

Who takes part in the allocations of an Allocation Map: the default rule that finds the participant set, and the  exceptions that exclude particular investor records or fix their share.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule** | **str** | Optional | How the default participant set is found. AllCommittedToMembers takes every investor record committed to any of the funds in memberIds; ExplicitList takes exactly the investor records in explicitInvestorRecordIds. Available values: AllCommittedToMembers, ExplicitList. |
| **member_ids** | [List[ResourceId]](ResourceId.md) | Optional | Under the AllCommittedToMembers rule, the member funds whose committed investor records participate, as scope and code. At least one is required under that rule. |
| **explicit_investor_record_ids** | **List[str]** | Optional | Under the ExplicitList rule, the investor records that participate. At least one is required under that rule. |
| **exceptions** | [List[AllocationMapException]](AllocationMapException.md) | Optional | Departures from the default participation for particular investor records. Each names the investor record, what happens to it, and why. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapParticipants import AllocationMapParticipants

instance = AllocationMapParticipants(
    rule="...",  # optional — How the default participant set is found. AllCommittedToMembers takes every investor record committed to any of the funds in memberIds; ExplicitList takes exactly the investor records in explicitInvestorRecordIds. Available values: AllCommittedToMembers, ExplicitList.
    member_ids=[],  # optional — Under the AllCommittedToMembers rule, the member funds whose committed investor records participate, as scope and code. At least one is required under that rule.
    explicit_investor_record_ids=,  # optional — Under the ExplicitList rule, the investor records that participate. At least one is required under that rule.
    exceptions=[]  # optional — Departures from the default participation for particular investor records. Each names the investor record, what happens to it, and why.
)
```

- [ResourceId](ResourceId.md) — used in `member_ids`
- [AllocationMapException](AllocationMapException.md) — used in `exceptions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

