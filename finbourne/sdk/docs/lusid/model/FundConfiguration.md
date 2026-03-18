# FundConfiguration

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Optional | The name of the FundConfiguration. |
| **description** | **str** | Optional | A description for the FundConfiguration. |
| **dealing_filters** | [List[ComponentFilter]](ComponentFilter.md) | Optional | The set of filters used to decide which JE lines are included in the dealing. |
| **pnl_filters** | [List[ComponentFilter]](ComponentFilter.md) | Optional | The set of filters used to decide which JE lines are included in the PnL. |
| **back_out_filters** | [List[ComponentFilter]](ComponentFilter.md) | Optional | The set of filters used to decide which JE lines are included in the back outs. |
| **external_fee_filters** | [List[ExternalFeeComponentFilter]](ExternalFeeComponentFilter.md) | Optional | The set of filters used to decide which JE lines are used for inputting fees from an external source. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Fund Configuration. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundConfiguration import FundConfiguration

instance = FundConfiguration(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    display_name="...",  # optional — The name of the FundConfiguration.
    description="...",  # optional — A description for the FundConfiguration.
    dealing_filters=[],  # optional — The set of filters used to decide which JE lines are included in the dealing.
    pnl_filters=[],  # optional — The set of filters used to decide which JE lines are included in the PnL.
    back_out_filters=[],  # optional — The set of filters used to decide which JE lines are included in the back outs.
    external_fee_filters=[],  # optional — The set of filters used to decide which JE lines are used for inputting fees from an external source.
    properties=ModelProperty(...),  # optional — A set of properties for the Fund Configuration.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [ComponentFilter](ComponentFilter.md) — used in `dealing_filters`
- [ComponentFilter](ComponentFilter.md) — used in `pnl_filters`
- [ComponentFilter](ComponentFilter.md) — used in `back_out_filters`
- [ExternalFeeComponentFilter](ExternalFeeComponentFilter.md) — used in `external_fee_filters`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

