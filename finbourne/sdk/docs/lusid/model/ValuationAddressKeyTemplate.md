# ValuationAddressKeyTemplate

A set of valuation metrics and grouping keys. Funds and NAV Types reference a template by its id.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Optional | The name of the Valuation Template. |
| **description** | **str** | Optional | A description of the Valuation Template. |
| **metrics** | [List[AggregateSpec]](AggregateSpec.md) | Optional | The metrics to calculate in a valuation that uses this template. Each metric is an address key, an operation and optional key options. Valuation Templates do not support returnAs. |
| **is_default** | **bool** | Optional | True if this is the default Valuation Template, which applies when neither the Fund nor the NAV Type references a template. A domain has one default. Set isDefault on UpsertValuationAddressKeyTemplate to change it. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ValuationAddressKeyTemplate import ValuationAddressKeyTemplate

instance = ValuationAddressKeyTemplate(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    display_name="...",  # optional — The name of the Valuation Template.
    description="...",  # optional — A description of the Valuation Template.
    metrics=[],  # optional — The metrics to calculate in a valuation that uses this template. Each metric is an address key, an operation and optional key options. Valuation Templates do not support returnAs.
    is_default=True,  # optional — True if this is the default Valuation Template, which applies when neither the Fund nor the NAV Type references a template. A domain has one default. Set isDefault on UpsertValuationAddressKeyTemplate to change it.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [AggregateSpec](AggregateSpec.md) — used in `metrics`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

