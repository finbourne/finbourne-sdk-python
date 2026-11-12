# BucketCurrencySubtotal

A bucket's balances for one payment currency, summed across portfolios and sub-holding keys.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bucket_start** | **datetime** | Optional | The start of the period the subtotal covers. |
| **bucket_end** | **datetime** | Optional | The end of the period the subtotal covers. |
| **currency** | **str** | Optional | The payment currency. |
| **open** | [BucketAmounts](BucketAmounts.md) | Optional | *No description available.* |
| **activity_total** | [BucketAmounts](BucketAmounts.md) | Optional | *No description available.* |
| **close** | [BucketAmounts](BucketAmounts.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketCurrencySubtotal import BucketCurrencySubtotal

instance = BucketCurrencySubtotal(
    bucket_start=datetime.now(),  # optional — The start of the period the subtotal covers.
    bucket_end=datetime.now(),  # optional — The end of the period the subtotal covers.
    currency="...",  # optional — The payment currency.
    open=BucketAmounts(...),  # optional
    activity_total=BucketAmounts(...),  # optional
    close=BucketAmounts(...),  # optional
    links=[]  # optional
)
```

- [BucketAmounts](BucketAmounts.md)
- [BucketAmounts](BucketAmounts.md)
- [BucketAmounts](BucketAmounts.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

