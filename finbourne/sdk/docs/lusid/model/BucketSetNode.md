# BucketSetNode

One node within a bucket set result: the fund aggregate or a single share class. Both carry NAV and buckets; the  capital ratio, the unit counts and the per-unit values are set only on share class nodes.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **node_type** | **str** | Required | The kind of node: the fund aggregate or a single share class. Available values: Fund, Class. |
| **share_class_short_code** | **str** | Optional | The short code of the share class this node is for, or null for the fund node. |
| **nav** | **float** | Optional | The net asset value at this node, in the fund currency, or null where it does not apply to the node type. |
| **capital_ratio** | **float** | Optional | The share class&#39;s capital ratio (its share of the fund NAV), set only on share class nodes. |
| **buckets** | [List[BucketSetResultBucket]](BucketSetResultBucket.md) | Required | The buckets on this node, each with its period movement and cumulative values. |
| **per_unit_value** | **float** | Optional | The share class&#39;s NAV per unit in issue, in the fund currency, rounded to the share class&#39;s PricePrecision (left unrounded where the share class declares none). Reported only for a share class that is unitised and has units in issue to divide by. The dealing price - in the share class currency, with its instrument&#39;s rounding convention applied - is on the share class breakdown&#39;s unitisation data. |
| **shares_in_issue** | **float** | Optional | The share class&#39;s units in issue at the end of the period. Reported only for a share class that is unitised. |
| **previous_per_unit_value** | **float** | Optional | The share class&#39;s NAV per unit at the previous valuation point, on the same basis as PerUnitValue. |
| **previous_shares_in_issue** | **float** | Optional | The share class&#39;s units in issue at the start of the period. Reported only for a share class that is unitised. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSetNode import BucketSetNode

instance = BucketSetNode(
    node_type="...",  # required — The kind of node: the fund aggregate or a single share class. Available values: Fund, Class.
    share_class_short_code="...",  # optional — The short code of the share class this node is for, or null for the fund node.
    nav=0.0,  # optional — The net asset value at this node, in the fund currency, or null where it does not apply to the node type.
    capital_ratio=0.0,  # optional — The share class&#39;s capital ratio (its share of the fund NAV), set only on share class nodes.
    buckets=[],  # required — The buckets on this node, each with its period movement and cumulative values.
    per_unit_value=0.0,  # optional — The share class&#39;s NAV per unit in issue, in the fund currency, rounded to the share class&#39;s PricePrecision (left unrounded where the share class declares none). Reported only for a share class that is unitised and has units in issue to divide by. The dealing price - in the share class currency, with its instrument&#39;s rounding convention applied - is on the share class breakdown&#39;s unitisation data.
    shares_in_issue=0.0,  # optional — The share class&#39;s units in issue at the end of the period. Reported only for a share class that is unitised.
    previous_per_unit_value=0.0,  # optional — The share class&#39;s NAV per unit at the previous valuation point, on the same basis as PerUnitValue.
    previous_shares_in_issue=0.0  # optional — The share class&#39;s units in issue at the start of the period. Reported only for a share class that is unitised.
)
```

- [BucketSetResultBucket](BucketSetResultBucket.md) — used in `buckets`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

