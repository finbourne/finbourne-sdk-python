# BucketBorderConfiguration

Configuration determining how the borders of bucket intervals behave when allocating cash flows to buckets.  When supplied, cash flows are bucketed into intervals defined by the bucketing dates rather than being  rounded to the nearest bucketing date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_inclusive** | **bool** | Optional | Is the start of the first bucket interval inclusive of its start date. Defaults to true. |
| **end_inclusive** | **bool** | Optional | Is the end of the last bucket interval inclusive of its end date. Defaults to false. |
| **boundary_belongs_to** | **str** | Optional | For boundaries shared by two adjacent intervals, which interval a cash flow falling exactly on the  boundary belongs to. Supported string (enumeration) values are: [Earlier, Later]. Defaults to &#39;Earlier&#39;. Available values: Earlier, Later. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketBorderConfiguration import BucketBorderConfiguration

instance = BucketBorderConfiguration(
    start_inclusive=True,  # optional — Is the start of the first bucket interval inclusive of its start date. Defaults to true.
    end_inclusive=True,  # optional — Is the end of the last bucket interval inclusive of its end date. Defaults to false.
    boundary_belongs_to="..."  # optional — For boundaries shared by two adjacent intervals, which interval a cash flow falling exactly on the  boundary belongs to. Supported string (enumeration) values are: [Earlier, Later]. Defaults to &#39;Earlier&#39;. Available values: Earlier, Later.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

