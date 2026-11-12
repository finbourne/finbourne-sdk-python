# MarginExplanationComponent

One step in the working behind a margin figure: a value and, unless it is a leaf, the arithmetic over its  sub-components that gives it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | Identifies the component within its explanation: its position in the tree as dot-separated indexes from the root, such as 0.1.3, the first index being the root&#39;s place among the explanation&#39;s components. |
| **component** | **str** | Required | A stable name for what the component is, such as PvInBase. A component whose rows the caller may not read is named Redacted. |
| **display_name** | **str** | Required | A human-readable name for the component. |
| **type** | **str** | Required | How the component takes its value. One of DerivedProperty, PartialFormula, Variable or Literal. |
| **value** | **float** | Optional | The figure the engine used for the component, as it was computed. Null where the component has none or, for a redacted component, where the rows it stands in for do not share a unit and currency. |
| **unit** | **str** | Optional | What the value measures. One of Currency, Percentage, Factor, Units or Years. Null where the value is unitless. |
| **currency** | **str** | Optional | The currency of a Currency value when it is not the explanation&#39;s currency. |
| **derivation_formula** | **str** | Optional | Plain arithmetic over the sub-components that gives the component&#39;s value. Null for a component with no sub-components. |
| **sub_components** | [List[MarginExplanationComponent]](MarginExplanationComponent.md) | Optional | The components the derivation formula reads. Null for a component that cannot be broken down further. |
| **redacted** | **bool** | Optional | True for a component that stands in for the working of portfolios the caller may not read. The caller sees that those portfolios contributed and, when their rows share a unit and currency, their combined value, so that the parent still adds up to the figure; never which portfolios or holdings they were. Null otherwise. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginExplanationComponent import MarginExplanationComponent

instance = MarginExplanationComponent(
    id="...",  # required — Identifies the component within its explanation: its position in the tree as dot-separated indexes from the root, such as 0.1.3, the first index being the root&#39;s place among the explanation&#39;s components.
    component="...",  # required — A stable name for what the component is, such as PvInBase. A component whose rows the caller may not read is named Redacted.
    display_name="...",  # required — A human-readable name for the component.
    type="...",  # required — How the component takes its value. One of DerivedProperty, PartialFormula, Variable or Literal.
    value=0.0,  # optional — The figure the engine used for the component, as it was computed. Null where the component has none or, for a redacted component, where the rows it stands in for do not share a unit and currency.
    unit="...",  # optional — What the value measures. One of Currency, Percentage, Factor, Units or Years. Null where the value is unitless.
    currency="...",  # optional — The currency of a Currency value when it is not the explanation&#39;s currency.
    derivation_formula="...",  # optional — Plain arithmetic over the sub-components that gives the component&#39;s value. Null for a component with no sub-components.
    sub_components=[],  # optional — The components the derivation formula reads. Null for a component that cannot be broken down further.
    redacted=True  # optional — True for a component that stands in for the working of portfolios the caller may not read. The caller sees that those portfolios contributed and, when their rows share a unit and currency, their combined value, so that the parent still adds up to the figure; never which portfolios or holdings they were. Null otherwise.
)
```

- [MarginExplanationComponent](MarginExplanationComponent.md) — used in `sub_components`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

