# FilteredFundIdList

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **filter** | **str** | Required |  |
| **values** | [List[ResourceId]](ResourceId.md) | Optional |  *(read-only)* |
| **nav_type_codes_hint** | **List[str]** | Optional |  |
| **nav_type_selection** | **str** | Optional | Available values: First, All. |
| **resolved_fund_nav_type_codes** | [List[FundNavTypeCodes]](FundNavTypeCodes.md) | Optional |  *(read-only)* |
| **reference_list_type** | **str** | Required | The reference list values. Available values: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FilteredFundIdList import FilteredFundIdList

instance = FilteredFundIdList(
    filter="...",  # required — 
    values=[],  # optional — 
    nav_type_codes_hint=,  # optional — 
    nav_type_selection="...",  # optional — Available values: First, All.
    resolved_fund_nav_type_codes=[],  # optional — 
    reference_list_type="..."  # required — The reference list values. Available values: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList.
)
```

- [ResourceId](ResourceId.md) — used in `values`
- [FundNavTypeCodes](FundNavTypeCodes.md) — used in `resolved_fund_nav_type_codes`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

