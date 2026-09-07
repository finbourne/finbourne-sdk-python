# EstimateTransferAgencyOrdersResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **successes** | [Dict[str, TransferAgencyOrderEstimateResult]](TransferAgencyOrderEstimateResult.md) | Optional | A dictionary of successfully estimated orders, keyed by the request key. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | A dictionary of failed estimates, keyed by the request key, containing error details. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EstimateTransferAgencyOrdersResponse import EstimateTransferAgencyOrdersResponse

instance = EstimateTransferAgencyOrdersResponse(
    successes=TransferAgencyOrderEstimateResult(...),  # optional — A dictionary of successfully estimated orders, keyed by the request key.
    failed=ErrorDetail(...),  # optional — A dictionary of failed estimates, keyed by the request key, containing error details.
    links=[]  # optional
)
```


## Related Models

- [TransferAgencyOrderEstimateResult](TransferAgencyOrderEstimateResult.md) — used in `successes`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

