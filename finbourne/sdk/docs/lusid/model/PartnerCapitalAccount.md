# PartnerCapitalAccount

A partner's capital account statement (PCAP) over a reporting period, in the ILPA row order, with quarter-,  year- and inception-to-date columns and a memo block of commitment balances from the register.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **investor_record_id** | **str** | Required | The investor record identifier of the partner. |
| **currency** | **str** | Required | The currency the capital account is expressed in, being the fund&#39;s base currency. |
| **period_start** | **datetime** | Required | The exclusive start of the reporting period. |
| **period_end** | **datetime** | Required | The inclusive end of the reporting period. |
| **status** | **str** | Required | Whether the figures are an Estimate or Final. Figures are Final only once a valuation point covering the period end has been finalised. |
| **rows** | [List[PartnerCapitalAccountRow]](PartnerCapitalAccountRow.md) | Required | The capital account rows, from beginning capital through to ending capital, each with quarter-to-date, year-to-date and inception-to-date columns. |
| **memo** | [PartnerCapitalAccountMemo](PartnerCapitalAccountMemo.md) | Required | *No description available.* |
| **foots** | **bool** | Required | Whether the ending capital agrees across the quarter-to-date, year-to-date and inception-to-date columns within tolerance. |
| **footing_difference** | **float** | Required | The largest difference between the ending capital of any two columns. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerCapitalAccount import PartnerCapitalAccount

instance = PartnerCapitalAccount(
    fund_id=ResourceId(...),  # required
    investor_record_id="...",  # required — The investor record identifier of the partner.
    currency="...",  # required — The currency the capital account is expressed in, being the fund&#39;s base currency.
    period_start=datetime.now(),  # required — The exclusive start of the reporting period.
    period_end=datetime.now(),  # required — The inclusive end of the reporting period.
    status="...",  # required — Whether the figures are an Estimate or Final. Figures are Final only once a valuation point covering the period end has been finalised.
    rows=[],  # required — The capital account rows, from beginning capital through to ending capital, each with quarter-to-date, year-to-date and inception-to-date columns.
    memo=PartnerCapitalAccountMemo(...),  # required
    foots=True,  # required — Whether the ending capital agrees across the quarter-to-date, year-to-date and inception-to-date columns within tolerance.
    footing_difference=0.0  # required — The largest difference between the ending capital of any two columns.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PartnerCapitalAccountRow](PartnerCapitalAccountRow.md) — used in `rows`
- [PartnerCapitalAccountMemo](PartnerCapitalAccountMemo.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

