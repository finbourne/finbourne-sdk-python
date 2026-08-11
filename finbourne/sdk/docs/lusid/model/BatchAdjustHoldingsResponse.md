# BatchAdjustHoldingsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, HoldingAdjustmentWithDate]](HoldingAdjustmentWithDate.md) | Optional | The holdings which have been successfully adjusted. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The holdings that could not be adjusted along with a reason for their failure. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Contains warnings related to adjusted holdings |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchAdjustHoldingsResponse import BatchAdjustHoldingsResponse

instance = BatchAdjustHoldingsResponse(
    values=HoldingAdjustmentWithDate(...),  # optional — The holdings which have been successfully adjusted.
    failed=ErrorDetail(...),  # optional — The holdings that could not be adjusted along with a reason for their failure.
    metadata=,  # optional — Contains warnings related to adjusted holdings
    links=[]  # optional
)
```


## Related Models

- [HoldingAdjustmentWithDate](HoldingAdjustmentWithDate.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

