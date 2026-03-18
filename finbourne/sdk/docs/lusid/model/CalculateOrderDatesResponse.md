# CalculateOrderDatesResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **successes** | [Dict[str, TransferAgencyDates]](TransferAgencyDates.md) | Optional | A dictionary of successful date calculations, keyed by the request key. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | A dictionary of failed date calculations, keyed by the request key, containing the error details of any failures that occurred during the calculation. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CalculateOrderDatesResponse import CalculateOrderDatesResponse

instance = CalculateOrderDatesResponse(
    successes=TransferAgencyDates(...),  # optional — A dictionary of successful date calculations, keyed by the request key.
    failed=ErrorDetail(...),  # optional — A dictionary of failed date calculations, keyed by the request key, containing the error details of any failures that occurred during the calculation.
    links=[]  # optional
)
```


## Related Models

- [TransferAgencyDates](TransferAgencyDates.md) — used in `successes`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

