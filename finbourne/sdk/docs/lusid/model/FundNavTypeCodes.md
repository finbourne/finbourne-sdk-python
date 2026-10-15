# FundNavTypeCodes

A fund resolved by a filtered fund list, with the NAV type codes matched by the list's hint.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **nav_type_codes** | **List[str]** | Optional |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundNavTypeCodes import FundNavTypeCodes

instance = FundNavTypeCodes(
    fund_id=ResourceId(...),  # optional
    nav_type_codes=  # optional — 
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

