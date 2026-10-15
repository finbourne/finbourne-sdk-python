# PartnerStatementDiff

The differences between two of a partner's statements.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **statement_id** | **str** | Required | The identifier of the statement. |
| **against_statement_id** | **str** | Required | The identifier of the statement to compare against. |
| **identical** | **bool** | Required | Whether the two statements carry the same figures. |
| **differences** | [List[PartnerStatementLineDifference]](PartnerStatementLineDifference.md) | Required | The figures that differ between the two statements. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerStatementDiff import PartnerStatementDiff

instance = PartnerStatementDiff(
    statement_id="...",  # required — The identifier of the statement.
    against_statement_id="...",  # required — The identifier of the statement to compare against.
    identical=True,  # required — Whether the two statements carry the same figures.
    differences=[]  # required — The figures that differ between the two statements.
)
```

- [PartnerStatementLineDifference](PartnerStatementLineDifference.md) — used in `differences`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

