# PartnerStatement

A partner's statement: the figures of their position on the fund over a period, fingerprinted so a later  statement can be compared against it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **statement_id** | **str** | Required | The identifier of the statement. |
| **fund_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **investor_record_id** | **str** | Required | The investor record the statement is for. |
| **period_start** | **datetime** | Required | The start of the statement period, exclusive. |
| **period_end** | **datetime** | Required | The end of the statement period, inclusive. |
| **nav_type_code** | **str** | Required | The NAV type to produce the statement under. Defaults to the fund&#39;s primary NAV type. |
| **currency** | **str** | Required | The currency of the statement. |
| **lines** | [List[PartnerStatementLine]](PartnerStatementLine.md) | Required | The figures on the statement. |
| **fingerprint** | **str** | Required | A hash of the statement&#39;s content, so two statements can be told apart. |
| **produced_as_at** | **datetime** | Required | When the statement was produced. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerStatement import PartnerStatement

instance = PartnerStatement(
    statement_id="...",  # required — The identifier of the statement.
    fund_id=ResourceId(...),  # required
    investor_record_id="...",  # required — The investor record the statement is for.
    period_start=datetime.now(),  # required — The start of the statement period, exclusive.
    period_end=datetime.now(),  # required — The end of the statement period, inclusive.
    nav_type_code="...",  # required — The NAV type to produce the statement under. Defaults to the fund&#39;s primary NAV type.
    currency="...",  # required — The currency of the statement.
    lines=[],  # required — The figures on the statement.
    fingerprint="...",  # required — A hash of the statement&#39;s content, so two statements can be told apart.
    produced_as_at=datetime.now()  # required — When the statement was produced.
)
```

- [ResourceId](ResourceId.md)
- [PartnerStatementLine](PartnerStatementLine.md) — used in `lines`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

