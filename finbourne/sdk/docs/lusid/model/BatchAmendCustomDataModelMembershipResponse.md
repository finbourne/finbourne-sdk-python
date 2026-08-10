# BatchAmendCustomDataModelMembershipResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [../model/Dict[str, MembershipAmendmentResponse]](MembershipAmendmentResponse.md) | Optional | *No description available.* |
| **staged** | [../model/Dict[str, MembershipAmendmentResponse]](MembershipAmendmentResponse.md) | Optional | *No description available.* |
| **failed** | [../model/Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | *No description available.* |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchAmendCustomDataModelMembershipResponse import BatchAmendCustomDataModelMembershipResponse

instance = BatchAmendCustomDataModelMembershipResponse(
    values=MembershipAmendmentResponse(...),  # optional
    staged=MembershipAmendmentResponse(...),  # optional
    failed=ErrorDetail(...),  # optional
    metadata=  # optional
)
```


## Related Models

- [MembershipAmendmentResponse](MembershipAmendmentResponse.md)
- [MembershipAmendmentResponse](MembershipAmendmentResponse.md)
- [ErrorDetail](ErrorDetail.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

