# RelativeDateOffset

Defines a date offset which is relative to some anchor date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **days** | **int** | Required | The number of days to add to the anchor date. |
| **business_day_convention** | **str** | Required | The adjustment type to apply to dates that fall upon a non-business day, e.g. modified following or following.    Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest]. |
| **day_type** | **str** | Optional | Indicates if consideration is given to whether a day is a good business day or not when calculating the offset date.    Supported string (enumeration) values are: [Business, Calendar].  Defaults to \&quot;Business\&quot; if not set. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RelativeDateOffset import RelativeDateOffset

instance = RelativeDateOffset(
    days=0,  # required — The number of days to add to the anchor date.
    business_day_convention="...",  # required — The adjustment type to apply to dates that fall upon a non-business day, e.g. modified following or following.    Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest].
    day_type="..."  # optional — Indicates if consideration is given to whether a day is a good business day or not when calculating the offset date.    Supported string (enumeration) values are: [Business, Calendar].  Defaults to \&quot;Business\&quot; if not set.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

