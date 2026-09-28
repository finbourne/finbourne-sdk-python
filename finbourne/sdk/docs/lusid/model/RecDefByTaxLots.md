# RecDefByTaxLots

Per-side tax-lot granularity for a Holding entry of a rec definition's rulesets.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | **bool** | Optional | Whether the left side splits holdings by tax lot. Must be omitted when the left side is relational, and reads as null there. |
| **right** | **bool** | Optional | Whether the right side splits holdings by tax lot. Must be omitted when the right side is relational, and reads as null there. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecDefByTaxLots import RecDefByTaxLots

instance = RecDefByTaxLots(
    left=True,  # optional — Whether the left side splits holdings by tax lot. Must be omitted when the left side is relational, and reads as null there.
    right=True  # optional — Whether the right side splits holdings by tax lot. Must be omitted when the right side is relational, and reads as null there.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

