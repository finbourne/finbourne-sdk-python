# ApportionmentMemberFactor

One member share class's outcome within an apportionment result: the base value the method produced for it  and the resulting apportionment factor.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **member_identifier** | **str** | Required | The member share class&#39;s short code. |
| **fund_scope** | **str** | Optional | The scope of the fund the member share class belongs to. |
| **fund_code** | **str** | Optional | The code of the fund the member share class belongs to. |
| **base_value** | **float** | Optional | The base value the method produced for the member, or null for the SetFactor method. |
| **apportionment_factor** | **float** | Required | The member&#39;s apportionment factor: its base value over the total across the group or fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ApportionmentMemberFactor import ApportionmentMemberFactor

instance = ApportionmentMemberFactor(
    member_identifier="...",  # required — The member share class&#39;s short code.
    fund_scope="...",  # optional — The scope of the fund the member share class belongs to.
    fund_code="...",  # optional — The code of the fund the member share class belongs to.
    base_value=0.0,  # optional — The base value the method produced for the member, or null for the SetFactor method.
    apportionment_factor=0.0  # required — The member&#39;s apportionment factor: its base value over the total across the group or fund.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

