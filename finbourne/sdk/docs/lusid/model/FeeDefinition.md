# FeeDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fee_code** | **str** | Required | *No description available.* |
| **basis** | **str** | Required | Available values: CommittedCapital, InvestedCapital, NetInvestedCapital, Nav. |
| **rate** | **float** | Optional | *No description available.* |
| **tiers** | [List[FeeSizeTier]](FeeSizeTier.md) | Optional | *No description available.* |
| **day_count_convention** | **str** | Optional | *No description available.* |
| **step_down** | [FeeStepDown](FeeStepDown.md) | Optional | *No description available.* |
| **offset_percentage** | **float** | Optional | *No description available.* |
| **waiver_percentage** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FeeDefinition import FeeDefinition

instance = FeeDefinition(
    fee_code="...",  # required
    basis="...",  # required — Available values: CommittedCapital, InvestedCapital, NetInvestedCapital, Nav.
    rate=0.0,  # optional
    tiers=[],  # optional
    day_count_convention="...",  # optional
    step_down=FeeStepDown(...),  # optional
    offset_percentage=0.0,  # optional
    waiver_percentage=0.0  # optional
)
```

- [FeeSizeTier](FeeSizeTier.md)
- [FeeStepDown](FeeStepDown.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

