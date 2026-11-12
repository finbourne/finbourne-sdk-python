# FilteredPortfolioIdList

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **filter** | **str** | Required | The filter that selects the portfolios in the list. It is stored as given and resolved against the portfolios the caller is entitled to see each time the list is read. Supports portfolio fields (e.g. id.scope, displayName, type) and portfolio properties (e.g. properties[Portfolio/MyScope/Strategy] eq &#39;Equity&#39;). Relationship filters are not supported. Time-variant properties are evaluated at the asAt of the request; there is no effectiveAt. On upsert the filter must resolve successfully. |
| **values** | [List[ResourceId]](ResourceId.md) | Optional | The ids of the portfolios the filter resolved to when the list was read. Read only; must not be supplied on upsert. *(read-only)* |
| **reference_list_type** | **str** | Required | The reference list values. Available values: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList, FilteredPortfolioIdList. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FilteredPortfolioIdList import FilteredPortfolioIdList

instance = FilteredPortfolioIdList(
    filter="...",  # required — The filter that selects the portfolios in the list. It is stored as given and resolved against the portfolios the caller is entitled to see each time the list is read. Supports portfolio fields (e.g. id.scope, displayName, type) and portfolio properties (e.g. properties[Portfolio/MyScope/Strategy] eq &#39;Equity&#39;). Relationship filters are not supported. Time-variant properties are evaluated at the asAt of the request; there is no effectiveAt. On upsert the filter must resolve successfully.
    values=[],  # optional — The ids of the portfolios the filter resolved to when the list was read. Read only; must not be supplied on upsert.
    reference_list_type="..."  # required — The reference list values. Available values: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList, FilteredPortfolioIdList.
)
```

- [ResourceId](ResourceId.md) — used in `values`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

