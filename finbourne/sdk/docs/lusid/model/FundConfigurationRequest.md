# FundConfigurationRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required |  |
| **display_name** | **str** | Optional | The name of the Fund. |
| **description** | **str** | Optional | A description for the Fund. |
| **dealing_filters** | [List[ComponentFilter]](ComponentFilter.md) | Required | The set of filters used to decide which JE lines are included in the dealing. |
| **pnl_filters** | [List[ComponentFilter]](ComponentFilter.md) | Required | The set of filters used to decide which JE lines are included in the PnL. |
| **back_out_filters** | [List[ComponentFilter]](ComponentFilter.md) | Required | The set of filters used to decide which JE lines are included in the back outs. |
| **external_fee_filters** | [List[ExternalFeeComponentFilter]](ExternalFeeComponentFilter.md) | Optional | The set of filters used to decide which JE lines are used for inputting fees from an external source. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Fund Configuration. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundConfigurationRequest import FundConfigurationRequest

instance = FundConfigurationRequest(
    code="...",  # required — 
    display_name="...",  # optional — The name of the Fund.
    description="...",  # optional — A description for the Fund.
    dealing_filters=[],  # required — The set of filters used to decide which JE lines are included in the dealing.
    pnl_filters=[],  # required — The set of filters used to decide which JE lines are included in the PnL.
    back_out_filters=[],  # required — The set of filters used to decide which JE lines are included in the back outs.
    external_fee_filters=[],  # optional — The set of filters used to decide which JE lines are used for inputting fees from an external source.
    properties=ModelProperty(...)  # optional — A set of properties for the Fund Configuration.
)
```

- [ComponentFilter](ComponentFilter.md) — used in `dealing_filters`
- [ComponentFilter](ComponentFilter.md) — used in `pnl_filters`
- [ComponentFilter](ComponentFilter.md) — used in `back_out_filters`
- [ExternalFeeComponentFilter](ExternalFeeComponentFilter.md) — used in `external_fee_filters`
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

