# ShareClassData

The data for a Share Class. Includes Valuation Point Data and instrument information.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **share_class_breakdown** | [ShareClassBreakdown](ShareClassBreakdown.md) | Required | *No description available.* |
| **share_class_details** | [ShareClassDetails](ShareClassDetails.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ShareClassData import ShareClassData

instance = ShareClassData(
    share_class_breakdown=ShareClassBreakdown(...),  # required
    share_class_details=ShareClassDetails(...)  # optional
)
```


## Related Models

- [ShareClassBreakdown](ShareClassBreakdown.md)
- [ShareClassDetails](ShareClassDetails.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

