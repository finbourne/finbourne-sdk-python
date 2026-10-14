# FundTermsVersion

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **terms_version_id** | **str** | Required | *No description available.* |
| **effective_from** | **datetime** | Required | *No description available.* |
| **fees** | [List[FeeDefinition]](FeeDefinition.md) | Optional | *No description available.* |
| **carry** | [CarryParameters](CarryParameters.md) | Optional | *No description available.* |
| **recycling** | [RecyclingTerms](RecyclingTerms.md) | Optional | *No description available.* |
| **equalisation** | [EqualisationTerms](EqualisationTerms.md) | Optional | *No description available.* |
| **applies_from_closing_id** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundTermsVersion import FundTermsVersion

instance = FundTermsVersion(
    terms_version_id="...",  # required
    effective_from=datetime.now(),  # required
    fees=[],  # optional
    carry=CarryParameters(...),  # optional
    recycling=RecyclingTerms(...),  # optional
    equalisation=EqualisationTerms(...),  # optional
    applies_from_closing_id="..."  # optional
)
```

- [FeeDefinition](FeeDefinition.md)
- [CarryParameters](CarryParameters.md)
- [RecyclingTerms](RecyclingTerms.md)
- [EqualisationTerms](EqualisationTerms.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

