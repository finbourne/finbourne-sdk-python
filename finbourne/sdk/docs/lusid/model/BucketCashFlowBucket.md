# BucketCashFlowBucket

One tenor bucket for one portfolio, payment currency and set of sub-holding keys: its opening balance, closing balance and the  cash flows that make up its activity.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bucket_id** | **str** | Optional | Identifies the bucket: a 32 character lowercase hexadecimal hash of its period (start and end), payment currency, portfolio and sub-holding keys. It is stable, the same bucket has the same id in every response, and it is opaque: compare it, do not take it apart. |
| **bucket_start** | **datetime** | Optional | The start of the period the bucket covers. |
| **bucket_end** | **datetime** | Optional | The end of the period the bucket covers. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **currency** | **str** | Optional | The payment currency of the bucket. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The sub-holding keys the bucket is for, limited to those the caller may read. |
| **open** | [BucketAmounts](BucketAmounts.md) | Optional | *No description available.* |
| **activity_total** | [BucketAmounts](BucketAmounts.md) | Optional | *No description available.* |
| **activity** | [List[CashFlowDetail]](CashFlowDetail.md) | Optional | The cash flows in the bucket, with the attributes a cash flow has in Values. |
| **close** | [BucketAmounts](BucketAmounts.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketCashFlowBucket import BucketCashFlowBucket

instance = BucketCashFlowBucket(
    bucket_id="...",  # optional — Identifies the bucket: a 32 character lowercase hexadecimal hash of its period (start and end), payment currency, portfolio and sub-holding keys. It is stable, the same bucket has the same id in every response, and it is opaque: compare it, do not take it apart.
    bucket_start=datetime.now(),  # optional — The start of the period the bucket covers.
    bucket_end=datetime.now(),  # optional — The end of the period the bucket covers.
    portfolio_id=ResourceId(...),  # optional
    currency="...",  # optional — The payment currency of the bucket.
    sub_holding_keys=PerpetualProperty(...),  # optional — The sub-holding keys the bucket is for, limited to those the caller may read.
    open=BucketAmounts(...),  # optional
    activity_total=BucketAmounts(...),  # optional
    activity=[],  # optional — The cash flows in the bucket, with the attributes a cash flow has in Values.
    close=BucketAmounts(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [BucketAmounts](BucketAmounts.md)
- [BucketAmounts](BucketAmounts.md)
- [CashFlowDetail](CashFlowDetail.md) — used in `activity`
- [BucketAmounts](BucketAmounts.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

