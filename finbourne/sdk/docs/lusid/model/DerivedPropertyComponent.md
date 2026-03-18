# DerivedPropertyComponent

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **component** | **str** | Optional | The component of the formula which is being evaluated. |
| **display_name** | **str** | Optional | The display name of the component being evaluated. |
| **type** | **str** | Optional | The type of the formula component. This can be a Literal, Variable, DerivedProperty, or PartialFormula. |
| **value** | [PropertyValue](PropertyValue.md) | Optional | *No description available.* |
| **derivation_formula** | **str** | Optional | The derivation formula of the component. This field will only be populated if the component is a derived property. |
| **sub_components** | [List[DerivedPropertyComponent]](DerivedPropertyComponent.md) | Optional | Any sub-components of this formula. If this formula cannot be further decomposed, this collection will be null. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DerivedPropertyComponent import DerivedPropertyComponent

instance = DerivedPropertyComponent(
    component="...",  # optional — The component of the formula which is being evaluated.
    display_name="...",  # optional — The display name of the component being evaluated.
    type="...",  # optional — The type of the formula component. This can be a Literal, Variable, DerivedProperty, or PartialFormula.
    value=PropertyValue(...),  # optional
    derivation_formula="...",  # optional — The derivation formula of the component. This field will only be populated if the component is a derived property.
    sub_components=[],  # optional — Any sub-components of this formula. If this formula cannot be further decomposed, this collection will be null.
    links=[]  # optional
)
```

- [PropertyValue](PropertyValue.md)
- [DerivedPropertyComponent](DerivedPropertyComponent.md) — used in `sub_components`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

