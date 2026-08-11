# DataModelMembership

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **membership** | [List[Membership]](Membership.md) | Required | The collection of data models this entity is a member of. |
| **current_model** | [MembershipAndStatus](MembershipAndStatus.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DataModelMembership import DataModelMembership

instance = DataModelMembership(
    membership=[],  # required — The collection of data models this entity is a member of.
    current_model=MembershipAndStatus(...)  # optional
)
```


## Related Models

- [Membership](Membership.md) — used in `membership`
- [MembershipAndStatus](MembershipAndStatus.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

