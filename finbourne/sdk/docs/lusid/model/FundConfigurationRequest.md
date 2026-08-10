# FundConfigurationRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required |  |
| **display_name** | **str** | Optional | The name of the Fund. |
| **description** | **str** | Optional | A description for the Fund. |
| **dealing_filters** | [../model/List[ComponentFilter]](ComponentFilter.md) | Optional | The set of filters used to decide which JE lines are included in the dealing. |
| **pnl_filters** | [../model/List[ComponentFilter]](ComponentFilter.md) | Optional | The set of filters used to decide which JE lines are included in the PnL. |
| **back_out_filters** | [../model/List[ComponentFilter]](ComponentFilter.md) | Optional | The set of filters used to decide which JE lines are included in the back outs. |
| **external_fee_filters** | [../model/List[ExternalFeeComponentFilter]](ExternalFeeComponentFilter.md) | Optional | The set of filters used to decide which JE lines are used for inputting fees from an external source. |
| **bucket_sets** | [../model/List[BucketSetDefinition]](BucketSetDefinition.md) | Optional | The ordered set of component bucket set definitions for this fund configuration. Each bucket set defines how JE lines are grouped into buckets at VP finalisation. |
| **properties** | [../model/Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Fund Configuration. |
| **apportionment_bucket_set** | **str** | Optional | The code of the bucket set definition within this fund configuration that is designated as the apportionment bucket set. Must reference a BucketSetDefinition code within the BucketSets collection. |
| **apportionment_method_property** | [../model/ApportionmentMethodProperty](ApportionmentMethodProperty.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundConfigurationRequest import FundConfigurationRequest

instance = FundConfigurationRequest(
    code="...",  # required — 
    display_name="...",  # optional — The name of the Fund.
    description="...",  # optional — A description for the Fund.
    dealing_filters=[],  # optional — The set of filters used to decide which JE lines are included in the dealing.
    pnl_filters=[],  # optional — The set of filters used to decide which JE lines are included in the PnL.
    back_out_filters=[],  # optional — The set of filters used to decide which JE lines are included in the back outs.
    external_fee_filters=[],  # optional — The set of filters used to decide which JE lines are used for inputting fees from an external source.
    bucket_sets=[],  # optional — The ordered set of component bucket set definitions for this fund configuration. Each bucket set defines how JE lines are grouped into buckets at VP finalisation.
    properties=ModelProperty(...),  # optional — A set of properties for the Fund Configuration.
    apportionment_bucket_set="...",  # optional — The code of the bucket set definition within this fund configuration that is designated as the apportionment bucket set. Must reference a BucketSetDefinition code within the BucketSets collection.
    apportionment_method_property=ApportionmentMethodProperty(...)  # optional
)
```

- [ComponentFilter](ComponentFilter.md) — used in `dealing_filters`
- [ComponentFilter](ComponentFilter.md) — used in `pnl_filters`
- [ComponentFilter](ComponentFilter.md) — used in `back_out_filters`
- [ExternalFeeComponentFilter](ExternalFeeComponentFilter.md) — used in `external_fee_filters`
- [BucketSetDefinition](BucketSetDefinition.md) — used in `bucket_sets`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [ApportionmentMethodProperty](ApportionmentMethodProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

