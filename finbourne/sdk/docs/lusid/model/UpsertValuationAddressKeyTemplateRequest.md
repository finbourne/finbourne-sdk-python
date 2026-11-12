# UpsertValuationAddressKeyTemplateRequest

The content of a Valuation Template. An upsert replaces the display name, description and metrics.  If isDefault is not specified, the template keeps its current default flag.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The name of the Valuation Template. |
| **description** | **str** | Optional | A description of the Valuation Template. |
| **metrics** | [List[AggregateSpec]](AggregateSpec.md) | Required | The metrics to calculate in a valuation that uses this template. Each metric is an address key, an operation and optional key options. Valuation Templates do not support returnAs. |
| **is_default** | **bool** | Optional | Set to true to make this template the domain default. The previous default stops being the default. Set to false on the current default to use the system default again. If not specified, the template keeps its current value. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertValuationAddressKeyTemplateRequest import UpsertValuationAddressKeyTemplateRequest

instance = UpsertValuationAddressKeyTemplateRequest(
    display_name="...",  # required — The name of the Valuation Template.
    description="...",  # optional — A description of the Valuation Template.
    metrics=[],  # required — The metrics to calculate in a valuation that uses this template. Each metric is an address key, an operation and optional key options. Valuation Templates do not support returnAs.
    is_default=True  # optional — Set to true to make this template the domain default. The previous default stops being the default. Set to false on the current default to use the system default again. If not specified, the template keeps its current value.
)
```

- [AggregateSpec](AggregateSpec.md) — used in `metrics`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

