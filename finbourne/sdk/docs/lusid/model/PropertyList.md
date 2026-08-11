# PropertyList

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [List[ModelProperty]](ModelProperty.md) | Required | *No description available.* |
| **reference_list_type** | **str** | Required | The reference list values. Available values: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PropertyList import PropertyList

instance = PropertyList(
    values=[],  # required
    reference_list_type="..."  # required — The reference list values. Available values: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList.
)
```


## Related Models

- [ModelProperty](ModelProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

