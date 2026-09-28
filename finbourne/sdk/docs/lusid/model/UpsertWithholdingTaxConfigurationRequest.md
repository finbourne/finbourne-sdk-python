# UpsertWithholdingTaxConfigurationRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **anomaly_dataset** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **main_dataset** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **source_priority** | **List[str]** | Optional | The rule sources in priority order, most preferred first. Optional: a single-source customer configures none and leaves ruleSource blank on every rate row, in which case no source filter is applied and specificity alone decides. |
| **value_sources** | [List[WithholdingTaxValueSource]](WithholdingTaxValueSource.md) | Optional | One declaration per customer-defined matching dimension across both datasets, naming where the engine reads that dimension&#39;s value from. A dataset column name cannot imply a storage location, so a declaration is required for every customer dimension: an unmapped dimension is never supplied by the matching request, so no row ever matches on it and the customer silently gets a broader rate than they configured. No declaration is required for taxCountry or profileType, which the engine fills from the waterfall, nor for ruleSource, which is compared against SourcePriority. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertWithholdingTaxConfigurationRequest import UpsertWithholdingTaxConfigurationRequest

instance = UpsertWithholdingTaxConfigurationRequest(
    anomaly_dataset=ResourceId(...),  # required
    main_dataset=ResourceId(...),  # required
    source_priority=,  # optional — The rule sources in priority order, most preferred first. Optional: a single-source customer configures none and leaves ruleSource blank on every rate row, in which case no source filter is applied and specificity alone decides.
    value_sources=[]  # optional — One declaration per customer-defined matching dimension across both datasets, naming where the engine reads that dimension&#39;s value from. A dataset column name cannot imply a storage location, so a declaration is required for every customer dimension: an unmapped dimension is never supplied by the matching request, so no row ever matches on it and the customer silently gets a broader rate than they configured. No declaration is required for taxCountry or profileType, which the engine fills from the waterfall, nor for ruleSource, which is compared against SourcePriority.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [WithholdingTaxValueSource](WithholdingTaxValueSource.md) — used in `value_sources`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

