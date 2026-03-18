# ShareClassDealingBreakdown

The breakdown of Dealing for a Share Class.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **class_dealing** | [Dict[str, ShareClassAmount]](ShareClassAmount.md) | Required | Bucket of detail for any &#39;Dealing&#39; specific to the share class that has occured inside the queried period. |
| **class_dealing_units** | [Dict[str, Amount]](Amount.md) | Required | Bucket of detail for any &#39;Dealing&#39; units specific to the share class that has occured inside the queried period. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ShareClassDealingBreakdown import ShareClassDealingBreakdown

instance = ShareClassDealingBreakdown(
    class_dealing=ShareClassAmount(...),  # required — Bucket of detail for any &#39;Dealing&#39; specific to the share class that has occured inside the queried period.
    class_dealing_units=Amount(...)  # required — Bucket of detail for any &#39;Dealing&#39; units specific to the share class that has occured inside the queried period.
)
```


## Related Models

- [ShareClassAmount](ShareClassAmount.md) — used in `class_dealing`
- [Amount](Amount.md) — used in `class_dealing_units`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

