# TaxCostRecord

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **tax_cost_record_code** | **str** | Optional | The code of the Tax Cost Record, unique within the Fund. |
| **portfolio_scope** | **str** | Required | The scope of the portfolio the holding belongs to. |
| **portfolio_code** | **str** | Required | The code of the portfolio the holding belongs to. |
| **instrument_identifier** | **str** | Required | The LUSID instrument identifier (LUID) of the holding the tax cost applies to. |
| **nav_type_code** | **str** | Optional | The code of the NAV type the tax cost applies to. Optional; omit for the fund&#39;s primary NAV type. |
| **tax_cost** | **float** | Required | The tax cost of the holding at the effective period end, in the fund&#39;s base currency. |
| **carried_forward_amount** | **float** | Required | The amount carried forward into the next tax period, in the fund&#39;s base currency. |
| **effective_period_end** | **datetime** | Required | The end date of the tax period the record applies to. |
| **source_valuation_point_id** | **str** | Optional | The identifier of the valuation point the record was derived from. Optional; omit for externally supplied records. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxCostRecord import TaxCostRecord

instance = TaxCostRecord(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    tax_cost_record_code="...",  # optional — The code of the Tax Cost Record, unique within the Fund.
    portfolio_scope="...",  # required — The scope of the portfolio the holding belongs to.
    portfolio_code="...",  # required — The code of the portfolio the holding belongs to.
    instrument_identifier="...",  # required — The LUSID instrument identifier (LUID) of the holding the tax cost applies to.
    nav_type_code="...",  # optional — The code of the NAV type the tax cost applies to. Optional; omit for the fund&#39;s primary NAV type.
    tax_cost=0.0,  # required — The tax cost of the holding at the effective period end, in the fund&#39;s base currency.
    carried_forward_amount=0.0,  # required — The amount carried forward into the next tax period, in the fund&#39;s base currency.
    effective_period_end=datetime.now(),  # required — The end date of the tax period the record applies to.
    source_valuation_point_id="...",  # optional — The identifier of the valuation point the record was derived from. Optional; omit for externally supplied records.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

