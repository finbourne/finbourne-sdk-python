# PortfolioIdList

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [List[ResourceId]](ResourceId.md) | Required | *No description available.* |
| **reference_list_type** | **str** | Required | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioIdList import PortfolioIdList

instance = PortfolioIdList(
    values=[],  # required
    reference_list_type="..."  # required — The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

