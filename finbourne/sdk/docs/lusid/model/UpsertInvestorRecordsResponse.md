# UpsertInvestorRecordsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, InvestorRecord]](InvestorRecord.md) | Optional | The investor records which have been successfully updated or created. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The investor records that could not be updated or created or were left unchanged without error along with a reason for their failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertInvestorRecordsResponse import UpsertInvestorRecordsResponse

instance = UpsertInvestorRecordsResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=InvestorRecord(...),  # optional — The investor records which have been successfully updated or created.
    failed=ErrorDetail(...),  # optional — The investor records that could not be updated or created or were left unchanged without error along with a reason for their failure.
    links=[]  # optional
)
```

- [InvestorRecord](InvestorRecord.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

