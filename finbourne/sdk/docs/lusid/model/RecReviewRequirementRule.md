# RecReviewRequirementRule

What the results of one structural category need by way of review: the requirement they carry by default,  and an optional condition that flips it for the results it selects.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **review_requirement** | **str** | Required | Whether this category&#39;s results need reviewing. One of: Required, NotRequired. Available values: Required, NotRequired. |
| **override_condition** | **str** | Optional | A boolean expression over a rec result, e.g. \&quot;resultType eq &#39;Cross&#39;\&quot;. Where it holds for a result, that result is treated as the opposite of the category&#39;s reviewRequirement. Null means the requirement applies to every result in the category. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecReviewRequirementRule import RecReviewRequirementRule

instance = RecReviewRequirementRule(
    review_requirement="...",  # required — Whether this category&#39;s results need reviewing. One of: Required, NotRequired. Available values: Required, NotRequired.
    override_condition="..."  # optional — A boolean expression over a rec result, e.g. \&quot;resultType eq &#39;Cross&#39;\&quot;. Where it holds for a result, that result is treated as the opposite of the category&#39;s reviewRequirement. Null means the requirement applies to every result in the category.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

