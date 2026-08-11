# InlinedPropertyDesign

Representation of a set of inlined properties for a given provider so that SQL can be generated to be able to inline properties into luminesce
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **provider_name** | **str** | Optional | The provider name for which these properties are to be inlined |
| **provider_name_extension** | **str** | Optional | The provider extension name for extended providers |
| **inlined_property_items** | [List[InlinedPropertyItem]](InlinedPropertyItem.md) | Optional | Collection of Inlined properties |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.InlinedPropertyDesign import InlinedPropertyDesign

instance = InlinedPropertyDesign(
    provider_name="...",  # optional — The provider name for which these properties are to be inlined
    provider_name_extension="...",  # optional — The provider extension name for extended providers
    inlined_property_items=[]  # optional — Collection of Inlined properties
)
```

- [InlinedPropertyItem](InlinedPropertyItem.md) — used in `inlined_property_items`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

