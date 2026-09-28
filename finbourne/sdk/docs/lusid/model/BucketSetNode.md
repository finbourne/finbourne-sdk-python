# BucketSetNode

One node within a bucket set result: the fund aggregate or a single share class. Both carry NAV and buckets; the  capital ratio, the unit counts and the per-unit values belong to share class nodes and are omitted on the fund node.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **node_type** | **str** | Required | The kind of node: the fund aggregate or a single share class. Available values: Fund, Class. |
| **share_class_short_code** | **str** | Optional | The short code of the share class this node is for. Omitted on the fund node. |
| **nav** | **float** | Optional | The net asset value at this node, in the fund currency. |
| **capital_ratio** | **float** | Optional | The share class&#39;s capital ratio (its share of the fund NAV). Omitted on the fund node. |
| **buckets** | [List[BucketSetResultBucket]](BucketSetResultBucket.md) | Required | The buckets on this node, each with its period movement and cumulative values. |
| **per_unit_value** | **float** | Optional | The share class&#39;s NAV per unit in issue, in the fund currency, rounded to the share class&#39;s PricePrecision (left unrounded where the share class declares none). Omitted on the fund node, for a share class that is not unitised, and for a unitised share class with no units in issue to divide by (SharesInIssue is then reported as zero). The dealing price - in the share class currency, with its instrument&#39;s rounding convention applied - is on the share class breakdown&#39;s unitisation data. |
| **shares_in_issue** | **float** | Optional | The share class&#39;s units in issue at the end of the period. Omitted on the fund node and for a share class that is not unitised. |
| **previous_per_unit_value** | **float** | Optional | The share class&#39;s NAV per unit at the previous valuation point, on the same basis as PerUnitValue. Omitted on the fund node, for a share class that is not unitised, and where the share class had no units in issue at the previous valuation point (including the fund&#39;s first valuation point). |
| **previous_shares_in_issue** | **float** | Optional | The share class&#39;s units in issue at the start of the period. Omitted on the fund node and for a share class that is not unitised; zero at the fund&#39;s first valuation point. |
| **label** | **str** | Optional | A display label for the node: the fund&#39;s display name on the fund node, the share class&#39;s name on a share class node. |
| **previous_nav** | **float** | Optional | The net asset value this node carried at the previous valuation point, in the fund currency. Zero at the fund&#39;s first valuation point. |
| **net_dealing_units** | **float** | Optional | The net units dealt for the share class over the period, so that the shares in issue are the previous shares in issue plus this. Omitted on the fund node and where the bucket set is not unitised. |
| **share_class_details** | [BucketSetShareClassDetails](BucketSetShareClassDetails.md) | Optional | *No description available.* |
| **nav_share_class_currency** | **float** | Optional | The node&#39;s net asset value restated in the share class&#39; own currency, at the rate this node publishes. Set only on share class nodes. |
| **share_class_to_fund_fx_rate** | **float** | Optional | The fx rate from the share class currency to the fund currency at this valuation point. Nav and the bucket values are in the fund currency, so divide by this rate to restate them in the share class currency. Set only on share class nodes. |
| **previous_nav_share_class_currency** | **float** | Optional | The net asset value in the share class&#39; currency at the previous valuation point, as that point published it, at the rate that point struck. Zero at the fund&#39;s first valuation point. Absent (rather than zero) if the previous valuation point predates this field. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSetNode import BucketSetNode

instance = BucketSetNode(
    node_type="...",  # required — The kind of node: the fund aggregate or a single share class. Available values: Fund, Class.
    share_class_short_code="...",  # optional — The short code of the share class this node is for. Omitted on the fund node.
    nav=0.0,  # optional — The net asset value at this node, in the fund currency.
    capital_ratio=0.0,  # optional — The share class&#39;s capital ratio (its share of the fund NAV). Omitted on the fund node.
    buckets=[],  # required — The buckets on this node, each with its period movement and cumulative values.
    per_unit_value=0.0,  # optional — The share class&#39;s NAV per unit in issue, in the fund currency, rounded to the share class&#39;s PricePrecision (left unrounded where the share class declares none). Omitted on the fund node, for a share class that is not unitised, and for a unitised share class with no units in issue to divide by (SharesInIssue is then reported as zero). The dealing price - in the share class currency, with its instrument&#39;s rounding convention applied - is on the share class breakdown&#39;s unitisation data.
    shares_in_issue=0.0,  # optional — The share class&#39;s units in issue at the end of the period. Omitted on the fund node and for a share class that is not unitised.
    previous_per_unit_value=0.0,  # optional — The share class&#39;s NAV per unit at the previous valuation point, on the same basis as PerUnitValue. Omitted on the fund node, for a share class that is not unitised, and where the share class had no units in issue at the previous valuation point (including the fund&#39;s first valuation point).
    previous_shares_in_issue=0.0,  # optional — The share class&#39;s units in issue at the start of the period. Omitted on the fund node and for a share class that is not unitised; zero at the fund&#39;s first valuation point.
    label="...",  # optional — A display label for the node: the fund&#39;s display name on the fund node, the share class&#39;s name on a share class node.
    previous_nav=0.0,  # optional — The net asset value this node carried at the previous valuation point, in the fund currency. Zero at the fund&#39;s first valuation point.
    net_dealing_units=0.0,  # optional — The net units dealt for the share class over the period, so that the shares in issue are the previous shares in issue plus this. Omitted on the fund node and where the bucket set is not unitised.
    share_class_details=BucketSetShareClassDetails(...),  # optional
    nav_share_class_currency=0.0,  # optional — The node&#39;s net asset value restated in the share class&#39; own currency, at the rate this node publishes. Set only on share class nodes.
    share_class_to_fund_fx_rate=0.0,  # optional — The fx rate from the share class currency to the fund currency at this valuation point. Nav and the bucket values are in the fund currency, so divide by this rate to restate them in the share class currency. Set only on share class nodes.
    previous_nav_share_class_currency=0.0  # optional — The net asset value in the share class&#39; currency at the previous valuation point, as that point published it, at the rate that point struck. Zero at the fund&#39;s first valuation point. Absent (rather than zero) if the previous valuation point predates this field.
)
```

- [BucketSetResultBucket](BucketSetResultBucket.md) — used in `buckets`
- [BucketSetShareClassDetails](BucketSetShareClassDetails.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

