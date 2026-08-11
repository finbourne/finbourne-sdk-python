# FilteredFundIdList

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **filter** | **str** | Required |  |
| **values** | [List[ResourceId]](ResourceId.md) | Optional |  *(read-only)* |
| **reference_list_type** | **str** | Required | The reference list values. Available values: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FilteredFundIdList import FilteredFundIdList

instance = FilteredFundIdList(
    filter="...",  # required — 
    values=[],  # optional — 
    reference_list_type="..."  # required — The reference list values. Available values: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList.
)
```

- [ResourceId](ResourceId.md) — used in `values`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

