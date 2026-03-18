# UpsertInvestmentAccountsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, InvestmentAccount]](InvestmentAccount.md) | Optional | The investment accounts which have been successfully updated or created. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The investment accounts that could not be updated or created or were left unchanged without error along with a reason for their failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertInvestmentAccountsResponse import UpsertInvestmentAccountsResponse

instance = UpsertInvestmentAccountsResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=InvestmentAccount(...),  # optional — The investment accounts which have been successfully updated or created.
    failed=ErrorDetail(...),  # optional — The investment accounts that could not be updated or created or were left unchanged without error along with a reason for their failure.
    links=[]  # optional
)
```

- [InvestmentAccount](InvestmentAccount.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

