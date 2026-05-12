# VersionedResourceListOfFundA2BDataRecord

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Required | *No description available.* |
| **values** | [List[FundA2BDataRecord]](FundA2BDataRecord.md) | Required | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **next_page** | **str** | Optional | *No description available.* |
| **previous_page** | **str** | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VersionedResourceListOfFundA2BDataRecord import VersionedResourceListOfFundA2BDataRecord

instance = VersionedResourceListOfFundA2BDataRecord(
    version=Version(...),  # required
    values=[],  # required
    href="...",  # optional
    next_page="...",  # optional
    previous_page="...",  # optional
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [FundA2BDataRecord](FundA2BDataRecord.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

