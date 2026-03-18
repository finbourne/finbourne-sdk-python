# TimeOfDay

A time of the day

## oneOf Type

`TimeOfDay` can be one of the following types:

* [CutLabelReference](./CutLabelReference.md)
* [SpecifiedTime](./SpecifiedTime.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.workflow.models.TimeOfDay import TimeOfDay

# Construct using any of the compatible types above
cut_label_reference_instance = workflow.models.cut_label_reference.CutLabelReference(
                        code = 'z', 
                        type = 'CutLabel', )

instance = TimeOfDay(cut_label_reference_instance)
```

## Related Models

- [CutLabelReference](./CutLabelReference.md)
- [SpecifiedTime](./SpecifiedTime.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

